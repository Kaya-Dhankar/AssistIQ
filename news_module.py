# news_module.py

import streamlit as st
import requests

API_KEY = "caa4c35f311d49cf9681ce07a256b804"

def show_news():
    st.subheader("📰 Top Headlines")

    categories = ["general", "business", "entertainment", "health", "science", "sports", "technology"]
    countries = {
        "India": "in",
        "United States": "us",
        "United Kingdom": "gb",
        "Australia": "au",
        "Canada": "ca",
        "Germany": "de",
        "France": "fr",
        "Singapore": "sg"
    }

    selected_country = st.selectbox("🌍 Select Country", list(countries.keys()))
    selected_category = st.selectbox("🗂️ Select Category", categories)

    if st.button("🔍 Get News"):
        with st.spinner("Fetching top headlines..."):
            url = (
                f"https://newsapi.org/v2/top-headlines?"
                f"country={countries[selected_country]}&"
                f"category={selected_category}&"
                f"apiKey={API_KEY}"
            )

            try:
                response = requests.get(url)
                data = response.json()

                # Fallback if no results
                if data.get("status") == "ok" and data.get("articles"):
                    show_articles(data)
                else:
                    st.info("No headlines found for this country & category. Searching globally...")
                    fallback_url = (
                        f"https://newsapi.org/v2/everything?"
                        f"q={selected_category}+{selected_country}&"
                        f"sortBy=publishedAt&"
                        f"apiKey={API_KEY}"
                    )
                    fallback_response = requests.get(fallback_url)
                    fallback_data = fallback_response.json()

                    if fallback_data.get("status") == "ok" and fallback_data.get("articles"):
                        show_articles(fallback_data)
                    else:
                        st.warning("No news found globally for this topic.")

            except Exception as e:
                st.error(f"❌ Error fetching news: {e}")


def show_articles(data):
    for article in data["articles"][:5]:
        st.markdown(f"### {article.get('title', 'No Title')}")
        if article.get("urlToImage"):
            st.image(article["urlToImage"], use_column_width=True)
        st.write(article.get("description", "No description available."))
        st.markdown(f"[Read more]({article.get('url')})")
        st.markdown("---")
