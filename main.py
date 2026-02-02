from ears import listen
from brain import ask_ayra
from voice import speak


def main():
    speak("AYRA online. Say something.")

    while True:
        query = listen()
        if query:
            reply = ask_ayra(query)
            speak(reply)

if __name__ == "__main__":
    main()
