from emulatordb import  getFolderFromCore, getPlatformFromExtension
import os
import re
import fnmatch

from retroarch import RetroArchGame
# Retroarch's installation folder:
__imagePath__: str = ""
def init_paths(image_path):
    global __imagePath__
    if __imagePath__ == "": # see notes below; explicit test for None
        __imagePath__ = image_path
    else:
        raise RuntimeError("Database name has already been set.") 

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


def getNameFromRetroArch( game: RetroArchGame) -> str:
    if(game.label != ''): 
        return game.label
    else:
        tmp = re.search(r'[^\\]+\.(\w+)$', game.path).group()      
        tmp = os.path.splitext(tmp)[0]        
        tmp = tmp.split('[')[0].strip()
        print(tmp)  
        return tmp

def getCountry(filename:str) -> str:
    return re.findall(r'\((.*?)\)', filename)[0]

def getLastFolder(file: str, path: str) -> str:
    path = path.replace(file, '')
    return os.path.basename(path)
    

def getImage(title:str, platform: str) -> str:
 
    result =  find_first_matching_image(platform,'*' + title + '*')
    if(result == ''):
        title = title.split('(')[0].strip()
        result = find_first_matching_image(platform,'*' + title + '*')
    if(result == ''):
        result = os.join(__imagePath__, "default.png")
    return result

def getPlatform(path: str, core: str) -> str:
    extension = os.path.splitext(path)[1]
    platform = getPlatformFromExtension(extension)    
    if platform == 'unknown':
        split = core.split(' (')[0].strip()
        platform = getFolderFromCore(split)
    return platform

 