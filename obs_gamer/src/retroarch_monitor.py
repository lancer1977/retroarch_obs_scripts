import asyncio 
import os 
import time 

# from poly-igdb import IgdbClient 

from RetroArchGame import RetroArchGame, importRetroArchGame 
from writedisk import writeDataFromRetroArchGame





def _set_current_game(path:str) -> RetroArchGame:
    return importRetroArchGame(
        os.path.join(path, "content_history.lpl")
    )


# if CurrentSettings.use_gui:
#    showWindow()
async def start(path: str, sleep_seconds: int, verbose :bool):
    last_game: RetroArchGame = None
    while True:
        current_game = _set_current_game(path)

        # Did the game change?
        if last_game is None or current_game.path != last_game.path:
            writeDataFromRetroArchGame(current_game)
            last_game = current_game
        else:
            if verbose:
                print("No Change")

        # Notifying sleep
        if verbose:
            print("Sleeping for", sleep_seconds, "seconds")
        time.sleep(sleep_seconds)
