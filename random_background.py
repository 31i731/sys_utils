from random import choice as rnd_choice
from os import listdir
import ctypes

img_path = "C:\\Users\\37255\\Pictures\\Saved Pictures\\"
current_file = None

def changeWallpaper():
    rnd_file = rnd_choice([pic for pic in listdir(img_path) if not "ini" in pic and not pic == current_file])
    global current_file
    current_file = rnd_file
    print(rnd_file)
    #SPI_SETDESKWALLPAPER = 20 
    #ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_path + rnd_file, 0)
