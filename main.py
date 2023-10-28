import os
import shutil
import time
import json
from game import Game
from retroarch import  RetroArchGame, importRetroArchGame
from settings import CurrentSettings


image_file = os.path.join(CurrentSettings.data_path, "cover.png")
json_file = os.path.join(CurrentSettings.data_path, "game.json")
 
def setCurrentGame()-> RetroArchGame:
    return  importRetroArchGame(os.path.join(CurrentSettings.retroarch_path, "content_history.lpl"))

def writeData(current_game: RetroArchGame):
        game = Game(current_game)
        game.report()        
        if os.path.exists(game.image):
            print("Writing", game.image, "to", image_file)
        os.makedirs(CurrentSettings.data_path, exist_ok=True)
        shutil.copy2(game.image, image_file)             
        
        game_json = json.dumps(game.__dict__, indent=2)
        with open(json_file, "w") as file:
            file.write(game_json)
        


last_game: RetroArchGame = None

while True:
    current_game = setCurrentGame()
    
    if last_game is None or current_game.path != last_game.path:
        if os.path.exists(image_file):
            os.remove(image_file)
        writeData(current_game)      
        last_game = current_game        
    else:
        if CurrentSettings.verbose:
            print("No Change")

    if CurrentSettings.verbose:
        print("Sleeping for", CurrentSettings.sleep_seconds, "seconds")
        
    time.sleep(CurrentSettings.sleep_seconds)
