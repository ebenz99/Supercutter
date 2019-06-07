import os
import time

def dlar(url):
	l = []
	os.chdir(os.getcwd()+"/audio")
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
		os.remove(file)
		print("sox \""+ str(file.split(".")[0]) + "m.wav\" -r 16000 \"" + file + "\"")
		os.system("sox \""+ str(file.split(".")[0]) + "m.wav\" -r 16000 \"" + file + "\"")
		os.remove((str(file.split(".")[0]) + "m.wav"))
		print("\n\n\n\n")
		os.system("ls")
		time.sleep(3)
		
	os.chdir("..")
	return l

dlar("https://www.youtube.com/playlist?list=PLYn4JCLV09Lu94-GL8GdMDNUdpGopPlR9")
