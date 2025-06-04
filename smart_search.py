import streamlit as st
import wikipedia
import requests
from bs4 import BeautifulSoup

# Function to get results using Wikipedia or fallback to DuckDuckGo
def get_ai_result(query):
    try:
        wikipedia.set_lang("en")
        search_results = wikipedia.search(query)

        if not search_results:
            raise wikipedia.PageError(query)

        best_match = search_results[0]
        summary = wikipedia.summary(best_match, sentences=2)
        return f"🌐 Wikipedia says: {summary}"

    except wikipedia.DisambiguationError as e:
        try:
            summary = wikipedia.summary(e.options[0], sentences=2)
            return f"🌐 Wikipedia says: {summary}"
        except:
            pass

    except wikipedia.PageError:
        pass

    # Fallback to DuckDuckGo search
    try:
        url = f"https://duckduckgo.com/html/?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        results = soup.select(".result__snippet")
        if results:
            return f"🔎 Web says: {results[0].get_text()}"
    except Exception as e:
        print(f"DuckDuckGo error: {e}")

    return "❌ Sorry, I couldn't find a result."


# ✅ Streamlit UI function
def show_search():
    st.title("🔍 Smart AI Search")
    user_input = st.text_input("Ask anything...", "")

    if st.button("Search") and user_input:
        response = get_ai_result(user_input)
        st.write(response)


