import streamlit as st
import requests

# Fonction pour appeler l'API Flask
def get_random_quote():
    api_url = 'http://127.0.0.1:5000/random_quote'
    response = requests.get(api_url)
    return response.json()

# App Streamlit
def main():
    st.title('Citation random')

    # Appeler l'API Flask pour obtenir une citation aléatoire
    quote = get_random_quote()

    # Afficher les résultats dans Streamlit
    st.write(f"Text: {quote['text']}")
    st.write(f"Author: {quote['author']}")
    st.write(f"Tags: {', '.join(quote['tags'])}")


if __name__ == '__main__':
    main()
