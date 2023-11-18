import os

def getFolderNames(directory_path: str):
# Get the list of all directories to use as defined platforms on disk
    #directory_path = 'U:\\Roms'
    all_entries = os.listdir(directory_path)
    # Filter only the directories from the entries
    folders = [entry for entry in all_entries if os.path.isdir(os.path.join(directory_path, entry))]    

    for folder in folders:
        print(f"\"{folder}\",")