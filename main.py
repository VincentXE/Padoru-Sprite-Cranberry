import ctypes
import os
import winsound
import subprocess
#drive = "C:\\"
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "lib/image.png", 3)
while True:
	winsound.PlaySound('lib/padoru.wav', winsound.SND_FILENAME)
