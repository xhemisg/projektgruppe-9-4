import streamlit as st 
import API
import UI


st.set_page_config(page_title="Bite Buddy", layout="wide", initial_sidebar_state="collapsed")

if 'current_index' not in st.session_state: #Verfulgung der Spieler
    st.session_state['current_index'] = 0

current_player = st.session_state['names'][st.session_state['current_index']]


#player_likes inizialisieren
if 'player_likes' not in st.session_state:
            st.session_state['player_likes'] = {}
# abgleich ob bereits alle spieler abgegeben haben 
allespielerdone = len(st.session_state['player_likes']) == len(st.session_state['names'])

            
if not allespielerdone:
    st.title(f"{current_player}, bitte deine Präferenzen!")

    location = st.session_state.get('location', "Zürich")
    open_at = st.session_state.get('open_at')

    categories = st.multiselect("Welche Küche bevorzugst du", ["newamerican", "italian", "swissfood", "chineese", "mexican" ])
    price = st.slider("Select a budget", 1, 4, 3 )
    min_rating = st.slider("Select a minimum rating", 1.0, 5.0, 3.0, step =0.1)
    limit = st.radio('Wie viele Vorschläge Willst du?', ["10", "20", "30"], index = None, horizontal = True )

    st.divider()

    if st.button("Finde mein Restaurant"):
        restaurant_data = API.get_restaurant_data(location, open_at, categories, price, min_rating, limit)
        if UI.restaurant_data_display(restaurant_data, current_player):
            # Capture likes when data is displayed and submitted.
            st.session_state['player_likes'][current_player] = st.session_state.get('liked_results', [])
    st.divider()   
    
    if st.button("Next Player"):
        # Ensure current player's likes are captured before moving on.
        if current_player not in st.session_state['player_likes']:
            st.session_state['player_likes'][current_player] = st.session_state.get('liked_results', [])

        # Check if this was the last player.
        if len(st.session_state['player_likes']) == len(st.session_state['names']):
            st.session_state['current_index'] = 0  # Reset for results
            st.experimental_rerun()
        else:
            st.session_state['current_index'] += 1 if st.session_state['current_index'] < len(st.session_state['names']) - 1 else 0
            st.experimental_rerun() #seite wieder leeren für nächsten spieler
    
if allespielerdone:
    st.page_link ("pages/ergebnis.py", label= "Zu den Resultaten")
    

