from retroarch_monitor import start
from settings import CurrentSettings
from api import startApi
import asyncio
# main.py
import sys

if __name__ == "__main__":

    if(len(sys.argv) > 1):
        app = sys.argv[1]
    else:
        app= "retroarch"

    if(app == "retroarch"):
        asyncio.run( start(CurrentSettings.retroarch_path, CurrentSettings.sleep_seconds, CurrentSettings.verbose))
    elif(app == "api"):
        asyncio.run( startApi())
        
