# this should be the fallback for ISO based games.
from distutils import core
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
        "dreamcast" : "Dreamcast",        
        "segacd": "Sega CD",
        "megadrive": "Genesis",
        "mastersystem": "Master System",
        "gamegear": "Game Gear",
        "sg1000": "SG-1000",
        "32x": "32X",
        "psx": "PlayStation",
        "ps2": "PlayStation 2",
        "xbox": "OG Xbox",
        "gb": "Game Boy",
        "gbc": "Game Boy Color",
        "gba": "Game Boy Advance",
        "virtualboy": "Virtual Boy",
        "nes": "NES",
        "snes": "SNES",
        "n64": "Nintendo 64",
        "atari2600": "Atari 2600",
        "atari5200": "Atari 5200",
        "atari7800": "Atari 7800",
        "atarilynx": "Atari Lynx",
        "tg16": "TurboGrafx 16",
        "tgcd": "TurboGrafx-CD",
        "pce": "TurboGrafx 16",
        "pcengine": "PC Engine",
        "pcenginecd": "PC Engine CD ",
        "coleco": "ColecoVision",
        "intellivision": "Intellivision",
    }
    
    return core_mapping.get(folder, "")

# this should be the default for non-ISO based games.
def getPlatformFromExtension(ext: str) -> str:
    platform_dict = {
        ".iso": "unknown",
        ".cso": "unknown",
        ".bin": "unknown",
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

    return platform_dict.get(ext, "unknown")
    
def getIgdbIdFromSlug(core: str) -> str:
    platforms = {
    "3do" : "50",# 3DO Interactive Multiplayer
    "actionmax" : "9999",#
    "amiga" : "16",# Amiga
    "amigacd32" : "114",# Amiga CD32
    "amstradcpc" : "25",# Amstrad CPC
    "arcade" : "52",# Arcade
    "arcade_chd" : "52",# Arcade
    "apple2" : "75",# Apple II
    "astrocade" : "91",# Bally Astrocade
    "atari2600" : "59",# Atari 2600
    "atari5200" : "66",# Atari 5200
    "atari7800" : "60",# Atari 7800
    "atari800" : "65",# Atari 8-bit
    "atarijaguar" : "62",# Atari Jaguar
    "atarijaguarcd" : "410",# Atari Jaguar CD
    "atarilynx" : "61",# Atari Lynx
    "atarist" : "63",# Atari ST/STE
    "c64" : "15",# Commodore C64/128/MAX
    "cdi" : "117",# Philips CD-i
    "channelf" : "127",# Fairchild Channel F
    "coleco" : "68",# ColecoVision
    "creativision" : "",#
    "crvision" : "",#
    "daphne" : "52",# Arcade
    "dos" : "13",# DOS
    "dreamcast" : "23",# Dreamcast
    "famicom" : "51",# Family Computer Disk System
    "fairchild" : "127",# Fairchild Channel F
    "fba" : "52",# Arcade
    "fds" : "",#
    "fmtowns" : "118",# FMTowns
    "gameandwatch" : "307",# Game & Watch
    "gamecube" : "21",# Nintendo GameCube
    "gamegear" : "35",# Sega Game Gear
    "gb" : "33",# Game Boy
    "gba" : "24",# Game Boy Advance
    "gbah" : "24",# Game Boy Advance
    "gbc" : "22",# Game Boy Color
    "gbh" : "33",# Game Boy
    "genh" : "29",# Sega Mega Drive/Genesis
    "ggh" : "",#
    "intellivision" : "67",# Intellivision
    "jaguar" : "62",# Atari Jaguar
    "genesis" : "29",# Sega Mega Drive/Genesis
    "megadrive" : "29",# Sega Mega Drive/Genesis
    "megadrive-japan" : "29",# Sega Mega Drive/Genesis
    "model123" : "52",# Arcade
    "msdos" : "13",# DOS
    "msx" : "27",# MSX
    "msx2" : "53",# MSX2
    "nds" : "20",# Nintendo DS
    "n3ds" : "37",# Nintendo 3DS
    "n64" : "4",# Nintendo 64
    "naomi" : "52",# Arcade
    "neogeo" : "80",# Neo Geo AES
    "neogeocd" : "136",# Neo Geo CD
    "nes" : "18",# Nintendo Entertainment System
    "nesh" : "",#
    "ngp" : "119",# Neo Geo Pocket
    "ngpc" : "120",# Neo Geo Pocket Color
    "nswitch" : "130",# Nintendo Switch
    "odyssey2" : "",#
    "pc" : "13",# DOS
    "pcengine" : "86",# TurboGrafx-16/PC Engine
    "pcenginecd" : "150",# Turbografx-16/PC Engine CD
    "pcfx" : "274",# PC-FX
    "pico" : "",#
    "ports" : "",#
    "ps1" : "7",# PlayStation
    "ps2" : "8",# PlayStation 2
    "ps3" : "9",# PlayStation 3
    "ps4" : "48",# PlayStation 4
    "ps5" : "167",# PlayStation 5
    "psp" : "38",# PlayStation Portable
    "vita" : "46",# PlayStation Vita
    "saturn" : "32",# Sega Saturn
    "Scumm" : "13",# DOS
    "scummvm" : "13",# DOS
    "sega32x" : "30",# Sega 32X
    "segacd" : "78",# Sega CD
    "segapico" : "339",# Sega Pico
    "sfc" : "58",# Super Famicom
    "sg-1000" : "84",# SG-1000
    "sgfx" : "128",# PC Engine SuperGrafx
    "sms" : "64",# Sega Master System/Mark III
    "snes" : "19",# Super Nintendo Entertainment System
    "snesh" : "19",# Super Nintendo Entertainment System
    "tg16" : "86",# TurboGrafx-16/PC Engine
    "tg16cd" : "150",# Turbografx-16/PC Engine CD
    "ti99" : "129",# Texas Instruments TI-99
    "vectrex" : "70",# Vectrex
    "vg5000" : "",#
    "videopac" : "",#
    "virtualboy" : "87",# Virtual Boy
    "wii" : "5",# Wii
    "wiiu" : "41",# Wii U
    "wiiware" : "",#
    "wonderswan" : "57",# WonderSwan
    "wonderswancolor" : "123",# WonderSwan Color
    "x68000" : "121",# Sharp X68000
    "xbox" : "11",# Xbox
    "Zinc" : "",#
    "zmachine" : "",#
    "zxspectrum" : "26",# ZX Spectrum
    }
    return platforms.get(core, "")