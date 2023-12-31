# this should be the fallback for ISO based games.

def gamePlatforms() -> list:
    platforms = ["3do",
        "Actionmax",
        "amiga",
        "amigacd32",
        "amstradcpc",
        "arcade",
        "arcade_chd",
        "arcadia",
        "astrocade",
        "atari2600",
        "atari5200",
        "atari7800",
        "atari800",
        "atarijaguar",
        "atarilynx",
        "atarist",
        "c64",
        "channelf",
        "coleco",
        "creativision",
        "crvision",
        "daphne",
        "dos",
        "dreamcast",
        "famicom",
        "fba",
        "fds",
        "gameandwatch",
        "gamecube",
        "gamegear",
        "gb",
        "gba",
        "gbah",
        "gbc",
        "gbh",
        "genh",
        "ggh",
        "intellivision",
        "jaguar",
        "megadrive",
        "megadrive-japan",
        "model123",
        "msdos",
        "msx",
        "msx2",
        "n3ds",
        "n64",
        "naomi",
        "neogeo",
        "neogeocd",
        "nes",
        "nesh",
        "ngp",
        "ngpc",
        "odyssey2",
        "pc",
        "pcengine",
        "pcenginecd",
        "pcfx",
        "pico",
        "ports",
        "ps1",
        "ps2",
        "ps3",
        "psp",
        "saturn",
        "Scumm",
        "scummvm",
        "sega32x",
        "segacd",
        "sfc",
        "sg-1000",
        "sgfx",
        "sms",
        "snes",
        "snesh",
        "tg16",
        "tg16cd",
        "ti99",
        "vectrex",
        "vg5000",
        "videopac",
        "virtualboy",
        "vita",
        "wii",
        "wiiu",
        "wiiware",
        "wonderswan",
        "wonderswancolor",
        "xbox",
        "Zinc",
        "zmachine",
        "zxspectrum"]
    return platforms

def getFolderFromCore(core: str) -> str:
    core_dict = {
        "Sega - MS/GG/MD/CD": "segacd",
        "Sega - MS": "megadrive",
        "Sega - Mega Drive - Genesis": "genesis",
        "Sega - Master System - Mark III": "mastersystem",
        "Sega - Game Gear": "gamegear",
        "Sega - SG-1000": "sg1000",
        "Sega - Mega-CD - Sega CD": "segacd",
        "Sega - 32X": "32x",
        "Sony - PlayStation": "psx",
        "Sony - PlayStation 2": "ps2",
        "Sega - Dreamcast/Naomi": "dreamcast",
        "Microsoft - Xbox": "xbox",
        "Nintendo - Game Boy": "gb",
        "Nintendo - Game Boy Color": "gbc",
        "Nintendo - Game Boy Advance": "gba",
        "Nintendo - Virtual Boy": "virtualboy",
        "Nintendo - Nintendo Entertainment System": "nes",
        "Nintendo - SNES": "snes",
        "Nintendo - Super Nintendo Entertainment System": "snes",
        "Nintendo - Nintendo 64": "n64",
        "Atari - 2600": "atari2600",
        "Atari - 5200": "atari5200",
        "Atari - 7800": "atari7800",
        "Atari - Lynx": "atarilynx",
        "NEC - PC Engine - TurboGrafx 16": "pcengine",
        "NEC - PC Engine CD - TurboGrafx-CD": "pcenginecd",
        "Coleco - ColecoVision": "coleco",
        "Intellivision": "intellivision"
        # Add more cores and their corresponding folders here
    }

    return core_dict.get(core, "")

