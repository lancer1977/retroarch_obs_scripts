import unittest

from canonical_payload import normalize_canonical_current_game, to_obs_payload


class TestCanonicalPayload(unittest.TestCase):
    def test_known_game_maps_canonical_media_and_provenance(self):
        result = normalize_canonical_current_game({
            "gameId": 42,
            "canonicalSlug": "super-mario-bros-nes",
            "title": "Super Mario Bros.",
            "platformHint": "NES",
            "preferredArt": {
                "url": "https://cdn.example.test/nes/smb-box.png",
            },
            "resolverContext": {
                "provenance": [
                    {
                        "provider": "ra",
                        "sourceKind": "external-id",
                        "sourceId": "ra:1234",
                        "confidence": 98,
                        "isSelected": True,
                    }
                ]
            },
        })

        self.assertEqual(result.state, "known")
        self.assertEqual(result.canonical_game_id, 42)
        self.assertEqual(result.platform, "NES")
        self.assertEqual(result.media_url, "https://cdn.example.test/nes/smb-box.png")
        self.assertEqual(result.confidence, 98.0)
        self.assertFalse(result.needs_review)

    def test_unknown_game_keeps_safe_fallback_title(self):
        result = normalize_canonical_current_game({
            "gameTitle": "Currently playing",
            "platform": "genesis",
            "fallbackReason": "canonical lookup returned 404",
        })

        self.assertEqual(result.state, "unknown")
        self.assertEqual(result.title, "Currently playing")
        self.assertEqual(result.platform, "genesis")
        self.assertTrue(result.needs_review)
        self.assertEqual(result.fallback_reason, "canonical lookup returned 404")

    def test_missing_media_keeps_canonical_identity(self):
        result = normalize_canonical_current_game({
            "canonicalGameId": "77",
            "canonicalSlug": "mystery-cart",
            "title": "Mystery Cart",
            "platform": "snes",
        })

        self.assertEqual(result.state, "missing_media")
        self.assertEqual(result.canonical_game_id, 77)
        self.assertEqual(result.media_url, "")
        self.assertEqual(result.fallback_reason, "canonical game has no media URL")

    def test_stale_payload_preserves_data_but_requires_review(self):
        result = normalize_canonical_current_game({
            "gameId": 9,
            "title": "Old Game",
            "platform": "arcade",
            "mediaUrl": "https://cdn.example.test/old.png",
            "isStale": True,
            "staleReason": "last observation expired",
        })

        self.assertEqual(result.state, "stale")
        self.assertEqual(result.media_url, "https://cdn.example.test/old.png")
        self.assertTrue(result.needs_review)
        self.assertEqual(result.fallback_reason, "last observation expired")

    def test_obs_payload_uses_stable_camel_case_keys(self):
        result = normalize_canonical_current_game({
            "gameId": 42,
            "title": "Super Mario Bros.",
            "platform": "NES",
            "mediaUrl": "https://cdn.example.test/nes/smb-box.png",
        })

        payload = to_obs_payload(result)

        self.assertEqual(payload["state"], "known")
        self.assertEqual(payload["canonicalGameId"], 42)
        self.assertEqual(payload["mediaUrl"], "https://cdn.example.test/nes/smb-box.png")
        self.assertFalse(payload["needsReview"])


if __name__ == "__main__":
    unittest.main()
