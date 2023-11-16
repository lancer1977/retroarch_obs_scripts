####!/usr/bin/env python312
# This folder has helpers for extracting information from a retroarch log, and for locating images on disk.
from emulatordb import  getFolderFromCore, getPlatformFromExtension
import os
import random
import fnmatch
import re

from retroArchGame import RetroArchGame 
from settings import CurrentSettings
# Retroarch's installation folder:

def getCountry(filename:str) -> str:
    try:        
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
    except:
        return "World"

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

def get_random_image(subfolder):
    folder = os.path.join(CurrentSettings.imagePath, subfolder) 
    # Check if the folder path exists
    if not os.path.exists(folder):
        return ''

    # Get a list of all files in the folder
    all_files = os.listdir(folder)

    # Filter only the image files (you can customize this based on your file extensions)
    image_files = [file for file in all_files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Check if there are any image files in the folder
    if not image_files:
        print(f"No image files found in '{folder}'.")
        return ''

    # Choose a random image file
    random_image = random.choice(image_files)

    # Return the full path to the random image
    return os.path.join(folder, random_image)

 


def getLastFolder(file: str, path: str) -> str:
    path = path.replace(file, '')
    return os.path.basename(path)

def formatText(value, max):
    if value == None:
        return ''
    if len(value) > max:
        value = value[:max] + "..."
    
    return value