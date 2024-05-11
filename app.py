import streamlit as st 
import API
import UI



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
user_input = st.text_input("Gib hier die Anzahl an Personen ein (Max. 4 Personen)")


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





city_name = st.text_input("Wo würdest du gerne essen?")
categories = st.multiselect("Welche Küche bevorzugst du", ["newamerican", "italian", "swissfood", "chineese", "mexican" ])
price = st.slider("Select a budget level (0-4, where 0 is most affordable)", 0, 4, 1)
min_rating = st.slider("Select a minimum rating", 1.0, 5.0, 3.0, step =0.1)


all_restaurants = []
fav_restaurants = []


if st.button("Finde mein Restaurant"):
    restaurant_data = API.get_restaurant_data(city_name, price, categories)
    UI.restaurant_data_display(restaurant_data, fav_restaurants)
   

if st.button("Zeig meine Favouriten"):
    UI.show_favourites(fav_restaurants)
