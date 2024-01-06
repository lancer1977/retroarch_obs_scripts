import re
import emulatordb

from difflib import get_close_matches
from poly_igdbpy import IgdbClient
from settings import CurrentSettings

_igdbClient = IgdbClient(CurrentSettings.twitch_clientid,
                         CurrentSettings.twitch_secret)


async def getPlatformInfo() -> str:
    platforms = await _igdbClient.getPlatformData()
    return platforms 


async def getIgdbMaps():
    # x.get('name','No Name') for x in
    def normalize_string(s):
        try:
            s = s.encode('ascii', 'ignore').decode(
                'ascii')  # Remove non-ascii characters
            s = s.lower()  # Convert to lowercase
            s = re.sub(r'[^a-z0-9]', '', s)  # Remove special characters
            return s
        except:
            return s

    igdbPlatforms = await getPlatformInfo()

    filePlatfomrs = emulatordb.gamePlatforms()
    unknowns = []

    for folder in filePlatfomrs:
        normalized_folder = normalize_string(folder)
        matches = get_close_matches(
            normalized_folder, igdbPlatforms, cutoff=0.6)
        if matches:
            matching_platform = matches[0]

            print(f"\"{folder}\":\"{matching_platform.get('id', 'error')}\",# {
                  matching_platform.get('name', 'error')}")
            # igdbPlatforms = next((x for x in my_list if x % 2 == 0), None)
            # normalized_igdb.(matching_platform)
        else:
            unknowns.append(f"\"{folder}\":\"unknown\",")
    # for unknown in unknowns:
        # print(unknown)
    for unknown in igdbPlatforms:
        print(f"\"{unknown['id']}\"") # : \"{str(unknown['name'])}\",")

def readPlatformsCsv():
    #this is intended to map folder names to platform ids with some hints
    with open('D:\\code\\retro_obs\\platform.csv', 'r') as file:
        platforms = file.readlines()
    print("Folders to IGDB ID :")
    print("-------------------------")
    for platform in platforms:
        platform = platform.replace('\n', '')
        items = platform.split(',')
        
        print(f"\"{items[0]}\" : \"{items[2]}\",")

#asyncio.run(getIgdbMaps())
readPlatformsCsv()

#getFolderPlatforms()