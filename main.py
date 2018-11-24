import ctypes, os, winsound, win32con, PIL
from PIL import Image

Image = Image.open('lib\image.png')
#Image.show()
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "lib/image.bmp", 0)
#winsound.PlaySound('lib\spritecranberry.wav', winsound.SND_FILENAME)
while True:
	Image.show()
	winsound.PlaySound('lib\padoru.wav', winsound.SND_FILENAME)
	winsound.PlaySound('lib\spritecranberry.wav', winsound.SND_FILENAME)

