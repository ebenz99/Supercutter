import os
import time
from shutil import copyfile
import cv2

def dlar(url):
	l = []
	os.chdir(os.getcwd()+"/audios")
	os.system('youtube-dl --extract-audio --audio-format wav -o "%(title)s.%(ext)s" ' + url)
	os.system("ls")
	time.sleep(10)
	for file in os.listdir(os.getcwd()):
		if file.endswith("wav"):
			l.append(file)
	for file in l:
		print(file)
		print("ffmpeg -i \""+ file + "\" -ac 1 \"" + str(file.split(".")[0]) + "m.wav\"")
		os.system("ffmpeg -i \""+ file + "\" -ac 1 \"" + str(file.split(".")[0]) + "m.wav\"")
		#copyfile((str(file.split(".")[0]) + "m.wav"), file)
		try:
			os.remove(file)
		except FileNotFoundError:
			pass
		print("sox \""+ str(file.split(".")[0]) + "m.wav\" -r 16000 \"" + file + "\"")
		os.system("sox \""+ str(file.split(".")[0]) + "m.wav\" -r 16000 \"" + file + "\"")
		try:
			os.remove((str(file.split(".")[0]) + "m.wav"))
		except FileNotFoundError:
			pass
		print("\n\n\n")
	os.chdir("..")
	return l

def dlvr(url):
	l = []
	os.chdir(os.getcwd()+"/videos")
	os.system("youtube-dl -i -f mp4 --yes-playlist -o '%(title)s.%(ext)s' " + url)
	os.system("ls")
	time.sleep(10)
	for file in os.listdir(os.getcwd()):
		if file.endswith("mp4"):
			l.append(file)
			vid = cv2.VideoCapture(file)
			height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
			width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
			print(height, width, "\n\n\n")
			if width != 1280 or height != 720:
				os.system(("ffmpeg -i \"" + file + "\" -vf scale=1280:720 \"" + file.split(".")[0]+"c.mp4\""))
				os.remove(file)
				os.listdir(os.getcwd())
				copyfile(file.split(".")[0]+"c.mp4", file)
				os.remove(file.split(".")[0]+"c.mp4")
		if file.endswith("wav"):
			try:
				os.remove(file)
			except FileNotFoundError:
				pass
	for file in l:
		print(file)
	os.chdir("..")
	return l

#dlar("https://www.youtube.com/playlist?list=PLYn4JCLV09Lu94-GL8GdMDNUdpGopPlR9")
#dlvr("https://www.youtube.com/playlist?list=PLYn4JCLV09Lu94-GL8GdMDNUdpGopPlR9")
