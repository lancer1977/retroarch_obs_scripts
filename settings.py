from pyhelpers import set_working_directory_to_exe_location
import os

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


class Settings:
    retroarch_path: str
    imagePath: str
    art_type: str
    # Folder to search for image files
    data_path: str
    # To not slam the CPU, set the number of seconds the script will pause for a few seconds between runs.
    sleep_seconds: int
    # Spam when sleeping and no changes
    verbose = bool

    def importSettings(self):

        settings_dict = {}
        with open('settings.ini', 'r') as file:
            for line in file:
                if (line.startswith('#') or line.startswith(';')):
                    continue
                key, value = line.split('=')
                settings_dict[key.strip()] = value.strip()
        self.retroarch_path = settings_dict.get(
            'retroarch_path', 'D:\\LaunchBox\\Emulators\\RetroArch')
        self.imagePath = settings_dict.get('imagePath', 'U:\\art')
        self.art_type = settings_dict.get('art_type', 'boxart')
        self.data_path = settings_dict.get('data_path', 'D:\\obs_assets')
        self.sleep_seconds = int(settings_dict.get('sleep_seconds', 2))
        self.verbose = settings_dict.get('verbose', 'false').lower() == 'true'

    def __init__(self):
        set_working_directory_to_exe_location()
        ensureSettingsExists()
        self.importSettings()


CurrentSettings: Settings = Settings()


