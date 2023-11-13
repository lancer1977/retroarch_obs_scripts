
from settings import CurrentSettings
from gui import updateText

def showDialog(title:str, message:str):
    formatted = f"{title} {message}"
    if(CurrentSettings.use_gui):
        updateText( formatted)
    else:
        print(formatted)

def showDialogShort( message:str):
    formatted = f"{message}"
    if(CurrentSettings.use_gui):
        updateText( formatted)
    else:
        print(formatted)