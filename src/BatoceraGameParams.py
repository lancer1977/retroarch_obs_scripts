from gamehelpers import getCountry
class BatoceraGameParams:
    path: str
    system: str
    start: str
    emulator: str
    core: str

    def __init__(self):
        self.path = ''
        self.system = ''
        self.start = ''
        self.emulator =''
        self.core = ''
        self.country = ''
    def load(self,values):
        self.start = values['start']
        self.path = values['path']
        self.system = values['system']
        self.emulator = values['emulator']
        self.core = values['core']
        self.country = getCountry(values.get('country', 'U'))