def getCoreFromSlug(folder: str) -> str:
    core_mapping = {
        "3do" : "3DO Interactive Multiplayer",
        "actionmax" : "",
        "amiga" : "Amiga",
        "amigacd32" : "Amiga CD32",
        "amstradcpc" : "Amstrad CPC",
        "arcade" : "Arcade",
        "arcade_chd" : "Arcade",
        "apple2" : "Apple II",
        "astrocade" : "Bally Astrocade",
        "atari2600" : "Atari 2600",
        "atari5200" : "Atari 5200",
        "atari7800" : "Atari 7800",
        "atari800" : "Atari 8-bit",
        "atarijaguar" : "Atari Jaguar",
        "atarijaguarcd" : "Atari Jaguar CD",
        "atarilynx" : "Atari Lynx",
        "atarist" : "Atari ST/STE",
        "c64" : "Commodore C64/128/MAX",
        "cdi" : "Philips CD-i",
        "channelf" : "Fairchild Channel F",
        "coleco" : "ColecoVision",
        "creativision" : "",
        "crvision" : "",
        "daphne" : "Arcade",
        "dos" : "DOS",
        "dreamcast" : "Dreamcast",
        "famicom" : "Family Computer Disk System",
        "fairchild" : "Fairchild Channel F",
        "fba" : "Arcade",
        "fds" : "",
        "fmtowns" : "FMTowns",
        "gameandwatch" : "Game & Watch",
        "gamecube" : "Nintendo GameCube",
        "gamegear" : "Sega Game Gear",
        "gb" : "Game Boy",
        "gba" : "Game Boy Advance",
        "gbah" : "Game Boy Advance",
        "gbc" : "Game Boy Color",
        "gbh" : "Game Boy",
        "genh" : "Sega Mega Drive/Genesis",
        "ggh" : "",
        "intellivision" : "Intellivision",
        "jaguar" : "Atari Jaguar",
        "genesis" : "Genesis",
        "megadrive" : "Mega Drive",
        "megadrive-japan" : "Sega Mega Drive",
        "model123" : "Arcade",
        "msdos" : "DOS",
        "msx" : "MSX",
        "msx2" : "MSX2",
        "nds" : "Nintendo DS",
        "n3ds" : "Nintendo 3DS",
        "n64" : "Nintendo 64",
        "naomi" : "Arcade",
        "neogeo" : "Neo Geo AES",
        "neogeocd" : "Neo Geo CD",
        "nes" : "NES",
        "nesh" : "",
        "ngp" : "Neo Geo Pocket",
        "ngpc" : "Neo Geo Pocket Color",
        "nswitch" : "Nintendo Switch",
        "odyssey2" : "",
        "pc" : "DOS",
        "pce" : "PC Engine",
        "pcecd" : "PC Engine CD",
        "pcengine" : "PC Engine",
        "pcenginecd" : "PC Engine CD",
        "pcfx" : "PC-FX",
        "pico" : "Sega Pico",
        "ports" : "",
        "ps1" : "PlayStation",
        "ps2" : "PlayStation 2",
        "ps3" : "PlayStation 3",
        "ps4" : "PlayStation 4",
        "ps5" : "PlayStation 5",
        "psp" : "PlayStation Portable",
        "vita" : "PlayStation Vita",
        "saturn" : "Sega Saturn",
        "Scumm" : "DOS",
        "scummvm" : "DOS",
        "sega32x" : "Sega 32X",
        "segacd" : "Sega CD",
        "segapico" : "Sega Pico",
        "sfc" : "Super Famicom",
        "sg-1000" : "SG-1000",
        "sgfx" : "PC Engine SuperGrafx",
        "sms" : "Sega Master System/Mark III",
        "snes" : "Super NES",
        "snesh" : "Super NES",
        "tg16" : "TurboGrafx-16",
        "tg16cd" : "Turbografx-16 CD",
        "ti99" : "Texas Instruments TI-99",
        "vectrex" : "Vectrex",
        "vg5000" : "",
        "videopac" : "",
        "virtualboy" : "Virtual Boy",
        "wii" : "Wii",
        "wiiu" : "Wii U",
        "wiiware" : "",
        "wonderswan" : "WonderSwan",
        "wonderswancolor" : "WonderSwan Color",
    }
    
    return core_mapping.get(folder, "")

# this should be the default for non-ISO based games.
def getPlatformFromExtension(ext: str) -> str:
    platform_dict = {
        ".iso": "unknown",
        ".cso": "unknown",
        ".img": "unknown",
        ".mdf": "unknown",
        ".cue": "unknown",
        ".ccd": "unknown",
        ".nrg": "unknown",
        ".pbp": "unknown",
        ".chd": "unknown",
        ".zip": "unknown",
        ".gb": "gb",
        ".gbc": "gbc",
        ".gba": "gba",
        ".nes": "nes",
        ".snes": "snes",
        ".smc": "snes",
        ".n64": "n64",
        ".gg": "gamegear",
        ".sms": "mastersystem",
        ".bin": "genesis",
        ".gen": "genesis",
        ".md": "genesis",
        ".smd": "genesis",
        ".32x": "32x",
        ".pce": "pce",
        ".sgx": "pce",
        ".ngc": "ngc",
        ".2600": "atari2600",
        ".5200": "atari5200",
        ".7800": "atari7800",
        ".lynx": "atarilynx",
        ".jag": "atarijaguar"
        # Add more extensions and their corresponding platforms here
    }

    return platform_dict.get(ext.lower(), "unknown")