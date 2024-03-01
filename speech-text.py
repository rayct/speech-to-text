import speech_recognition as sr
# import pyaudio

def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen to the user's input
        audio_data = recognizer.listen(source)

        print("Processing...")

        try:
            # Use Google Web Speech API to recognize the audio
            text = recognizer.recognize_google(audio_data)

            return text

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return None

        except sr.RequestError as e:
            print(f"Error: {e}")
            return None

if __name__ == "__main__":
    # Call the function to convert speech to text
    recognized_text = speech_to_text()

    if recognized_text:
        print("You said:", recognized_text)
