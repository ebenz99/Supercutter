import os
from pocketsphinx import AudioFile
from pprint import pprint


stre = ""
print(os.getcwd()+"/audio")
for file in os.listdir(os.getcwd()+"/audio"):
	if file.endswith("wav"):
		print(file)
		for phrase in AudioFile(audio_file=(os.getcwd()+"/audio/"+file)):
			stre+=str(phrase)
			print(stre)
		exit(1)