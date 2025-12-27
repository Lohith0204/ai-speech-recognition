import streamlit as st
import tempfile
from ai_engine.model import transcribe_audio

st.title("AI Speech Recognition")

audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if audio_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
        temp_audio.write(audio_file.read())
        text = transcribe_audio(temp_audio.name)

    st.subheader("Transcribed Text")
    st.write(text)
