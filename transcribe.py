import os
from pocketsphinx import AudioFile

print(os.getcwd()+"/audio")
for file in os.listdir(os.getcwd()+"/audio"):
	if file.endswith("wav"):
		print(file)
		for phrase in AudioFile(audio_file=(os.getcwd()+"/audio/"+file)):
			print(phrase) # => "go forward ten meters"
			print(type(phrase))
		exit(1)