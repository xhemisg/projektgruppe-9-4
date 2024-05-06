import streamlit as st 
import API
import UI



##Titel und Überschriften anpassen
    #Nachfolgende HTLM-Code wurde von ChatGPT geschrieben, aufgrund fehlendem Wissen in dieser Programierungssprache 
    #Titel wird schräg gemacht und schriftgröße angepasst 
    #die Unterüberschrift wurde in einen geleben Rahmen gepackt, der als Trapez geformt und entsprechend der Hauptüberschrift ausgerichtet wurde 
st.markdown("""
    <h1 style='font-size:60px;                                           # Schriftgröße auf 60px einstellen
                 font-style:italic;                                      # Schrift im Kursivstil formatieren
                 transform: rotate(-3deg);                               # Überschrift um -3 Grad drehen (nach links neigen)
                 text-align:center;'>                                    # Textausrichtung auf die Mitte setzen
        Let us solve, what and where you'll eat tonight                  # Überschrift Inhalt 
    </h1>
    <div style='font-size:20px;                                          # Schriftgröße der Unterüberschrift auf 20px einstellen
                 font-style:italic;                                      # Schrift im Kursivstil formatieren
                 transform: rotate(-3deg);                               # Unterüberschrift um -3 Grad drehen (nach links neigen)
                 text-align:center;                                      # Textausrichtung auf die Mitte setzen
                 background: #ff963B;                                    # Hintergrundfarbe der Box auf #ff963B (Orange) einstellen
                 border: 3px solid #d0d0d0;                              # Box-Rand (3px dick, hellgrau)
                 padding: 10px;                                          # Innenabstand der Box auf 10px einstellen
                 clip-path: polygon(10% 0%, 100% 0%, 90% 100%, 0% 100%); # Form der Box als Trapez einstellen
                 box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.2);'>           # Schlagschatten der Box auf 3x5px, leicht schwarz
        Der #1 Restaurant-Finder, um euer Dilemma zu lösen.              #Unterüberschrift Inhalt 
    </div>
""", unsafe_allow_html=True) #erlaubt es uns HTLM in Streamlit direkt zu nutzen 


#Bild anzeigen (geht noch nicht so wie es soll!!!)

#image_url = "https://images.unsplash.com/photo-1590947132387-155cc02f3212?q=80&w=3240&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
#st.image(image_url, caption="Bild von Unsplash")

st.write("")
st.write("")

st.write("NUR DIESE DREI SCHRITTE NEHMEN EUCH DEN HUNGER")

st.write("")
st.write("")

##kurze Darstellung der Schritte wie man zum Ergebnis kommt 
    #Darstellung erfolgt in einer Tabelle, welche aus zwei Zeilen (headline & inhalt) und drei Spalten (die drei Schritte) bestehen 
    #der Code wurde selber Geschrieben, nach der Vorlage von den bisher genutzten von Chat-GPT ausgegeben HTLM programmierten Codes (vgl. Code weiter oben zur Darstellung der Überschrift)
    #Header-Zeile erstellen
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='border: 1px solid #ddd;  # Rand der Box: 1px dick, hellgrau 
                 padding: 10px;          # Innenabstand: 10px 
                 border-radius: 5px;'>   # Ecken der Box abrunden 
        Anzahl an Personen               # Inahlt Überschrift erste Spalte 
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='border: 1px solid #ddd;  # Rand der Box: 1px dick, hellgrau 
                 padding: 10px;          # Innenabstand: 10px 
                 border-radius: 5px;'>   # Ecken der Box abrunden 
        Eure Kriterien                   # Inhalt Überschrift zweite Spalte 
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='border: 1px solid #ddd;  # Rand der Box: 1px dick, hellgrau 
                 padding: 10px;          # Innenabstand: 10px 
                 border-radius: 5px;'>   # Ecken der Box abrunden 
        Zaubere!                         # Inhalt Überschrift dritte Spalte 
    </div>
    """, unsafe_allow_html=True)

# Inhalt-Zeile erstellen
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style='border: 1px solid #ddd;         # Rand der Box: 1px dick, hellgrau 
                 padding: 10px;                 # Innenabstand: 10px 
                 border-radius: 5px;'>          # Ecken der Box abrunden 
        Gebt an wie viele Leute fast verhungern # Inhalt erste Spalte zweite Zeile 
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='border: 1px solid #ddd;     # Rand der Box: 1px dick, hellgrau 
                 padding: 10px;             # Innenabstand: 10px 
                 border-radius: 5px;'>      # Ecken der Box abrunden 
       Jeder gibt manuell seine Daten ein   # Inhalt zweite Überschrift, zweite Zeile 
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style='border: 1px solid #ddd;             # Rand der Box: 1px dick, hellgrau 
                 padding: 10px;                     # Innenabstand: 10px 
                 border-radius: 5px;'>              # Ecken der Box abrunden 
        Nur noch ein Klick und der Zauber beginnt   # Inhalt dritte Überschrift, zweite Zeile 
    </div>
    """, unsafe_allow_html=True)

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
