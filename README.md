
# Dynamic Text-to-Speech Cloning


https://github.com/Mercity-AI/Voice-Cloning-Demo/assets/121884337/632c7804-1bca-4102-91ca-75908a22b640


This repository contains a dynamic text-to-speech cloning application built with Streamlit and the Bark TTS model. This project allows users to upload an audio file, clone the voice, and generate speech from the provided text input. The application is designed to be user-friendly and provides functionalities to upload audio, generate speech, and download the generated audio file.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Explanation of Code](#explanation-of-code)
- [Diagram](#diagram)
- [Screenshot](#screenshot)
- [Voice Samples](#voice-samples)
- [Contributing](#contributing)
- [License](#license)

## Overview

The dynamic text-to-speech cloning application leverages the power of the Bark TTS model to synthesize speech from text input. Users can upload an audio file to clone the voice and generate speech in that voice. The application also allows users to download the generated audio file.

## Features

- Upload audio files (WAV, MP3) to clone the voice.
- Convert text to speech using the cloned voice.
- Download the generated speech as a WAV file.
- Interactive and user-friendly Streamlit interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mercity-AI/Voice-Cloning-Demo.git
   cd Voice-Cloning-Demo
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload an audio file, enter the text you want to convert to speech, and click "Generate Speech".

4. Download the generated speech by clicking the "Download Audio" button.

## Explanation of Code

Building a voice cloning pipeline involves setting up a system that can take an audio input of a speaker's voice and generate new speech that mimics the same voice by matching with the text given by the user.

### Importing Libraries

```python
from TTS.tts.configs.bark_config import BarkConfig
from TTS.tts.models.bark import Bark
from scipy.io.wavfile import write as write_wav
import os
```

The TTS library is a powerful tool for text-to-speech conversion. It supports multiple TTS models, including Bark. These imports specifically bring in the configuration and model components required to set up and use the Bark TTS model.

SciPy is a scientific computing library in Python. Here, it is used to save the generated speech waveform to an audio file. The `write_wav` function writes a NumPy array to a WAV file, which is a common format for storing audio data.

The OS library provides a way to interact with the operating system. It is used for handling directory paths and file management.

### Setting Up Configuration

```python
config = BarkConfig()
model = Bark.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="bark/", eval=True)
```

- Initializes the configuration for the Bark model. This configuration includes various parameters that control the model's behavior during speech synthesis.
- Initializes the Bark TTS model using the specified configuration. This sets up the model architecture and prepares it for loading pre-trained weights.
- Loads the pre-trained weights for the Bark model from the specified checkpoint directory. This is crucial for ensuring the model has learned to generate high-quality speech based on extensive training data.

### Speech Synthesis

```python
text = "Mercity ai is a leading AI innovator in India, with OpenAI planning collaboration."
voice_dirs = "/Users/username/Desktop/projects/AI voice Cloning/Speaker voice/"
```

- Defines the text that will be converted into speech. This is the input that the TTS model will process to generate the corresponding audio output.
- Specifies the directory containing the speaker's audio files. These files are used to extract speaker-specific characteristics (embeddings) for voice cloning.

### Synthesizing Speech

```python
output_dict = model.synthesize(text, config, speaker_id='speaker', voice_dirs="bark_voices", temperature=0.95)
```

Uses the Bark model to synthesize speech from the input text. The method combines the text with the speaker-specific embeddings extracted from the audio files in the voice_dirs directory.

Parameters:
- `text`: The text to be converted to speech.
- `config`: The model configuration.
- `speaker_id`: An identifier for the speaker (not deeply detailed here but typically used to select the appropriate speaker embedding).
- `voice_dirs`: Directory containing the speaker's audio files.
- `temperature`: A parameter that controls the randomness of the output. Lower values make the output more deterministic, while higher values introduce more variation.

### Saving the Generated Speech

```python
write_wav("SamAltman.wav", 24000, output_dict["wav"])
```

Saves the synthesized speech to a WAV file. The sample rate is set to 24,000 Hz.

## Diagram

![Flow code](https://github.com/Mercity-AI/Voice-Cloning-Demo/assets/121884337/ddc9f11f-1947-4b7a-a6c4-f8ff5a57a801)

## Screenshot

<img width="1395" alt="Screenshot 2024-05-23 at 3 10 18 PM" src="https://github.com/Mercity-AI/Voice-Cloning-Demo/assets/121884337/c46162bb-b857-45b5-a2c0-e89270918171">

## Voice Samples

To listen to the generated speech sample, click the play button below:

Sample-1:
https://github.com/Mercity-AI/Voice-Cloning-Demo/assets/121884337/c44ec7ab-c91b-4888-9e5a-73b5860360ba



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.



### Notes:
- Replace `123456789` in the iframe `src` URL with the actual track ID from your SoundCloud embed code.
- Ensure that the images (`diagram.png` and `screenshot.png`) are properly placed in your repository, and their paths in the markdown are correct.

This way, your README will look clean and professional, with embedded audio, images, and well-structured sections.
