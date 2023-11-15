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




def getLastFolder(file: str, path: str) -> str:
    path = path.replace(file, '')
    return os.path.basename(path)

def formatText(value, max):
    if value == None:
        return ''
    if len(value) > max:
        value = value[:max] + "..."
    
    return value