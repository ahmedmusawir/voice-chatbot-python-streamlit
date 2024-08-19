import streamlit as st
import os
from utils.record_audio import record_audio
from utils.transcribe_w_whisper import transcribe_audio
from utils.get_llm_response import (
    get_openai_llm_response,
    get_claude_llm_response,
    get_groq_llm_response,
    get_gemini_llm_response,
)
from utils.get_tts_response import generate_speech

# Parameters for recording
duration = 5  # Duration for the recording in seconds
fs = 48000  # Sample rate
device_index = 17  # Replace with your selected device index
audio_file_path = 'audio/question.wav'  # File path to save the recording
tts_audio_file_path = 'audio/answer.mp3'  # File path for the TTS audio

# Streamlit app layout
st.title("Voice Chatbot (Muli-Model)")

# Sidebar for model selection
st.sidebar.title("Choose a Model:")
model_choice = st.sidebar.radio(
    "Select the LLM model:",
    ("OpenAI GPT-4o", "Claude Sonnet 3.5", "Llama 3.1 70b", "Gemini Pro 1.5")
)

# Function to get the LLM response based on model choice
def get_llm_response(transcribed_text, model_choice):
    if model_choice == "OpenAI GPT-4o":
        return get_openai_llm_response(transcribed_text)
    elif model_choice == "Claude Sonnet 3.5":
        return get_claude_llm_response(transcribed_text)
    elif model_choice == "Llama 3.1 70b":
        return get_groq_llm_response(transcribed_text)
    elif model_choice == "Gemini Pro 1.5":
        return get_gemini_llm_response(transcribed_text)

# Placeholder for status messages and spinners
status_placeholder = st.empty()
transcription_placeholder = st.empty()
response_placeholder = st.empty()
tts_placeholder = st.empty()

# Check if process is running
process_running = st.session_state.get("process_running", False)

# "Ask Question" Button
if st.button("Ask Question", disabled=process_running):
    st.session_state.process_running = True
    
    # RECORDING AUDIO
    with st.spinner('Recording... Please wait.'):
        record_audio(audio_file_path, duration, fs, device_index)
    status_placeholder.text("Question generation complete...")
    
    # AUDIO TRANSCRIBER 
    if os.path.exists(audio_file_path):
        with st.spinner('Transcribing with Whisper... Please wait.'):
            transcription_text = transcribe_audio(audio_file_path)
            st.session_state.transcription_text = transcription_text
        transcription_placeholder.markdown(
            f'<div style="background-color:#e0f7fa;padding:10px;border-radius:5px;">'
            f'<strong>👤 You:</strong> {transcription_text}</div>',
            unsafe_allow_html=True
        )
    
    # GET LLM TEXT RESPONSE GENERATOR
    if "transcription_text" in st.session_state:
        with st.spinner(f'Getting LLM answer with {model_choice}... Please wait.'):
            llm_response = get_llm_response(st.session_state.transcription_text, model_choice)
            st.session_state.llm_response = llm_response
        response_placeholder.markdown(
            f'<div style="background-color:#ffe0e0;padding:10px;border-radius:5px;margin:1rem 0rem;">'
            f'<strong>🤖 AI:</strong> {llm_response}</div>',
            unsafe_allow_html=True
        )
    
    # TEXT LLM RESPONSE TO SPEECH
    if "llm_response" in st.session_state:
        with st.spinner('Converting LLM answer to speech with TTS-1... Please wait.'):
            generate_speech(st.session_state.llm_response, tts_audio_file_path)
        tts_placeholder.text("LLM Answer to speech by TTS-1 complete...")

        # Display the audio player (Auto-playing might not work due to browser restrictions)
        st.audio(tts_audio_file_path, format="audio/mp3", autoplay=True)

    st.session_state.process_running = False
