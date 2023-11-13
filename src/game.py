# retroarch.py
from retroArchGame import RetroArchGame
from gamehelpers import *
from dialog import *

class Game:
    title: str
    core: str
    country: str
    image: str
    background_image: str
    path: str
    filename: str
    platform: str
    description: str
    year: int
    
    def Playing(self):
        return "Playing " + self.title + " (" + self.platform + ")"
    def validate(self):
        return self.title != '' and self.core != '' and self.file != '' and self.image != ''
    
    def report(self):
        showDialogShort("----------------------------")
        showDialog("Game: ", self.title)
        showDialog("Core: ", self.core)
        showDialog("File Path: ", self.path)
        showDialog("Country: ", self.country)
        showDialog("Filename: ", self.filename)        
        showDialog("Platform: ", self.platform)        
        showDialog("Image: ", self.image)
        showDialog("Background Image: ", self.background_image)
        showDialog("Description: ", self.description)
        showDialog("Year: ", self.year)
        showDialogShort("----------------------------")
    
    def __init__(self, game: RetroArchGame):
        self.path = game.path
        self.core = game.core_name
        self.filename = os.path.basename(game.path)
        
        self.country = getCountry(self.filename)        
        self.platform = getPlatform(self.path, self.core    )
        self.title = game.getNameFromRetroArch()
        self.image = getImage(self.title, self.platform, self.country)
        self.background_image = getBackgroundImage(self.platform, self.country)

    def updateFromIgdb(self, igdb):
        self.description = igdb.summary
        self.year = igdb.year
        self.image = igdb.image 
