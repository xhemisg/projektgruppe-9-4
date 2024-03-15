import streamlit as st




st.title('Hotelia')
st.write('created with a lot of coffee in the suburbans of St. Gallen')

# erstes Eingabefeld
user_name = st.text_input("Vorname und Nachname")

# so stelle ich dieses Feld dar
st.write(f'Lass uns ein passendes Hotel finden, {user_name}!')


user_standort = st.text_input("In welcher Region suchst du ein Hotel?")
st.write(f'Hallo, {user_name}! Wir helfen dir das passende Hotel in {user_standort} zu finden!')
