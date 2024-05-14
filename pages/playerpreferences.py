import streamlit as st 
import API
import UI


st.set_page_config(page_title="Bite Buddy", layout="wide", initial_sidebar_state="collapsed")

if 'current_index' not in st.session_state:
    st.session_state['current_index'] = 0

current_player = st.session_state['names'][st.session_state['current_index']]

st.title(f"{current_player}, bitte deine Präferenzen!")



location = st.session_state.get('location', "Zürich")
open_at = st.session_state.get('open_at')

categories = st.multiselect("Welche Küche bevorzugst du", ["newamerican", "italian", "swissfood", "chineese", "mexican" ])
price = st.slider("Select a budget", 1, 4, 3 )
min_rating = st.slider("Select a minimum rating", 1.0, 5.0, 3.0, step =0.1)
limit = st.radio('wie viele Vorschläge Willst du?', ["10", "20", "30"], index = None, horizontal = True )




if st.button("Finde mein Restaurant"):
    restaurant_data = API.get_restaurant_data(location, categories, price, min_rating, open_at, limit)
    UI.restaurant_data_display(restaurant_data, current_player)
   
if st.button("Next Player"):
    if 'player_likes' not in st.session_state:
        st.session_state['player_likes'] = {}

    st.session_state['player_likes'][current_player] = st.session_state['liked_results']

    if st.session_state['current_index'] < len(st.session_state['names']) - 1:
        st.session_state['current_index'] += 1
    else:
        st.session_state['current_index'] = 0  # Reset or move to a summary page
    st.experimental_rerun()
    
    
st.page_link ("pages/ergebnis.py", label= "Zu den Resultaten")
    