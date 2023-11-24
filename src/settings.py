import os
from pyhelpers import set_working_directory_to_exe_location


def ensureSettingsExists():
    if not os.path.exists('settings.ini'):
        with open('settings.ini', 'w') as file:
            file.write('# Path to RetroArch\n')
            file.write('retroarch_path=D:\\LaunchBox\\Emulators\\RetroArch\n')
            file.write('# Path to image folder\n')
            file.write('imagePath=U:\\art\n')
            file.write('# Type of art to display\n')
            file.write('art_type=boxart\n')
            file.write('# Folder to search for image files\n')
            file.write('data_path=D:\\obs_assets\n')
            file.write('# To not slam the CPU, set the number of seconds the script will pause for a few seconds between runs.\n')
            file.write('sleep_seconds=2\n')
            file.write('# Spam when sleeping and no changes\n')
            file.write('verbose=false\n')
            file.write('# Discord integration\n')
            file.write('discord_enable=false\n')
            file.write('# Discord token\n')
            file.write('discord_token=\n')
            file.write('# Use Gui\n')
            file.write('use_gui=false\n')

            file.write('# Twitch twitch_clientid\n')
            file.write('twitch_clientid=\n')
            file.write('# Use Gui\n')
            file.write('twitch_secret=\n')                 

            
            file.write('# Local Api Debug\n')
            file.write('local_api_debug=false\n')
            file.write('# Local Api IP\n')
            file.write('local_api_ip=\n')   
            file.write('# Local Api Port\n')
            file.write('local_api_port=\n')

class Settings:
    local_api_port: str
    local_api_ip: str
    local_api_debug: str
    retroarch_path: str
    imagePath: str
    art_type: str
    # Folder to search for image files
    data_path: str
    # To not slam the CPU, set the number of seconds the script will pause for a few seconds between runs.
    sleep_seconds: int
    # Spam when sleeping and no changes
    verbose: bool
    
    #discord items
    #discord_enable: bool
    discord_token: str
    use_gui: bool

    #twitch items
    twitch_clientid: str
    twitch_secret: str
    twitch_redirect_url: str

    def twitchEnabled(self):
        return self.twitch_clientid != '' and self.twitch_secret != ''

    def discordEnabled(self):
        return self.discord_token != ''
    
    
    def importSettings(self):

        settings_dict = {}
        with open('settings.ini', 'r') as file:
            for line in file:
                if (line.startswith('#') or line.startswith(';')):
                    continue
                key, value = line.split('=')
                settings_dict[key.strip()] = value.strip()
        self.retroarch_path = settings_dict.get('retroarch_path', 'D:\\LaunchBox\\Emulators\\RetroArch')
        self.imagePath = settings_dict.get('imagePath', 'U:\\art')
        self.art_type = settings_dict.get('art_type', 'boxart')
        self.data_path = settings_dict.get('data_path', 'D:\\obs_assets')
        self.sleep_seconds = int(settings_dict.get('sleep_seconds', 2))
        self.verbose = settings_dict.get('verbose', 'false').lower() == 'true'
        #self.discord_enable = settings_dict.get('discord_enable', 'false').lower() == 'true'
        self.discord_token = settings_dict.get('discord_token', '')
        self.use_gui = settings_dict.get('use_gui', 'false').lower() == 'true'

        self.twitch_clientid = settings_dict.get('twitch_clientid', '')
        self.twitch_secret = settings_dict.get('twitch_secret', '')
        
        self.twitch_redirect_url = settings_dict.get('twitch_redirect_url', '')

        self.local_api_port = settings_dict.get('local_api_port', '')
        self.local_api_ip = settings_dict.get('local_api_ip', '')        
        self.local_api_debug = settings_dict.get('local_api_debug', '')

 

    def __init__(self):
        set_working_directory_to_exe_location()
        ensureSettingsExists()
        self.importSettings()


CurrentSettings: Settings = Settings() 
