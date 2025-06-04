import streamlit as st
from translate import Translator
from gtts import gTTS
import tempfile
import base64

def show_translator():
    st.title("🌐 Multilingual Translator")

    # Language code dictionary
    languages = {
        'English': 'en',
        'Hindi': 'hi',
        'Bengali': 'bn',
        'Spanish': 'es',
        'French': 'fr',
        'Marathi': 'mr',
        'German': 'de',
        'Chinese (Simplified)': 'zh',
        'Japanese': 'ja',
        'Russian': 'ru'
    }

    # Language selection
    source_lang = st.selectbox("From Language", list(languages.keys()), index=0)
    target_lang = st.selectbox("To Language", list(languages.keys()), index=1)

    # Text input
    input_text = st.text_area("Enter text to translate:")

    def speak_text_gtts(text, lang_code):
        try:
            tts = gTTS(text=text, lang=lang_code)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                audio_path = fp.name

            audio_file = open(audio_path, 'rb')
            audio_bytes = audio_file.read()
            audio_b64 = base64.b64encode(audio_bytes).decode()
            audio_html = f"""
                <audio autoplay controls>
                    <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Text-to-Speech failed: {e}")

    if input_text:
        try:
            # Translation
            translator = Translator(from_lang=languages[source_lang], to_lang=languages[target_lang])
            translated_text = translator.translate(input_text)

            st.subheader("Translated Text:")
            st.write(translated_text)

            if st.button("🔊 Speak Translated Text"):
                speak_text_gtts(translated_text, languages[target_lang])

        except Exception as e:
            st.error(f"Translation failed: {e}")
