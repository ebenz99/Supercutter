import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import sys
import subprocess as sp

from moviepy.tools import subprocess_call
from moviepy.config import get_setting

def my_ffmpeg_extract_subclip(filename, t1, t2, targetname=None):
    """ makes a new video file playing video file ``filename`` between
        the times ``t1`` and ``t2``. """
    name,ext = os.path.splitext(filename)
    if not targetname:
        T1, T2 = [int(1000*t) for t in [t1, t2]]
        targetname = name+ "%sSUB%d_%d.%s"(name, T1, T2, ext)
    
    cmd = [get_setting("FFMPEG_BINARY"),"-y",
      "-ss", "%0.2f"%t1,
      "-i", filename,
      "-t", "%0.2f"%(t2-t1),
      targetname]
    
    subprocess_call(cmd)

def cut(dic):
	counter = 0
	for video in dic:
		for timestamp in dic[video]:
			#my_ffmpeg_extract_subclip((os.getcwd()+"/videos/Jake and Amir - Chugging.mp4"), 33.35-.5, 33.73+.5, targetname=("jc.mp4"))
			my_ffmpeg_extract_subclip((os.getcwd()+"/videos/"+video), timestamp[0]-.1, timestamp[1]+.2, targetname=(os.getcwd()+"/clips/"+str(counter)+"cut.mp4"))
			counter+=1
