import speech_recognition as sr

def listen_command():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5)

        return r.recognize_google(audio)

    except:
        return ""