# retroarch.py
from retroArchGame import *
from gamehelpers import *
from dialog import *
import re
 

def getBackgroundImage(platform: str, country: str) -> str:
    result = get_random_image(os.path.join(platform ,"background"))
    if(result == ''):
        result = os.path.join(CurrentSettings.imagePath, "background_default.png")
    return result

def getImage(title:str, platform: str, country: str) -> str:
 
    result =  find_first_cart_matching_image(platform,f"*{title} ({country})*")
    if(result == ''):
        result =  find_first_cart_matching_image(platform,f"*{title}*")
    #if(result == ''):
    #    result = os.path.join(CurrentSettings.imagePath, "default.png")
    return result

#attempt to initially get core from extension, else extract it from folder name
def getPlatform(path: str, core: str) -> str:
    extension = os.path.splitext(path)[1]
    platform = getPlatformFromExtension(extension)    
    if platform == 'unknown':
        split = core.split(' (')[0].strip()
        platform = getFolderFromCore(split)
    return platform

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
    developer: str
    year: int
    image_url:str
    
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
        showDialog("Image_url: ", self.image_url)
        showDialog("Background Image: ", self.background_image)
        showDialog("Developer: ", self.developer)
        showDialog("Description: ", self.description[:40])
        showDialog("Year: ", self.year)
        showDialogShort("----------------------------")

    def getNameFromRetroArch(self, game ) -> str:
        if(game.label != ''): 
            return game.label
        else:
            tmp = re.search(r'[^\\]+\.(\w+)$', self.path).group()      
            tmp = os.path.splitext(tmp)[0]        
            tmp = tmp.split('(')[0].strip()
            print(tmp)  
            return tmp
        
    def createFromApi(self, game: GameParams):
        self.path = ''
        self.core = '' #game.core_name
        self.filename = ''#os.path.basename(game.path)
        
        self.country = 'Usa'       
        self.platform = game.platform # getPlatform(self.path, self.core)
        
        self.title = game.name #getNameFromRetroArch(game)
        self.image = getImage(self.title, self.platform, self.country)
        self.background_image = getBackgroundImage(self.platform, self.country)
        self.description = ""
        self.year = 0
        self.image_url = ""
        self.developer = ""
    
    def createFromRetroarch(self, game: RetroArchGame):
        self.path = game.path
        self.core = game.core_name
        self.filename = os.path.basename(game.path)
        
        self.country = getCountry(self.filename)        
        self.platform = getPlatform(self.path, self.core)
        
        self.title = self.getNameFromRetroArch(game)
        self.image = getImage(self.title, self.platform, self.country)
        self.background_image = getBackgroundImage(self.platform, self.country)
        self.description = ""
        self.year = 0
        self.image_url = ""
        self.developer = ""
        
    def updateFromIgdb(self, igdb):
        if igdb is None:
            return
        self.description = igdb.summary
        self.year = igdb.year
        self.image_url = igdb.image 
        self.developer = igdb.developer
