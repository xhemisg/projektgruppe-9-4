import streamlit as st

if 'usernames' not in st.session_state:
    st.session_state['usernames'] = []


st.title('Let us solve, what and where you\'ll eat tonight')
st.write('Der #1 Restaurant-Finder, um euer Dilemma zu lösen')
st.write("")#dienen des Abstandes in der Website um den Code ansehnlicher zu gestalten 
st.write("")



# erstes Eingabefeld komplett im Folgenden
st.write("NUR DIESE DREI SCHRITTE NEHMEN EUCH DEN HUNGER") #info was die folgenden Templates aussagen 
st.write("")#dienen des Abstandes in der Website um den Code ansehnlicher zu gestalten 
st.write("")


#Spalten mit Infos zu den drei Schritten um mit BiteBuddy erfolgreich sein Essen auszuwählen
col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("Anzahl an Personen"): #durch st.expand die Möglichkeit jede der drei Spalten auszuklappen, sodass nur Überschrift in erster Linie zu sehen ist 
        st.write("Gebt an wieviel Leute fast verhungern")

with col2:
    with st.expander("Eure Kriterien"):
        st.write("Jeder gibt manuell seine Daten zu Budget, Standort, Küche und Wunschbewertung ein")

with col3:
    with st.expander("Zaubere!"):
        st.write("Nur noch einmal klicken und der Zauber beginnt")

st.write("")#dienen des Abstandes in der Website um den Code ansehnlicher zu gestalten 
st.write("")
st.write("")


#nun wird die BiteBuddy Experience erklärt in den einzelnen Schritten; im Folgenden wird CSS genutzt um den Kasten zu gestalten 

# CSS zur Gestaltung des Kastens direkt in HTML einbetten
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
user_input = st.text_input("Gib hier die Anzahl an Personen ein (Max. 4 Personen)")

#nun folgt der Start Button 
st.button("Wir möchten Starten") 
st.write("")#dienen des Abstandes in der Website um den Code ansehnlicher zu gestalten 
st.write("")
st.write("")
st.write("")
st.write("")


#Name des / der Teilnehmer 
st.title("Wie heißt du?")
user_input = st.text_input("Gebe hier deinen Namen ein")

#Nun beginnt der eigentliche Teil indem die vorgebenen Kriterien angegeben werden 
# Überprüfe, ob der Nutzer bereits einen Namen eingegeben hat
if user_input:
    st.title(f"Lass uns beginnen, {user_input}")
else:
    st.title("Bitte gib deinen Namen ein!!")

#Küche eingeneben 
st.write("")#dienen des Abstandes in der Website um den Code ansehnlicher zu gestalten 
st.write("")
st.write("")
st.write("")
st.write("")

user_input = st.text_input("Welche Küche bevorzugst du? Bitte gebe den Namen in CAPSLOCK ein!")

#Kriterien eingeben 
col1, col2, col3 = st.columns(3)

with col1:
    with st.title("Dein Standort"): #durch st.expand die Möglichkeit jede der drei Spalten auszuklappen, sodass nur Überschrift in erster Linie zu sehen ist 
       user_input = st.text_input("Wo wollt ihr essen? Gebe dein Standort ein")
with col2:
    with st.title("Dein Budget von 1-5"):
        user_input = st.text_input("Dein Budget von 1-5 (1 sehr tief, 5 sehr hoch)")

with col3:
    with st.title("Die Mindestbewertung?"):
        user_input = st.text_input("Die Bewertung von 1-5 (1 sehr tief, 5 sehr hoch)")





