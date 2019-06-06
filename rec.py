import time
import os

def my_start_recording():
	import sys
	import os
	md = os.getcwd()
	td = md+"/libs"
	sys.path.insert(0, td)
	import recorder as rc
	import time
	import os
	import pyaudio

	rec = rc.Recorder(channels=1)
	recfile2 = rec.open(os.getcwd()+"/testaudio.wav")
	recfile2.start_recording()
	return recfile2

def my_stop_recording(robj):
	import sys
	import os
	md = os.getcwd()
	td = md+"/libs"
	sys.path.insert(0, td)
	import recorder as rc
	robj.stop_recording()
	robj.close()
	print("I've succeeded")

a = my_start_recording()
time.sleep(10)
my_stop_recording(a)
os.system("sox testaudio.wav -r 16000 file-16000.wav")
