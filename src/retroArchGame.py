
class RetroArchGame:

    def __init__(self, data):
        self.path = data['path']
        self.label = data['label']
        self.core_path = data['core_path']
        self.core_name = data['core_name']
        self.crc32 = data['crc32']
        self.db_name = data['db_name']