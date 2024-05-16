import streamlit as st 
import API
import UI
import requests
import datetime
import pytz


st.set_page_config(page_title="Bite Buddy", layout="wide", initial_sidebar_state="collapsed")

col1, col2 = st.columns([1, 2]) #Zwei Kolonnen um um es ansichtlicher zu machen 

with col1:
    # APP Titel
    st.title('Let us solve, what and where you\'ll eat tonight')
    st.write('Der #1 Restaurant-Finder, um euer Dilemma zu lösen')

with col2: #Tietelbild der APP
    st.image('BiteBuddy Immage.jpeg')
st.write("")#dienen des Abstandes in der Website um den Code ansehnlicher zu gestalten 
st.write("")



#Notiz: der Folgende Code wurde mithilfe von ChatGPT geschrieben, um das Layout ansehnlich zu gestalten!! (da es nicht in der Vorlesung geleehrt wurde, wurde auf ChatGPT zurückgegriffen)
def set_css():
    st.markdown("""
        <style>
        .color-box {
            padding: 20px;              /* Innenabstand */
            background-color: #ffe599;  /* Hintergrundfarbe */
            color: black;               /* Textfarbe */
            border-radius: 5px;         /* Abgerundete Ecken */
            text-align: center;         /* Text zentrieren */
            margin: 10px 0;             /* Abstand oben und unten */
        }
        .color-box h2 {
            margin: 0 0 10px 0;         /* Abstand um die Überschrift: kein oberer Abstand, 10px unterer Abstand */
            color: #003366;             /* Dunkelblaue Farbe für die Überschrift */
        }
        </style>
        """, unsafe_allow_html=True)

set_css()

# Verwende HTML für die Textanzeige
st.markdown("""
<div class="color-box">
    <h2>ERLEBE DIE BITEBUDDY EXPERIENCE!</h2>
    <p>1. Wähle unten die Anzahl an Personen</p>
    <p>2. Fülle die vorhandenen Kriterien aus</p>
    <p>3. Klicke auf "Zauberen"!</p>
    <p>4. Sehe welche Restaurants für euch in Frage kommen.</p>
</div>
""", unsafe_allow_html=True)

st.write("")#dienen des Abstandes in der Website um den Code ansehnlicher zu gestalten 
st.write("")
st.write("")


#nun Folgend die ersten Interaktionsfelder 
#gestartet wird mit dem Feld in dem die Anzahl der personen beschrieben wird (1-4 Pax sind möglich) 
st.title("Anzahl Personen") 
players = st.radio('Wie viele personen seit ihr?', ["2", "3", "4"], index = None, horizontal = True )


st.write("")#dienen des Abstandes in der Website um den Code ansehnlicher zu gestalten 
st.write("")

timezone = pytz.timezone('Europe/Zurich')


link_button_disabled = True #Button auschaulten 

if players:
    st.session_state['players'] = int(players)
    st.title("Wie heißt ihr?")

    # Create a text input for each player and let Streamlit manage the session state
    names_entered = []
    for i in range(1, st.session_state['players'] + 1):
        name = st.text_input(" ", key=f"spieler{i}", placeholder=f"Gast {i}")
        
        if name:
            names_entered.append(name)
    if 'names' not in st.session_state:
        st.session_state['names'] = []
    # Determine if all names are entered
    all_names_entered = len(names_entered) == st.session_state['players']
    st.session_state['names'] = names_entered
    # Request location if all names are entered
    if all_names_entered:
        st.title("In welcher Ortschaft wollt ihr essen?")
        location = st.text_input(" ", key="ort", placeholder="Bitte gebt eine Stadt ein!")
        st.title("Wann wollt ihr essen gehen?")
        time = st.time_input("Choose the dining time:", "now")
        
        if location: #wird überprüft ob location existiert und nur dann kann man weiter cklicken - stellt sicher das man später keine problme hat wenn die location fehlt 
                    #zeit ist per default auf Jetzt gestellt darum nicht nötig dies zu testen 
            st.session_state['location'] = location
            link_button_disabled = False 
        else:
            link_button_disabled = True
        
        
    # Datum von heute - App is gedacht als spontan nur für den abend userfriendlyness
        today_date = datetime.date.today()
    # Zeit und Datum Kombinieren - ChatGPT hilfe um den code zu erstellen
        dining_datetime = datetime.datetime.combine(today_date, time)
        if 'open_at' not in st.session_state:
            st.session_state['open_at'] = []
        open_at = int(timezone.localize(dining_datetime).timestamp())
        st.session_state['open_at'] = open_at #opent_at variable in sessionstate ablegen für API nutzen

st.divider ()  
#Nun beginnt der eigentliche Teil indem die vorgebenen Kriterien angegeben werden - Verlinkung auf eine Unterseite   
st.page_link ("pages/playerpreferences.py", label= "Lass uns Los Legen", icon = "🍕", disabled = link_button_disabled)












