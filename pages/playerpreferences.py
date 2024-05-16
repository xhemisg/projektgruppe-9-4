import streamlit as st 
import API
import UI


st.set_page_config(page_title="Bite Buddy", layout="wide", initial_sidebar_state="collapsed") #Konfiguration der Page

if 'current_index' not in st.session_state: #Verfulgung der Spieler
    st.session_state['current_index'] = 0

current_player = st.session_state['names'][st.session_state['current_index']] #holt basierend auf aktuellem durchlauf den Namen des Spielers


#player_likes inizialisieren
if 'player_likes' not in st.session_state:
            st.session_state['player_likes'] = {}
#min_srating inizialisieren um es in anderen pages zu verwenden        
if 'min_rating' not in st.session_state:
            st.session_state['min_rating'] = {}
            
# abgleich ob bereits alle spieler abgegeben haben 
allespielerdone = len(st.session_state['player_likes']) == len(st.session_state['names'])

            
if not allespielerdone: #solange nicht True wird die Maske für die Präferenzen und Likes angezeigt 
    st.title(f"{current_player}, bitte deine Präferenzen!")
# hole die Variablen für Location und open_at vom sessionstate 
    location = st.session_state.get('location') 
    open_at = st.session_state.get('open_at')
    categories = 'restaurant' # um nur restaurants angzeigt zu kriegen base value
    
    #User Input für Filter Kriterien
    preis = st.slider("Was ist dein Budget?", 1, 4, 3 )
    min_rating = st.slider("Wie gut muss die Bewertung Mindestens sein?", 1.0, 5.0, 3.0, step =0.1, help = "Bei höheren Bewertungen kann es sein dass es weniger bis keine Resultate gibt.")
    st.session_state['min_rating'] = min_rating
    #hinweis dass bei Hoher mindest bewertung nicht so viele Resultate angezeigt werden
    limit = st.radio('Wie viele Vorschläge willst du?', ["10", "20", "30"], index = None, horizontal = True )

    price = str(preis)
    
    st.divider()

    if st.button("Finde mein Restaurant"): # ausführen des API requests und der Funktion um die Spielerspeziefischen Resultate anzuzeigen
        restaurant_data = API.get_restaurant_data(location, open_at, categories, price, min_rating, limit)
        if UI.restaurant_data_display(restaurant_data, current_player):
            # Capture likes when data is displayed and submitted.
            st.session_state['player_likes'][current_player] = st.session_state.get('liked_results', [])
    st.divider()   
    
    if st.button("Nächster"):
        # Speichern der Likes vom spieler davor 
        if current_player not in st.session_state['player_likes']:
            st.session_state['player_likes'][current_player] = st.session_state.get('liked_results', [])

        # Überprüfen ob es der letzte spieler ist (ChatGPT Lösung da sonst immer erst die resultate des letzten spieler bim nochmaligen Cklicken von Nächster Button gespeichert wurden)
        if len(st.session_state['player_likes']) == len(st.session_state['names']):
            st.session_state['current_index'] = 0  # Reset for results
            st.experimental_rerun()
        else:
            st.session_state['current_index'] += 1 if st.session_state['current_index'] < len(st.session_state['names']) - 1 else 0
            st.experimental_rerun() #seite wieder leeren für nächsten spieler
    
if allespielerdone:
    st.switch_page ("pages/ergebnis.py") #label= "Zu den Resultaten")
    UI.display_final_likes #führt die funktion aus 

