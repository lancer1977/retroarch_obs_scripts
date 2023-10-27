# retroarch.py
from retroarch import RetroArchGame
import os
import re
import fnmatch
# Retroarch's installation folder:
__imagePath__: str = ""
def init_paths(image_path):
    global __imagePath__
    if __imagePath__ == "": # see notes below; explicit test for None
        __imagePath__ = image_path
    else:
        raise RuntimeError("Database name has already been set.") 

def getFolderFromCore(core: str) -> str:
    if core == "Sega - MS":
        return "megadrive"
    if core == "Sega - Mega Drive - Genesis":
        return "megadrive"
    if core == "Sega - Master System - Mark III":
        return "mastersystem"
    if core == "Sega - Game Gear":
        return "gamegear"
    if core == "Sega - SG-1000":
        return "sg1000"
    if core == "Sega - Mega-CD - Sega CD":
        return "segacd"
    if core == "Sega - 32X":
        return "32x"
    if core == "Sony - PlayStation":
        return "psx"
    if core == "Sony - PlayStation 2":
        return "ps2"
    if core == "Microsoft - Xbox":
        return "xbox"
    if core == "Nintendo - Game Boy":
        return "gb"
    if core == "Nintendo - Game Boy Color":
        return "gbc"
    if core == "Nintendo - Game Boy Advance":
        return "gba"
    if core == "Nintendo - Virtual Boy":
        return "virtualboy"
    if core == "Nintendo - Nintendo Entertainment System":
        return "nes"
    if core == "Nintendo - SNES":
        return "snes"
    if core == "Nintendo - Super Nintendo Entertainment System":
        return "snes"
    if core == "Nintendo - Nintendo 64":
        return "n64"

    if core == "Atari - 2600":
        return "atari2600"
    if core == "Atari - 5200":
        return "atari5200"
    if core == "Atari - 7800":
        return "atari7800"
    if core == "Atari - Lynx":
        return "atarilynx"
    if core == "NEC - PC Engine - TurboGrafx 16":
        return "pcengine"
    if core == "NEC - PC Engine CD - TurboGrafx-CD":
        return "pcenginecd"
    if core == "Coleco - ColecoVision":
        return "coleco"
    if core == "Intellivision":
        return "intellivision"
    return ""
    
def find_first_matching_image(subfolder:str, pattern:str) -> str:
    folder = os.path.join(__imagePath__, subfolder)
    boxartFolder = os.path.join(folder, "boxart")
    if(os.path.exists(boxartFolder)):
        folder = boxartFolder
    for root, _, files in os.walk(folder):
        for filename in files:
            if fnmatch.fnmatch(filename, pattern):
                return os.path.join(root, filename)
    return ''


def getNameFromRetroArch(game: RetroArchGame) -> str:
    if(game.label != ''): 
        return game.label
    else:
        print( game.path)
        tmp = re.search(r'[^\\]+\.(\w+)$', game.path).group()      
        tmp = tmp[:-4]
        tmp = tmp.split('[')[0].strip()
        print(tmp)  
        return tmp
    
def getImage(title:str, core:str) -> str:
    folder = getFolderFromCore(core)
    result =  find_first_matching_image(folder,'*' + title + '*')
    if(result == ''):
        title = title.split('(')[0].strip()
        result = find_first_matching_image(folder,'*' + title + '*')
    if(result == ''):
        result = os.join(__imagePath__, "default.png")
    return result

def getCore(game: RetroArchGame) -> str:
    platform = game.core_name.split(' (')[0].strip()
    core = platform.split('/')[0].strip()
    return core

class Game:
    title: str
    core: str
    image: str
    file: str    
        
    def validate(self):
        return self.title != '' and self.core != '' and self.file != '' and self.image != ''
    
    def report(self):
        print("Game: ", self.title)
        print("Core: ", self.core)
        print("File: ", self.file)
        print("Image: ", self.image)
    
    def __init__(self, game: RetroArchGame):
        self.title = getNameFromRetroArch(game)
        self.core = getCore(game)
        self.file = game.path
        self.image = getImage(self.title, self.core)
