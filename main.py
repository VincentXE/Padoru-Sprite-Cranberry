import ctypes, os, winsound
ctypes.windll.user32.SystemParametersInfoA(20, 0, "lib/image.png", 0)
while True:
	#winsound.PlaySound('lib\padoru.wav', winsound.SND_FILENAME)
	#winsound.PlaySound('lib\spritecranberry.wav', winsound.SND_FILENAME)
	os.startfile('lib\\pandoru.png')
	os.startfile('lib\\image.png')
	os.startfile('lib\\spritecranberry.png')
	os.startfile('notepad.exe')

