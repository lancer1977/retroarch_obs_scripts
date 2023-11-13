import asyncio
import json
import os
import platform
import shutil
import time

from discord_api import update_discord
from emulatordb import getCoreFromSlug
from game import Game
from gui import showWindow
from IgdbClient import IgdbClient
from retroArchGame import RetroArchGame, importRetroArchGame
from settings import CurrentSettings

image_file = os.path.join(CurrentSettings.data_path, "cover.png")
background_file = os.path.join(CurrentSettings.data_path, "background.png")
json_file = os.path.join(CurrentSettings.data_path, "game.json")
name_file = os.path.join(CurrentSettings.data_path, "name.txt")
platform_file = os.path.join(CurrentSettings.data_path, "platform.txt")
_igdbClient = IgdbClient(CurrentSettings.twitch_clientid,
                         CurrentSettings.twitch_secret)
last_game: RetroArchGame = None


def setCurrentGame() -> RetroArchGame:
    return importRetroArchGame(os.path.join(CurrentSettings.retroarch_path, "content_history.lpl"))


async def getGame(current_game: RetroArchGame) -> Game:
    game = Game(current_game)
    game.report()
    igdb = await _igdbClient.getGame(game_name, game.platform)
    game.updateFromIgdb(igdb)
    return game


async def writeData(current_game: RetroArchGame):
    game = getGame(current_game)

    os.makedirs(CurrentSettings.data_path, exist_ok=True)

    # Copy the image to the data folder
    if os.path.exists(game.image):
        print("Writing", game.image, "to", image_file)
        try:
            shutil.copy2(game.image, image_file)
        except:
            print("Could not copy image")

    # Copy the background to the data folder
    if os.path.exists(game.background_image):
        print("Writing", game.background_image, "to", background_file)
        try:
            shutil.copy2(game.background_image, background_file)
        except:
            print("Could not copy image")

    # Update the discord playing API
    update_discord(game.Playing())

    # write game json to disk
    game_json = json.dumps(game.__dict__, indent=2)
    with open(json_file, "w") as file:
        file.write(game_json)

    # write Title to disk
    with open(name_file, "w") as file:
        file.write(game.title)

    # write Platform to disk
    with open(platform_file, "w") as file:
        file.write(getCoreFromSlug(game.platform))


# if CurrentSettings.use_gui:
#    showWindow()

while True:
    current_game = setCurrentGame()

    # Did the game change?
    if last_game is None or current_game.path != last_game.path:
        if os.path.exists(image_file):
            os.remove(image_file)
        asyncio.run(writeData(current_game))
        last_game = current_game
    else:
        if CurrentSettings.verbose:
            print("No Change")

    # Notifying sleep
    if CurrentSettings.verbose:
        print("Sleeping for", CurrentSettings.sleep_seconds, "seconds")
    time.sleep(CurrentSettings.sleep_seconds)
