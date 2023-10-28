
import os
import shutil
import time
from game import Game, init_paths
from retroarch import  RetroArchGame, importRetroArchGame
from settings import *



# Messages the console
def notify(title, message):
    print(title + ": " + message)

def setCurrentGame()-> RetroArchGame:
    return  importRetroArchGame(os.path.join(retroarch_path, "content_history.lpl"))

init_paths(imagePath)

last_game: RetroArchGame = None

while True:
    current_game = setCurrentGame()
    
    if last_game is None or current_game.path != last_game.path:
        game = Game(current_game)
        game.report()
        
        target_dir = os.path.join(data_path, "cover.png")
        if os.path.exists(target_dir):
            os.remove(target_dir)
        if os.path.exists(game.image):
            print("image: Writing", game.image)
        os.makedirs(data_path, exist_ok=True)
        shutil.copy2(game.image, target_dir)    
        last_game = current_game
    else:
        if verbose:
            print("No Change")

    if verbose:
        print("Sleeping for", sleep_seconds, "seconds")
        
    time.sleep(sleep_seconds)
