import asyncio
import json
import os
import shutil
import time
from poly_igdb import IgdbClient

# from poly-igdb import IgdbClient
from discord_api import update_discord
from emulatordb import getCoreFromSlug
from game import Game
from pyhelpers import save_image_from_url

from retroArchGame import RetroArchGame, importRetroArchGame
from settings import CurrentSettings
from writedisk import writeData


last_game: RetroArchGame = None


def set_current_game() -> RetroArchGame:
    return importRetroArchGame(
        os.path.join(CurrentSettings.retroarch_path, "content_history.lpl")
    )


# if CurrentSettings.use_gui:
#    showWindow()

while True:
    current_game = set_current_game()

    # Did the game change?
    if last_game is None or current_game.path != last_game.path:
        asyncio.run(writeData(current_game))
        last_game = current_game
    else:
        if CurrentSettings.verbose:
            print("No Change")

    # Notifying sleep
    if CurrentSettings.verbose:
        print("Sleeping for", CurrentSettings.sleep_seconds, "seconds")
    time.sleep(CurrentSettings.sleep_seconds)
