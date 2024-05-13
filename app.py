import streamlit as st 
import API
import UI


st.set_page_config(page_title="Bite Buddy", layout="wide", initial_sidebar_state="collapsed")


st.title('Let us solve, what and where you\'ll eat tonight')
st.write('Der #1 Restaurant-Finder, um euer Dilemma zu lösen')
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
st.write("")
st.write("")
st.write("")

#nun Folgend die ersten Interaktionsfelder 
#gestartet wird mit dem Feld in dem die Anzahl der personen beschrieben wird (1-4 Pax sind möglich) 
st.title("Anzahl Personen") 
players = st.radio('Wie viele personen seit ihr?', ["2", "3", "4"], index = None, horizontal = True )


st.write("")#dienen des Abstandes in der Website um den Code ansehnlicher zu gestalten 
st.write("")



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

    # Determine if all names are entered
    all_names_entered = len(names_entered) == st.session_state['players']
    st.session_state['names'] = names_entered
    # Request location if all names are entered
    if all_names_entered:
        st.title("In welcher Ortschaft wollt ihr essen?")
        location = st.text_input(" ", key="ort", placeholder="Bitte gebt eine Stadt ein!")
        if location:
            st.session_state['location'] = location
            link_button_disabled = False 
        else:
            link_button_disabled = True

      
st.page_link ("pages/playerpreferences.py", label= "Lass uns Los Legen", disabled = link_button_disabled)

#Nun beginnt der eigentliche Teil indem die vorgebenen Kriterien angegeben werden 




#Küche eingeneben 
st.write("")#dienen des Abstandes in der Website um den Code ansehnlicher zu gestalten 
st.write("")






