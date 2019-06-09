import os
from shutil import copyfile

def stitch():
	arr = os.listdir(os.getcwd()+"/clips")
	varr = [(os.getcwd()+"/clips/"+vid) for vid in arr if vid.endswith("mp4")]

	if len(varr) == 0:
		print("NO CLIPS - EXITING")
		exit(2)
	elif len(varr) == 1:
		copyfile((os.getcwd()+"/clips/"+varr[0]),os.getcwd()+"/video/finalcut.mp4")
	else:
		os.system(("mp4box -cat " + varr[0] + " -cat " + varr[1] + " -new video/fcut.mp4"))
		for i in range(2,len(varr)):
			os.system(("mp4box -cat " + varr[i] + " -cat video/fcut.mp4 -new video/fcut.mp4"))

def clean():
	mydir = os.getcwd()
	subdirs = ["/audios","/videos","/clips"]
	for subdir in subdirs:
		for file in os.listdir((mydir+subdir)):
			if file.endswith("mp4") or file.endswith("wav"):
				os.remove((mydir+subdir+"/"+file))
