import sys
import os

def set_working_directory_to_exe_location():
    if getattr(sys, 'frozen', False):
        # If the script is frozen (e.g., an executable created by PyInstaller)
        exe_dir = os.path.dirname(sys.executable)
        os.chdir(exe_dir)
    else:
        # If the script is running in a non-frozen environment (e.g., in a development environment)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_dir)