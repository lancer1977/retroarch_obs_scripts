from emulatordb import  getFolderFromCore, getPlatformFromExtension
import os
import re
import fnmatch

from retroarch import RetroArchGame
from settings import imagePath, art_type
# Retroarch's installation folder:



def find_first_matching_image(subfolder:str, pattern:str) -> str:
    folder = os.path.join(imagePath, subfolder)
    boxartFolder = os.path.join(folder, art_type)
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
        tmp = tmp.split('(')[0].strip()
        print(tmp)  
        return tmp

def getCountry(filename:str) -> str:
    code =  re.findall(r'\((.*?)\)', filename)[0]
    if(code == 'U'):
        return 'USA'
    elif(code == 'E'):
        return 'Europe'
    elif(code == 'J'):
        return 'Japan'
    elif(code == 'W'):
        return 'World'
    else:
        return code
    

def getLastFolder(file: str, path: str) -> str:
    path = path.replace(file, '')
    return os.path.basename(path)
    

def getImage(title:str, platform: str) -> str:
 
    result =  find_first_matching_image(platform,'*' + title + '*')
    if(result == ''):
        title = title.split('(')[0].strip()
        result = find_first_matching_image(platform,'*' + title + '*')
    if(result == ''):
        result = os.path.join(imagePath, "default.png")
    return result

def getPlatform(path: str, core: str) -> str:
    extension = os.path.splitext(path)[1]
    platform = getPlatformFromExtension(extension)    
    if platform == 'unknown':
        split = core.split(' (')[0].strip()
        platform = getFolderFromCore(split)
    return platform

 