from pocketsphinx import AudioFile
for phrase in AudioFile(audio_file="file-16000.wav"):
	print(phrase) # => "go forward ten meters"