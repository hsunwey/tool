#!/usr/bin/python

import os
import sys
import speech_recognition as sr
import moviepy.editor as mp

def main(argv):
	filename = argv
	outputfile = filename.split('.')[0] + '.txt'

	mp4_wav(filename)
	result = speech_recognition()
	export_txt(result, outputfile)

	print(result)
	# delete_wav()


def mp4_wav(filename):
	clip = mp.VideoFileClip(filename)
	clip.audio.write_audiofile(r"converted.wav")
	return

def speech_recognition():
	r = sr.Recognizer()
	audio = sr.AudioFile("converted.wav")

	with audio as source:
			audio_file = r.record(source)

	
	result = r.recognize_google(audio_file)
	return result

def delete_wav():
	os.remove("converted.wav")
	return

def export_txt(result, outputfile):
	with open(outputfile, mode ='w') as file: 
		file.write(result) 
		print("ready!")
	return


if __name__ == "__main__":
	main(sys.argv[1])



# documentation for recognizer_instance.recognize_sphinx, recognizer_instance.recognize_google, recognizer_instance.recognize_wit, recognizer_instance.recognize_bing, recognizer_instance.recognize_api, recognizer_instance.recognize_houndify, and recognizer_instance.recognize_ibm.

# ffmpeg -i 112341.mp4 -ss 00:06:00 -t 00:10:00 -c copy split.mp4
