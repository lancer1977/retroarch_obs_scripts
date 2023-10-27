import json


class RetroArchGame:
    path: str
    label: str
    core_path: str
    core_name: str
    crc32: str
    db_name: str

    def __init__(self):
        self.path = ''
        self.label = ''
        self.core_path = ''
        self.core_name = ''
        self.crc32 = ''
        self.db_name = ''

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
