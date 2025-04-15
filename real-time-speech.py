import gradio as gr
import speech_recognition as sr
import pyttsx3
import tempfile
import os

def speech_to_text(audio_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            text = "Could not understand audio."
        except sr.RequestError as e:
            text = f"Request error: {e}"

    return text

# Convert text to speech and return audio path
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.setProperty('volume', 1.0)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio_path = temp_audio.name

    engine.save_to_file(text, temp_audio_path)
    engine.runAndWait()

    return temp_audio_path

# Combined function
def speech_to_speech(audio_path):
    text = speech_to_text(audio_path)
    speech_output_path = text_to_speech(text)
    return text, speech_output_path

# Gradio interface
interface = gr.Interface(
    fn=speech_to_speech,
    inputs=gr.Audio(type="filepath", label="🎤 Record your voice"),
    outputs=[
        gr.Text(label="📝 Recognized Text"),
        gr.Audio(label="🗣️ Converted Speech", type="filepath"),
    ],
    title="🗣️ Real-Time Speech-to-Speech App",
    description="Speak something and let the app convert it to text, then back to speech!"
)

interface.launch()
