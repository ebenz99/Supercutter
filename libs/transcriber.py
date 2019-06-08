import os
from pocketsphinx import AudioFile
from pprint import pprint

def transcribe(myword):
	occurences = []
	fps = 100
	stre = ""
	print(os.getcwd()+"/audios")
	for file in os.listdir(os.getcwd()+"/audios"):
		if file.endswith("wav"):
			print(file)
			for phrase in AudioFile(audio_file=(os.getcwd()+"/audios/"+file),full_utt=False):
				for s in phrase.seg():
					#if '<' not in s.word:
					print('| %4ss | %4ss | %8s |' % (s.start_frame/fps, s.end_frame/fps, s.word))
					if myword in s.word:
						occ = [s.start_frame/fps, s.end_frame/fps]
						occurences.append(occ)
			break
	return occurences


print(transcribe("your"))