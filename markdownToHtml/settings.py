import os 
import sys
from file_monitor import FileMonitor
import markdown_observer

def set_working_directory_to_exe_location():
    if getattr(sys, "frozen", False):
        # If the script is frozen (e.g., an executable created by PyInstaller)
        exe_dir = os.path.dirname(sys.executable)
        os.chdir(exe_dir)
    else:
        # If the script is running in a non-frozen environment (e.g., in a development environment)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)

def ensureSettingsExists():
    if not os.path.exists('settings.ini'):
        with open('settings.ini', 'w') as file:
            file.write('# Folder to analyze for updates')
            file.write('inputFolder=C:\\Users\\lance\\SynologyDrive\\obsidian\\Projects\\API\\Learning\n')
            file.write('# Markdown Path\n')
            file.write('inputFile=C:\\Users\\lance\\SynologyDrive\\obsidian\\Projects\\API\\Learning\\Goals.md\n')
            file.write('outputFile=D:\\obs_assets\\goals.html\n')
            file.write('# To not slam the CPU, set the number of seconds the script will pause for a few seconds between runs.\n')
            file.write('sleep_seconds=2\n')
            file.write('# Spam when sleeping and no changes\n')
            file.write('verbose=false\n')
            file.write('# Spam when sleeping and no changes\n')
         

class Settings:
    fileMonitor = FileMonitor()
    inputFolder: str
    # File within folder (no path) to check for updates
    inputFile: str
    # Folder to search for image files
    outputFile: str
    # To not slam the CPU, set the number of seconds the script will pause for a few seconds between runs.
    sleep_seconds: int
    # Spam when sleeping and no changes
    verbose: bool

    
    def file(self):
        return os.path.join(self.inputFolder, self.inputFile)
                            
    def importSettings(self):
        print("importing settings")
        settings_dict = {}
        with open('settings.ini', 'r') as file:
            for line in file:
                if (line.startswith('#') or line.startswith(';')):
                    continue
                try:
                    key, value = line.split('=')
                    settings_dict[key.strip()] = value.strip()
                except:
                    print("Error parsing settings file, line: ", line)
        self.inputFile = settings_dict.get('inputFile', 'Goals.md')
        self.inputFolder = settings_dict.get('inputFolder', 'C:\\Users\\lance\\SynologyDrive\\obsidian\\Projects\\API\\Learning')
        self.outputFile = settings_dict.get('outputFile', 'D:\\obs_assets\\goals.html')
        self.sleep_seconds = int(settings_dict.get('sleep_seconds', 2))
        self.verbose = settings_dict.get('verbose', 'false').lower() == 'true'
        
        markdown_observer.Current.update(self.inputFile,self.inputFolder,self.outputFile)
        markdown_observer.Current.startMonitor()

    def startMonitor(self): 
        self.fileMonitor.folder = os.path.dirname(os.path.realpath(__file__))
        self.fileMonitor.filepath = os.path.join(self.fileMonitor.folder, 'settings.ini')
        print (self.fileMonitor.filepath)
        self.fileMonitor.action = self.importSettings
        self.fileMonitor.startMonitor()

    def __init__(self):
        set_working_directory_to_exe_location()
        ensureSettingsExists()
        self.importSettings()
        self.monitorSettings()
        


CurrentSettings: Settings = Settings() 
