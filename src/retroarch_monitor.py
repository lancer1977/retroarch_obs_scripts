import os 
import time
import json

from retroArchGame import RetroArchGame 
from writedisk import writeDataFromRetroArchGame

def _set_current_game(base_path:str) -> RetroArchGame:
    file = os.path.join(base_path, "content_history.lpl")
    with open(file, 'r') as json_file:
        data = json.load(json_file)
    items = data.get('items', [])
    if items:
        return RetroArchGame(items[0])
    else:
        return None
    
 

# if CurrentSettings.use_gui:
#    showWindow()
async def start(path: str, sleep_seconds: int, verbose :bool):
    last_game: RetroArchGame = None
    while True:
        current_game = _set_current_game(path)

        # Did the game change?
        if last_game is None or current_game.path != last_game.path:
            await writeDataFromRetroArchGame(current_game)
            last_game = current_game
        else:
            if verbose:
                print("No Change")

        # Notifying sleep
        if verbose:
            print("Sleeping for", sleep_seconds, "seconds")
        time.sleep(sleep_seconds)
