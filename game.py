# retroarch.py
from retroarch import RetroArchGame
from gamehelpers import *

class Game:
    title: str
    core: str
    country: str
    image: str
    path: str
    filename: str
        
    def validate(self):
        return self.title != '' and self.core != '' and self.file != '' and self.image != ''
    
    def report(self):
        print("Game: ", self.title)
        print("Core: ", self.core)
        print("File Path: ", self.path)
        print("Country: ", self.country)
        print("Filename: ", self.filename)        
        print("Platform: ", self.platform)        
        print("Image: ", self.image)
    
    def __init__(self, game: RetroArchGame):
        self.path = game.path
        self.core = game.core_name
        self.filename = os.path.basename(game.path)
        
        self.country = getCountry(self.filename)        
        self.platform = getPlatform(self.path, self.core    )
        self.title = getNameFromRetroArch(game)
        self.image = getImage(self.title, self.platform)
