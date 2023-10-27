
def getFolderFromCore(core: str) -> str:
    if core == "Sega - MS/GG/MD/CD":
        return "segacd"
    if core == "Sega - MS":
        return "megadrive"
    if core == "Sega - Mega Drive - Genesis":
        return "megadrive"
    if core == "Sega - Master System - Mark III":
        return "mastersystem"
    if core == "Sega - Game Gear":
        return "gamegear"
    if core == "Sega - SG-1000":
        return "sg1000"
    if core == "Sega - Mega-CD - Sega CD":
        return "segacd"
    if core == "Sega - 32X":
        return "32x"
    if core == "Sony - PlayStation":
        return "psx"
    if core == "Sony - PlayStation 2":
        return "ps2"
    if core == "Microsoft - Xbox":
        return "xbox"
    if core == "Nintendo - Game Boy":
        return "gb"
    if core == "Nintendo - Game Boy Color":
        return "gbc"
    if core == "Nintendo - Game Boy Advance":
        return "gba"
    if core == "Nintendo - Virtual Boy":
        return "virtualboy"
    if core == "Nintendo - Nintendo Entertainment System":
        return "nes"
    if core == "Nintendo - SNES":
        return "snes"
    if core == "Nintendo - Super Nintendo Entertainment System":
        return "snes"
    if core == "Nintendo - Nintendo 64":
        return "n64"
    if core == "Atari - 2600":
        return "atari2600"
    if core == "Atari - 5200":
        return "atari5200"
    if core == "Atari - 7800":
        return "atari7800"
    if core == "Atari - Lynx":
        return "atarilynx"
    if core == "NEC - PC Engine - TurboGrafx 16":
        return "pcengine"
    if core == "NEC - PC Engine CD - TurboGrafx-CD":
        return "pcenginecd"
    if core == "Coleco - ColecoVision":
        return "coleco"
    if core == "Intellivision":
        return "intellivision"
    return ""

def getPlatformFromExtension(ext:str)-> str:
    if ext == ".iso" or ext == ".cso" or ext == ".bin" or ext == ".img" or ext == ".mdf" or ext == ".cue" or ext == ".ccd" or ext == ".nrg" or ext == ".pbp" or ext == ".chd" or ext == ".zip":
        return "unknown"
    if ext == ".nes":
        return "nes"
    elif ext == ".snes" or ext == ".smc":
        return "snes"
    elif ext == ".gen" or ext == ".md":
        return "genesis"
    elif  ext == ".32x":
        return "32x"
    elif ext == ".pce" or ext == ".cue" or ext == ".sgx":
        return "pce"
    elif ext == ".gb" or ext == ".gbc":
        return "gb"
    elif ext == ".gba":
        return "gba"
    elif ext == ".ngc":
        return "ngc"
    # Add more extensions and their corresponding platforms here
    else:
        return "unknown"
