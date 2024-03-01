import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    return audio

def transcribe(audio):
    recognizer = sr.Recognizer()

    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "Sorry, I'm having trouble accessing the speech recognition service."

if __name__ == "__main__":
    while True:
        audio_input = listen()
        text_output = transcribe(audio_input)
        print("You said:", text_output)
