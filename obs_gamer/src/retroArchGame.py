import json
import re
import os

class RetroArchGame:

    def __init__(self, data):
        self.path = data['path']
        self.label = data['label']
        self.core_path = data['core_path']
        self.core_name = data['core_name']
        self.crc32 = data['crc32']
        self.db_name = data['db_name']
        


def importRetroArchGame(directory: str) -> RetroArchGame:
    with open(directory, 'r') as json_file:
        data = json.load(json_file)
    items = data.get('items', [])
    if items:
        return RetroArchGame(items[0])
    else:
        return None


