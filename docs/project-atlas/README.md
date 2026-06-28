# Project Atlas

## Purpose

`retroarch_obs_scripts` watches RetroArch/Batocera current-game state and writes
OBS-friendly files for cover art, background art, title, platform, and metadata.
It is a local automation bridge, not the long-term canonical catalog authority.

## Boundaries

- `Api.VideoGames` owns canonical game identity and resolver behavior.
- `Api.CDN` owns media coverage and media availability checks.
- DreadTV is the preferred future home for reusable OBS-source streaming
  behavior.
- This repo should keep local OBS file writing and small adapters that can be
  validated with fixtures.

## Validation Map

| Surface | Command |
| --- | --- |
| Unit tests | `PYTHONPATH=src:tests python -m unittest discover -s tests -p 'test_*.py' -v` |
| Dependency audit | `pip-audit -r requirements.txt` |
| Full local validation | `bash scripts/validate.sh` |
| DevStudio structure | `devstudio validate --repo .` |

## Manual Smoke

1. Configure `settings.ini` with RetroArch, image, and data paths.
2. Start the watcher with `python src/main.py retroarch`.
3. Launch a RetroArch game and confirm `content_history.lpl` changes.
4. Confirm the configured OBS data folder receives `cover.png`,
   `background.png`, `game.json`, `name.txt`, `platform.txt`, and `all.txt`.
5. Confirm OBS image/text sources refresh from that folder.
