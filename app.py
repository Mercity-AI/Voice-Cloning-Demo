import streamlit as st
from TTS.tts.configs.bark_config import BarkConfig
from TTS.tts.models.bark import Bark
from scipy.io.wavfile import write as write_wav
import numpy as np
import os
import shutil
# Initialize TTS model
config = BarkConfig()
model = Bark.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="bark/", eval=True)

st.title("Dynamic Text-to-Speech Cloning")
st.write("Upload an audio file to clone the voice and enter the text you want to convert to speech:")

# Ensure the temporary directory and speaker subdirectory exist
os.makedirs("temp_audio/speaker", exist_ok=True)

# File uploader for the audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary location within the speaker directory
    temp_audio_path = os.path.join("temp_audio/speaker", uploaded_file.name)
    with open(temp_audio_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Uploaded {uploaded_file.name} successfully!")

    # Input text from the user
    text = st.text_area("Text input", "Enter your text here...")

    if st.button("Generate Speech"):
        with st.spinner("Generating speech..."):
            output_dict = model.synthesize(text, config, speaker_id='speaker', voice_dirs="temp_audio", temperature=0.95)
            audio_path = "Output.wav"
            write_wav(audio_path, 24000, output_dict["wav"])
            
            st.audio(audio_path, format="audio/wav")
            st.success("Speech generated successfully!")

            #Provide a download link for the generated audio file
            with open(audio_path, "rb") as file:
                btn = st.download_button(
                    label="Download Audio",
                    data=file,
                    file_name="output.wav",
                    mime="audio/wav"
                )
             # Clear temporary files after download button is shown
            if btn:
                os.remove(audio_path)
                shutil.rmtree("temp_audio/speaker")
                os.makedirs("temp_audio/speaker")
else:
    st.warning("Please upload an audio file to clone the voice.")

# To run this app, save it to a file (e.g., app.py) and run `streamlit run app.py` in your terminal.
