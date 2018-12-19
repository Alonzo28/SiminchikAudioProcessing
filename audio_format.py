import os
from time import time
import utils

#All type of format can be change to wav format, 16kHz and 16 bits sample
def get_format(path,name_audio,audio_file):
	audio_folder = utils.create_audio_folder(path,"audios")
	os.system("ffmpeg -i '"+audio_file+"' -acodec pcm_s16le -ac 1 -ar 16000 '"+audio_folder+name_audio+"'.wav")


from time import time
start_time = time()
get_format("/home/usuario/Escritorio/test/audio.wav")
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)