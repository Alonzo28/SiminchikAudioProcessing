# -*- coding: utf-8 -*- 

import os
import numpy as np
import random
import shutil
import librosa


# Create a copy file with noise
def load_audio_file(path,audio_file,name_audio):
    y, sr = librosa.load(audio_file)
    data_wn = create_noise(y)
    librosa.output.write_wav(path+name_audio+"_noise", data_wn, sr)

# Add noise to the audios
def create_noise(data):
	wn = np.random.randn(len(data))
	data_wn = data + 0.01 * wn
	return data_wn

# Create a copy of txt file
def create_transcription(path,name_txt):
    shutil.copy(path+name_txt+".txt",path+name_txt+"_noise.txt")



