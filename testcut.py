import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
counter = 1
ffmpeg_extract_subclip((os.getcwd()+"/videos/Jake and Amir - Chugging.mp4"), 5, 10, targetname=(str(counter)+"cut.mp4"))