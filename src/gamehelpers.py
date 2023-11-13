####!/usr/bin/env python312
# This folder has helpers for extracting information from a retroarch log, and for locating images on disk.
from emulatordb import  getFolderFromCore, getPlatformFromExtension
import os
import re
import fnmatch

from retroArchGame import RetroArchGame 
from settings import CurrentSettings
# Retroarch's installation folder:



def find_first_matching_image(subfolder:str, pattern:str) -> str:
    folder = os.path.join(CurrentSettings.imagePath, subfolder)
    for root, _, files in os.walk(folder):
        for filename in files:
            if fnmatch.fnmatch(filename, pattern):
                return os.path.join(root, filename)
    return ''

def find_first_cart_matching_image(subfolder:str, pattern:str) -> str:
    folder = os.path.join(CurrentSettings.imagePath, subfolder)
    boxartFolder = os.path.join(folder, CurrentSettings.art_type)
    if(os.path.exists(boxartFolder)):
        folder = boxartFolder
    for root, _, files in os.walk(folder):
        for filename in files:
            if fnmatch.fnmatch(filename, pattern):
                return os.path.join(root, filename)
    return ''


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

    
def getBackgroundImage(platform: str, country: str) -> str:
    filename = "background"
    result =  find_first_matching_image(platform,f"*{filename} ({country})*")
    if(result == ''):
        result =  find_first_matching_image(platform,f"*{filename}*")
    if(result == ''):
        result = os.path.join(CurrentSettings.imagePath, "background_default.png")
    return result

def getImage(title:str, platform: str, country: str) -> str:
 
    result =  find_first_cart_matching_image(platform,f"*{title} ({country})*")
    if(result == ''):
        result =  find_first_cart_matching_image(platform,f"*{title}*")
    if(result == ''):
        result = os.path.join(CurrentSettings.imagePath, "default.png")
    return result

#attempt to initially get core from extension, else extract it from folder name
def getPlatform(path: str, core: str) -> str:
    extension = os.path.splitext(path)[1]
    platform = getPlatformFromExtension(extension)    
    if platform == 'unknown':
        split = core.split(' (')[0].strip()
        platform = getFolderFromCore(split)
    return platform

 