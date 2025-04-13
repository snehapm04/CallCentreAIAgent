import speech_recognition as sr

def speech_to_text(audio_file):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        print("Listening to the audio...")
        audio_data = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio_data)
            print("Recognized Text:")
            print(text)
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

# Example usage
if __name__ == "__main__":
    speech_to_text("output.wav")
