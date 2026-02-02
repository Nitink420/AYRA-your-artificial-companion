import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("🎧 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        print("🧑 You:", text)
        return text

    except sr.UnknownValueError:
        return None
    except Exception as e:
        print("EARS ERROR:", e)
        return None
