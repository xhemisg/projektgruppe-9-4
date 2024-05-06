import streamlit as st 
import API
import UI


##Titel und Überschriften anpassen
    #Nachfolgende HTLM-Code wurde von ChatGPT geschrieben, aufgrund fehlendem Wissen in dieser Programierungssprache 
    #Titel wird schräg gemacht und schriftgröße angepasst 
    #die Unterüberschrift wurde in einen geleben Rahmen gepackt, der als Trapez geformt und entsprechend der Hauptüberschrift ausgerichtet wurde 

st.markdown("""
    <h1 style='font-size:60px; font-style:italic; transform: rotate(-25deg); text-align:center;''Let us solve, what and where you\'ll eat tonight'/h1>
        <div style='font-size:20px; font-style:italic; text-align:center; 
                background: #ffe599; border: 3px solid #d0d0d0; padding: 10px;
                clip-path: polygon(10% 0%, 100% 0%, 90% 100%, 0% 100%);
                box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2);'>
       Der #1 Restaurant-Finder, um euer Dilemma zu lösen.
    </div>
""", unsafe_allow_html=True)


# Bild anzeigen
#image_url = "https://images.unsplash.com/photo-1590947132387-155cc02f3212?q=80&w=3240&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#st.image(image_url, caption="Bild von Unsplash")



    #dienen des Abstandes in der Website um den Code ansehnlicher zu gestalten 
st.write("")
st.write("")



##Notiz: der Folgende Code wurde mithilfe von ChatGPT geschrieben, um das Layout ansehnlich zu gestalten!! (da es nicht in der Vorlesung geleehrt wurde, wurde auf ChatGPT zurückgegriffen)
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


    #erneuter Abstand
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

##Interaktionsfelder## 

    #gestartet wird mit dem Feld in dem die Anzahl der personen beschrieben wird (1-4 Pax sind möglich) 
st.title("Anzahl Personen") 
user_input = st.text_input("Gib hier die Anzahl an Personen ein (Max. 4 Personen)") #hier anzahl an Personen eingeben


    #erneute Abstände 
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


    #Name des / der Teilnehmer 
st.title("Wie heißt du?")
user_input = st.text_input("Gebe hier deinen Namen ein") #hier Name eingeben 

##Angabe der Kriterien für die Auswahl des Abendessen## 

    #Überprüfe, ob der Nutzer bereits einen Namen eingegeben hat
if user_input:
    #user_input wird überprüft, wenn das erfüllt wird, wird Name eingefügt in "Lass uns beginnen"
    st.title(f"Lass uns beginnen, {user_input}") 

else:
    #Wenn user_input noch nicht ausgefüllt wurde, dann ändert sich nichts und es gibt nach wie vor die Aufforderung dies zu tun. 
    st.title("Bitte gib deinen Namen ein!!") 



    #erneute Abstände 
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")





    #Region wo man essen will wird eingegeben 
location = st.text_input("Wo würdest du gerne essen?")

    #Die Kategroie stehen zur Auswahl mit hilfe einer Drop-Down-Applikation 
categories = st.multiselect("Welche Küche bevorzugst du", ["newamerican", "italian", "swissfood", "chineese", "mexican" ]) #Liste mit verschiedenen Küchen

    #Hier wird der price angegeben, mithilfe einer Slidefunktion in dem zwischen Kategorie 1-4 ausgewählt werden kann. Hier kann es nur in ganzen Zahlen ausgewählt werden
price = st.slider("Select a budget", 1, 4, 3 )

    #Hier wird das Rating der Restaurants ausgewählt, auch mit einem silder. Jedoch kann hier das Rating in 0.1 schritten ausgewählt werden 
min_rating = st.slider("Select a minimum rating", 1.0, 5.0, 3.0, step =0.1)




##Hier wird nun die Ausgewählten Kriterien auf die Restaurants angewendet 
    #es werden in all_restaurants alle Restaurants angezeigt die den Kriterien entsprechen 
all_restaurants = []

    #hier können die Fav. Restaurants abgespeichert werden, wenn die App öfters benutzt wird 
fav_restaurants = []




##Interaktion um die Anwendung auf die verschiedenen Restaurants zu starten 
    #hier wird die Suche nach den Restaurants gestartet 
if st.button("Finde mein Restaurant"):
    #zugriff auf die verwendete API 
    restaurant_data = API.get_restaurant_data(location, categories, price, min_rating)

    #Darstellung von allen Restaurants über die Verknüpfung mit der API durch restaurant_data 
    all_restaurants = restaurant_data

    #hier wird über die UI (user Interface) die Restaurants dargestellt und ausgegeben, mit denen dann weiter Interagiert werden kann in Form von Abspeicherung der Restaurants als Favorieten 
    #dargestellt wird das ganze in durch fav_restaurants die zu beginn eine leere Liste sind 
    UI.restaurant_data_display(restaurant_data,fav_restaurants)
   
    #hier werden die Favoriten angezeigt die Abgespeichert wurden, die anzeige erfoglt auch über das UI mit einer verbindung zur Leeren Liste in fav_restaurants[] 
if st.button("Zeig meine Favouriten"):
    UI.show_favourites(fav_restaurants)
