from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class CanonicalCurrentGame:
    state: str
    title: str
    platform: str
    canonical_game_id: int | None = None
    canonical_slug: str = ""
    media_url: str = ""
    confidence: float | None = None
    provenance: list[dict[str, Any]] = field(default_factory=list)
    fallback_reason: str = ""

    @property
    def has_media(self) -> bool:
        return bool(self.media_url)

    @property
    def needs_review(self) -> bool:
        return self.state in ("unknown", "missing_media", "stale", "fallback")


def normalize_canonical_current_game(payload: dict[str, Any] | None) -> CanonicalCurrentGame:
    if not payload:
        return CanonicalCurrentGame(
            state="unknown",
            title="Unknown game",
            platform="unknown",
            fallback_reason="empty payload",
        )

    title = _first_text(payload, "title", "gameTitle", "name") or "Unknown game"
    platform = _first_text(payload, "platform", "platformHint", "system") or "unknown"
    canonical_game_id = _first_int(payload, "canonicalGameId", "gameId", "game_id")
    canonical_slug = _first_text(payload, "canonicalSlug", "canonical_slug") or ""
    media_url = _first_text(payload, "mediaUrl", "imageUrl", "coverUrl") or _preferred_art_url(payload)
    provenance = _provenance(payload)
    confidence = _confidence(payload, provenance)

    if _truthy(payload.get("stale")) or _truthy(payload.get("isStale")):
        return CanonicalCurrentGame(
            state="stale",
            title=title,
            platform=platform,
            canonical_game_id=canonical_game_id,
            canonical_slug=canonical_slug,
            media_url=media_url,
            confidence=confidence,
            provenance=provenance,
            fallback_reason=_first_text(payload, "staleReason", "fallbackReason") or "stale payload",
        )

    if canonical_game_id is None:
        return CanonicalCurrentGame(
            state="unknown",
            title=title,
            platform=platform,
            media_url=media_url,
            confidence=confidence,
            provenance=provenance,
            fallback_reason=_first_text(payload, "fallbackReason") or "canonical game not resolved",
        )

    if not media_url:
        return CanonicalCurrentGame(
            state="missing_media",
            title=title,
            platform=platform,
            canonical_game_id=canonical_game_id,
            canonical_slug=canonical_slug,
            confidence=confidence,
            provenance=provenance,
            fallback_reason="canonical game has no media URL",
        )

    return CanonicalCurrentGame(
        state="known",
        title=title,
        platform=platform,
        canonical_game_id=canonical_game_id,
        canonical_slug=canonical_slug,
        media_url=media_url,
        confidence=confidence,
        provenance=provenance,
    )


def to_obs_payload(current_game: CanonicalCurrentGame) -> dict[str, Any]:
    return {
        "state": current_game.state,
        "title": current_game.title,
        "platform": current_game.platform,
        "canonicalGameId": current_game.canonical_game_id,
        "canonicalSlug": current_game.canonical_slug,
        "mediaUrl": current_game.media_url,
        "confidence": current_game.confidence,
        "provenance": current_game.provenance,
        "fallbackReason": current_game.fallback_reason,
        "needsReview": current_game.needs_review,
    }


def _first_text(payload: dict[str, Any], *keys: str) -> str:
    for key in keys:
        value = payload.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return ""


def _first_int(payload: dict[str, Any], *keys: str) -> int | None:
    for key in keys:
        value = payload.get(key)
        if isinstance(value, bool):
            continue
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
    return None


def _preferred_art_url(payload: dict[str, Any]) -> str:
    preferred_art = payload.get("preferredArt")
    if isinstance(preferred_art, dict):
        return _first_text(preferred_art, "url")
    return ""


def _provenance(payload: dict[str, Any]) -> list[dict[str, Any]]:
    resolver_context = payload.get("resolverContext")
    if isinstance(resolver_context, dict):
        provenance = resolver_context.get("provenance")
        if isinstance(provenance, list):
            return [item for item in provenance if isinstance(item, dict)]

    provenance = payload.get("provenance")
    if isinstance(provenance, list):
        return [item for item in provenance if isinstance(item, dict)]

    return []


def _confidence(payload: dict[str, Any], provenance: list[dict[str, Any]]) -> float | None:
    value = payload.get("confidence")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)

    selected = [item for item in provenance if item.get("isSelected") is True]
    candidates = selected or provenance
    for item in candidates:
        value = item.get("confidence")
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return float(value)

    return None


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in ("1", "true", "yes", "on")
    return False
