import os
from pocketsphinx import AudioFile
from pprint import pprint

fps = 100
stre = ""
print(os.getcwd()+"/audio")
for file in os.listdir(os.getcwd()+"/audio"):
	if file.endswith("wav"):
		print(file)
		
		for phrase in AudioFile(audio_file=(os.getcwd()+"/audio/"+file),full_utt=False):
			stre+=str(phrase)+" "
			for s in phrase.seg():
				if '<' not in s.word:
					print('| %4ss | %4ss | %8s |' % (s.start_frame/fps, s.end_frame/fps, s.word))
			print(phrase)
		exit(1)

