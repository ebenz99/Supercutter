import os
from shutil import copyfile, rmtree

def stitch():
	arr = os.listdir(os.getcwd()+"/clips")
	varr = [(os.getcwd()+"/clips/"+vid) for vid in arr if vid.endswith("mp4")]
	print("\n\n\n\n\n\n")
	print(varr)
	print("\n\n\n\n\n\n")
	if len(varr) == 0:
		print("NO CLIPS - EXITING")
		exit(2)
	elif len(varr) == 1:
		copyfile((os.getcwd()+"/clips/"+varr[0]),os.getcwd()+"/video/finalcut.mp4")
	else:
		os.system("./ccat.sh")

def clean():
	mydir = os.getcwd()
	subdirs = ["/audios","/videos","/clips"]
	for subdir in subdirs:
		for file in os.listdir((mydir+subdir)):
			if file.endswith("mp4") or file.endswith("wav"):
				os.remove((mydir+subdir+"/"+file))
	rmtree((mydir+"/libs/__pycache__/"),ignore_errors=True)

