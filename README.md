# Dynamic Text-to-Speech Cloning

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
   git clone https://github.com/yourusername/dynamic-text-to-speech-cloning.git
   cd dynamic-text-to-speech-cloning
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

This application uses the Bark TTS model to convert text to speech. The model is initialized and loaded with a pre-trained checkpoint. Users can upload an audio file to clone the voice. The uploaded file is saved temporarily, and the text input is processed to generate speech using the cloned voice. The generated speech is saved as a WAV file, which users can play back or download.

The Streamlit interface includes file upload, text input, and buttons to generate and download speech. The application also handles the temporary storage of audio files and cleans up after the download.

## Diagram

![Diagram](diagram.png)

## Screenshot

![Screenshot](screenshot.png)

## Voice Samples

- [Sample 1](samples/sample1.wav)
- [Sample 2](samples/sample2.wav)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

To run this app, save it to a file (e.g., `app.py`) and run `streamlit run app.py` in your terminal.

### Diagram and Screenshot

Please add the diagram image (diagram.png) and screenshot image (screenshot.png) in the repository directory where the README is located. Additionally, ensure that the voice samples (sample1.wav and sample2.wav) are added to the 'samples' directory.

This README provides a comprehensive overview of the project, including setup instructions, usage guidelines, and additional resources. For any questions or further assistance, feel free to contact us or open an issue on GitHub.
