import ctypes
import os
import winsound
import subprocess
#drive = "C:\\"
folder = "lib"
image = "image.png"
image_path = os.path.join(folder, image)
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
while True:
	winsound.PlaySound('lib/padoru.wav', winsound.SND_FILENAME)
