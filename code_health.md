# Code Health

## Current Validation

Run the repo validation lane from the repository root:

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
bash scripts/validate.sh
```

The validation script runs:

- Python unittest discovery for `tests/test_*.py`
- `pip-audit -r requirements.txt` for pinned runtime dependencies

GitHub Actions runs the same test and audit surfaces before the container build.

## Runtime Notes

- The script surface is still filesystem/OBS oriented and expects a configured
  `settings.ini` for local RetroArch and OBS asset paths.
- Canonical current-game and media payload normalization is intentionally pure
  Python in `src/canonical_payload.py` so it can move into or integrate with
  DreadTV later without inheriting OBS filesystem side effects.
- Live OBS validation remains manual: run RetroArch, confirm
  `content_history.lpl` changes, and confirm the OBS image/text sources update
  from the configured data directory.

## Remaining Health Watch

- Keep runtime dependencies pinned in `requirements.txt`.
- Keep audit tooling in `requirements-dev.txt`, not the runtime image unless a
  production audit step needs it.
- Add sample `settings.ini` fixtures before expanding write-to-disk behavior.
