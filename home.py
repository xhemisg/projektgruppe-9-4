import streamlit as st

if 'usernames' not in st.session_state:
    st.session_state['usernames'] = []


st.title('Hotelia')
st.write('created with a lot of coffee in the suburbans of St. Gallen')

# erstes Eingabefeld
user_name = st.text_input("Vorname und Nachname")

# so stelle ich dieses Feld dar





# Append the new username to the list if it's not already there
if user_name and user_name not in st.session_state['usernames']:
    st.session_state['usernames'].append(user_name)
    # Print the updated list of usernames to the console
    print("Updated list of usernames:", st.session_state['usernames'])
    print ("list of usernames:", st.session_state['usernames'])

st.write(f'Lass uns ein passendes Hotel finden, {user_name}!')


user_standort = st.text_input("In welcher Region suchst du ein Hotel?")
st.write(f'Hallo, {user_name}! Wir helfen dir das passende Hotel in {user_standort} zu finden!')

