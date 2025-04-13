import pyttsx3

def save_speech_to_wav(text, filename='output.wav'):
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)      # Speed of speech
    engine.setProperty('volume', 1.0)    # Volume (0.0 to 1.0)
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"Speech saved to {filename}")

# Example usage
if __name__ == "__main__":
    user_text = input("Enter text to convert to speech and save: ")
    save_speech_to_wav(user_text)
