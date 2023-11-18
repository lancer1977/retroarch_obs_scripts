
from settings import CurrentSettings 

def showDialog(title:str, message:str):
    formatted = f"{title} {message}"
    if(CurrentSettings.use_gui):
        print( formatted)
    else:
        print(formatted)

def showDialogShort( message:str):
    formatted = f"{message}"
    if(CurrentSettings.use_gui):
        print( formatted)
    else:
        print(formatted)