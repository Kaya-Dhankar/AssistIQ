import streamlit as st
from pytube import Search

def show_songs():
    st.title("🎵Song Player")

    song_name = st.text_input("Enter Song Name")
    platform = st.radio("Choose Platform", ["YouTube", "Spotify"])

    if st.button("Play Song"):
        if not song_name:
            st.warning("Please enter a song name.")
            return

        if platform == "YouTube":
            try:
                # Search YouTube and get first result
                s = Search(song_name)
                video = s.results[0]
                video_id = video.video_id
                video_url = f"https://www.youtube.com/embed/{video_id}"
                st.subheader("▶️ YouTube Result")
                st.video(video_url)
            except Exception as e:
                st.error(f"Could not fetch video: {e}")

        elif platform == "Spotify":
            search_url = f"https://open.spotify.com/search/{song_name.replace(' ', '%20')}"
            st.subheader("🎧 Spotify Result")
            st.markdown(f"[Click here to open on Spotify 🎶]({search_url})", unsafe_allow_html=True)
