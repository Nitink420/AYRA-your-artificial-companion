# gui.py
import streamlit as st

from brain import ask_ayra
from tts import ayra_speak_bytes
from voice import listen_command

st.set_page_config(page_title="AYRA AI", page_icon="🤖")

st.title("🤖 AYRA AI")
st.write("Talk to AYRA using text or voice")

# TEXT INPUT (Enter press se chalega)
user_input = st.text_input("You:", placeholder="Type and press Enter...")

if user_input.strip():
    reply = ask_ayra(user_input)
    st.markdown(f"**AYRA:** {reply}")
    st.audio(ayra_speak_bytes(reply), format="audio/mp3", autoplay=True)

st.divider()

# VOICE BUTTON
if st.button("🎤 Speak"):
    spoken = listen_command()
    if spoken:
        st.markdown(f"**You:** {spoken}")

        reply = ask_ayra(spoken)
        st.markdown(f"**AYRA:** {reply}")
        st.audio(ayra_speak_bytes(reply), format="audio/mp3", autoplay=True)