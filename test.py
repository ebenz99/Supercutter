from pocketsphinx import AudioFile
import os
import downloader


eplist = downloader.dlar("https://www.youtube.com/playlist?list=PLYn4JCLV09Lu94-GL8GdMDNUdpGopPlR9")


#for phrase in AudioFile(audio_file="file-16000.wav"):
#	print(phrase) # => "go forward ten meters"