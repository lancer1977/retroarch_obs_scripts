import json
import os
import shutil
from game import Game
from BatoceraGameParams import BatoceraGameParams
from discord_api import update_discord
from emulatordb import getCoreFromSlug 
from pyhelpers import save_image_from_url
from retroArchGame import RetroArchGame
from settings import CurrentSettings
from poly_igdbpy import IgdbClient



_igdbClient = IgdbClient(CurrentSettings.twitch_clientid, CurrentSettings.twitch_secret)

image_file = os.path.join(CurrentSettings.data_path, "cover.png")
background_file = os.path.join(CurrentSettings.data_path, "background.png")
json_file = os.path.join(CurrentSettings.data_path, "game.json")
all_file = os.path.join(CurrentSettings.data_path, "all.txt")
name_file = os.path.join(CurrentSettings.data_path, "name.txt")
platform_file = os.path.join(CurrentSettings.data_path, "platform.txt")

async def writeDataFromGameParams(current_game: BatoceraGameParams) -> Game :
    game = Game()
    game.createFromApi(current_game) 
    await  game.updateFromIgdb(_igdbClient)
    game.report()
    await _writeDataFromGame(game)
    return game

async def writeDataFromRetroArchGame(current_game: RetroArchGame):
    game = Game()
    game.createFromRetroarch(current_game.path, current_game.core_name)
    await game.updateFromIgdb(_igdbClient)
    game.report()
    await _writeDataFromGame(game)
    return game
    
async def _writeDataFromGame(game: Game):  
    os.makedirs(CurrentSettings.data_path, exist_ok=True)
    #cleanup old values
    if os.path.exists(image_file):
        os.remove(image_file)
    if os.path.exists(background_file):
        os.remove(background_file)
    if os.path.exists(all_file):
        os.remove(all_file)


    # Copy the image to the data folder
    if os.path.exists(game.image):
        print("Writing", game.image, "to", image_file)
        try:
            shutil.copy2(game.image, image_file)
        except:
            print("Could not copy image")
    else:
        save_image_from_url(game.image_url, image_file)
        
    # Copy the background to the data folder
    if  (game.background_image):
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
    with open(all_file, "w") as file:
        file.write(
            f"Title: {game.title}\nPlatform: {getCoreFromSlug(game.platform)}\nDeveloper: {game.developer}\nYear:{game.year} \nSumary: {game.description}")
        # \nDeveloper: {game.developer}\nPublisher: {game.publisher}\nRating: {game.rating}\nPlayers: {game.players}\nDescription: {game.description}")
