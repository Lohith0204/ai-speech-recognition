import streamlit as st
import tempfile
from ai_engine.model import transcribe_audio, summarize_text

st.title("AI Video / Audio Summarizer")

uploaded_file = st.file_uploader(
    "Upload an audio file extracted from video",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file is not None:
    st.audio(uploaded_file)

    if st.button("Generate Summary"):
        with st.spinner("Processing..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
                temp_audio.write(uploaded_file.read())
                temp_audio_path = temp_audio.name

            transcription = transcribe_audio(temp_audio_path)
            summary = summarize_text(transcription)

        st.success("Summary generated")
        st.subheader("Summary")
        st.write(summary)
