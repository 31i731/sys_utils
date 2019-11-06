import ctypes
from random import choice as rnd_choice
from os import listdir

def changeWallpaper(toTakeFrom):
    rnd_file = rnd_choice([pic for pic in listdir(toTakeFrom) if (".jpg" or ".png") in pic])
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, toTakeFrom + rnd_file, 0)