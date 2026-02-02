import webbrowser
import datetime
import os

def handle_command(text: str):
    text = text.lower()

    if "open youtube" in text:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    if "time" in text:
        return datetime.datetime.now().strftime("It's %I:%M %p")

    if "shutdown" in text:
        return "Shutdown command detected but blocked for safety 😄"

    return None