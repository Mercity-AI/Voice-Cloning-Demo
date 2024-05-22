from transformers import AutoProcessor, BarkModel

import scipy

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")


def generate_audio (text, preset, output):
  inputs = processor(text, voice_preset=preset)
  audio_array = model.generate(**inputs)
  audio_array = audio_array.cpu().numpy ().squeeze()
  sample_rate = model.generation_config.sample_rate
  scipy.io.wavfile.write(output, rate=sample_rate, data=audio_array)

generate_audio(
text="hi, welcome to my youtube channel",
preset="v2/en_speaker_9" ,
output="output.wav" ,)