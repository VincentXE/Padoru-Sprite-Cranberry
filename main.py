import ctypes, os, winsound, subprocess
ctypes.windll.user32.SystemParametersInfoA(20, 0, "lib/image.png", 0)
p = subprocess.Popen(["lib\\res.exe",
				'/x:800',
				'/y:600'])
p.communicate()
while True:
	winsound.PlaySound('lib\\padoru.wav', winsound.SND_FILENAME)
	os.startfile('lib\\pandoru.png')
	os.startfile('lib\\image.png')
	os.startfile('lib\\spritecranberry.png')
	os.startfile('notepad.exe')

