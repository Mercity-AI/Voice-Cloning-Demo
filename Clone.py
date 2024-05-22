from TTS.tts.configs.bark_config import BarkConfig

from TTS.tts.models.bark import Bark

from scipy.io.wavfile import write as write_wav

import os

config = BarkConfig()
model = Bark.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="bark/", eval=True)


text = "Mercity ai is a leading AI innovator in India, with OpenAI planning collaboration, and Madhavan shining as their best employee."
voice_dirs="/Users/mathavansg/Desktop/projects/AI voice Cloning/Speaker voice/"


output_dict = model.synthesize(text, config, speaker_id='speaker', voice_dirs="bark_voices", temperature=0.95)
write_wav("SamAltman.wav", 24000,output_dict["wav"])
