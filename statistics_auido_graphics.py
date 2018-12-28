import matplotlib.pyplot as plt
import os 
import contextlib 
import scipy.io.wavfile as waves
import numpy
from scipy.io.wavfile import read as wavread
from wave import Wave_read
import wave

path=os.getcwd()+'/Audios_test'


def grafica(first_format,second_format,wav,others):
	fig = plt.figure(u'Grafica de barras') # Figure
	ax = fig.add_subplot(111) # Axes
	nombres = [first_format,second_format]
	datos = [wav,others]
	xx = range(len(datos))
	ax.bar(xx, datos)
	ax.set_xticks(xx)
	ax.set_xticklabels(nombres)
	plt.show()

def format(path,wav=0,others=0):
	matriz= []
	for file in os.listdir(path):
		name_file=file.split('.')
		if(name_file[1]=='wav'):
			first_format=name_file[1]
			wav+=1
		else:
			others+=1
	grafica(first_format,"others",wav,others)

format(path)

def frequency(path,count_rate=0, count_rates=0):
	for filename in os.listdir(path):
		with contextlib.closing(wave.open(path+'/'+filename,'r')) as f:
		    rate = f.getframerate()
		    if(rate==16000):
		    	count_rate+=1
		    else:
		    	count_rates+=1
	grafica(rate,"others",count_rate,count_rates)

frequency(path)

def duration(path,d=0,others=0):
	for filename in os.listdir(path):
		with contextlib.closing(wave.open(path+'/'+filename,'r')) as f: 
			frames=f.getnframes()
			rate=f.getframerate()
			duration=frames/rate
			if duration==30:
				time_d=duration
				d+=1
			else:
				others+=1
	grafica(time_d,"others",d,others)
duration(path)

def byte(path,b_s=0,b_n=0):
	for filename in os.listdir(path):
		[samplerate, x] = wavread(path+'/'+filename)
		if x.dtype == 'int16':
    			b_s+=1
		else:
			b_n+=1
	grafica("16 bytes","32 bytes", b_s,b_n )
byte(path)

def channel(path,mono=0,stereo=0):
	for filename in os.listdir(path):
		y=wave.open(path+'/'+filename)
		canal=Wave_read.getnchannels(y)
		if(canal==1):
			mono+=1
		else:
			stereo+=1
	grafica("mono","stereo",mono,stereo)
channel(path)