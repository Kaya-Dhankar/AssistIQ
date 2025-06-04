import streamlit as st
import openai
from news_module import show_news
from weather_module import show_weather
from songs_module import show_songs
from translator_app import show_translator
from health_tracker import show_tracker
from smart_search import show_search


st.set_page_config(page_title="SmartLife Hub", layout="centered")
# ---- Set Background Color ----
st.markdown("""
    <style>
        body {
            background-color: #e8f5e9;  /* You can change this hex color code to any color you want */
        }
    </style>
""", unsafe_allow_html=True)

menu = st.sidebar.selectbox(
    "Choose a Feature",
    ["Home", "News", "Weather", "Songs", "Translator","Health_Tracker","Smart_Search"]
)

# ---- Custom CSS for Styling ----
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f4;
        }
        .header {
            text-align: center;
            padding: 20px 0;
        }
        .header h1 {
            color: #2c3e50;
            font-size: 2.5em;
            margin: 0;
        }
        .header p {
            color: #7f8c8d;
            font-size: 1.2em;
            margin: 0;
        }
        .feature-card {
            background-color:white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.2s;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 4px 4px 15px rgba(0,0,0,0.2);
        }
        .feature-card h3 {
            color: #2c3e50;
        }
        .feature-card p {
            color: #7f8c8d;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            margin: 10px;
            background-color: #2c3e50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .button:hover {
            background-color: #34495e;
        }
        .feature-image {
            width: 60px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

if menu == "Home":
    st.markdown("""
          <style>
              .hero {
                  text-align: center;
                  padding: 80px 20px;
                  background-color: #a5d6a7;
                  color: black;
                  border-radius: 12px;
                  margin-bottom: 40px;
                  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
              }
              .hero h1 {
                  font-size: 48px;
                  margin-bottom: 10px;
                  font-weight: 700;
              }
              .hero p {
                  font-size: 22px;
                  margin-bottom: 30px;
                  font-weight: 500;
              }
              .hero button {
                  background-color: #388e3c;
                  color: white;
                  border: none;
                  padding: 15px 40px;
                  font-size: 18px;
                  border-radius: 8px;
                  cursor: pointer;
                  transition: background-color 0.3s ease;
              }
              .hero button:hover {
                  background-color: #2e7d32;
              }
          </style>

          <div class="hero">
              <h1>✨ Meet AssistIQ</h1>
              <p>Your All-in-One AI Assistant for Life</p>
          </div>
      """, unsafe_allow_html=True)

    st.write("---")
    cols = st.columns(3)

    features = [
        {"title": "News", "desc": "Latest headlines from around the world.",
         "img": "https://img.icons8.com/color/96/news.png"},

        {"title": "Weather", "desc": "Up-to-date weather information for your area.",
         "img": "https://img.icons8.com/color/96/cloud.png"},

        {"title": "Music", "desc": "Discover and listen to your favorite tracks.",
         "img": "https://img.icons8.com/color/96/musical-notes.png"},

        {"title": "Language", "desc": "Translate between multiple languages easily.",
         "img": "https://img.icons8.com/color/96/language.png"},

        {"title": "Health Tracker", "desc": "Track your health and wellness data.",
         "img": "https://img.icons8.com/color/96/heart-health.png"},

        {"title": "Smart Search", "desc": "Search smarter and faster with our AI tools.",
         "img": "https://img.icons8.com/color/96/search.png"}
    ]
    for i, feature in enumerate(features):
        col = cols[i % 3]
        with col:
            st.markdown(f"""
                   <div class='feature-card'>
                       <img src='{feature['img']}' class='feature-image'/>
                       <h3>{feature['title']}</h3>
                       <p>{feature['desc']}</p>
                   </div>
               """, unsafe_allow_html=True)

elif menu == "News":
    show_news()
elif menu == "Weather":
    show_weather()
elif menu == "Songs":
    show_songs()
elif menu == "Translator":
    show_translator()
elif menu == "Health_Tracker":
    show_tracker()
elif menu == "Smart_Search":
    show_search()
