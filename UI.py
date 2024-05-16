import streamlit as st
import app
import datetime

@st.experimental_fragment #Extrem wichtig das nicht das ganze script  neuladet sondern nur ein Teil
def restaurant_data_display(restaurant_data, current_player):
    open_at_datetime = datetime.datetime.fromtimestamp(st.session_state['open_at']) #Importiere Uhrzeit vom Sessionstate
    min_rating = st.session_state['min_rating'] #min_rating aus sessionstate holen
    #case keine Daten 
    if not restaurant_data:
        st.error("Keine Restaurants mit euren parametern Gefunden")
        return
    
    

    if 'liked_results' not in st.session_state: #session state für liked_results starten (liste der resultate) für alle 
        st.session_state['liked_results'] = []
    #liste der Resultate analysieren und nur die anzeigen die das min_rating habend a Yelp rating nicht als filter für den get request hat 
    filtered_restaurants = [restaurant for restaurant in restaurant_data if restaurant.get('rating', 0) >= min_rating]
    
    for restaurant in filtered_restaurants:
        #sessionstate für den jeweiligen nutzer
        if 'liked' not in restaurant:
            restaurant['liked'] = False
    #streamlit Form damit mehere inputs getätigt werden können ohne ständiges neu laden
    with st.form("like_form"):
        for idx, restaurant in enumerate(filtered_restaurants):
            col1, col2, col3 = st.columns([5, 3, 2]) #3 Kolonnen mit ration 5:3:2

            with col1:
                st.markdown(
                """
                <style>
             .image {
             height: 300px;
             width: 250px;
                object-fit: cover;
             }
                </style>
             """, unsafe_allow_html=True) #CSS injektion um bild grösse zu beinflussen
                
                if 'image_url' in restaurant and restaurant['image_url']:
                    st.markdown(f"<img class='image' src='{restaurant['image_url']}'/>", unsafe_allow_html=True)
                else:
                    st.write("Kein Bild Verfügbar")
                    
            with col2: #alle Restaurant informationen von API Request Visualisieren 
                st.write(f"**Name:** {restaurant['name']}")
                st.write(f"**Bewertungg:** {restaurant.get('rating', 'nicht Verfügbar')} ⭐")
                st.write(f"**Preis:** {restaurant.get('price', 'nicht Verfügbar')}")
                categories = ', '.join([cat['title'] for cat in restaurant.get('categories', [])]) #wenn mehere einträge bei diesem parameter zusammenfügen
                st.write(f"**Küche:** {categories}")
                address = ', '.join([restaurant['location'].get(key, '') for key in ['address1', 'city', 'state', 'zip_code']])
                st.write(f"**Adresse:** {address}")
                st.write(f"**Geöffnet am {open_at_datetime.strftime('%Y-%m-%d')} um {open_at_datetime.strftime('%H:%M')}**")   
                st.markdown(f'**Webseite:** [Auf Yelp anschauen]({restaurant.get("url")})', unsafe_allow_html=True)
            
            with col3:
                # Checkbox um restautrants zu liken
                liked_key = f"liked_{idx}"
                restaurant['liked'] = st.checkbox("Like", key=liked_key, value=restaurant.get('liked', False))

            st.markdown("---")
          # Submit button for the form
        submitted = st.form_submit_button("Meine Lieblinge Speichern")
    
    if submitted:
        current_likes = set(restaurant['id'] for restaurant in filtered_restaurants if restaurant.get('liked')) #schauen welche restaurants gerade gelicked wurden
        #zum sessionstate liked_reults hinzufügen wenn sie noch nicht vorhanden sind (logik zur analyse der likes)
        st.session_state['liked_results'] = [restaurant for restaurant in filtered_restaurants if restaurant['id'] in current_likes]  
        st.success("Deine Lieblings Restaurants sind gespeichert")

    




#Funktion zum Finalen Anzeigen der Analysierten gemeinsamen resultate

def display_final_likes():
    #Wenn gar keine likes getätig wurden
    if 'player_likes' not in st.session_state:
        st.title("Keine Gemeinsamen Lieblinge")
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
            <h2>Versucht etwas Neues!</h2>
            <p>1. Das erste Asiatisch Restaurant Welches Google vorschlägt</p>
            <p>2. Das erste Italienische Restaurant welches Google vorschlägt</p>
            <p>3. Das erste Afrikanische Restaurant welches Google vorschlägt</p>
           
            </div>
            """, unsafe_allow_html=True)
        return
# ChatGPT Hilfe für die Logik weil zu komplex mit den sessionstates und abgleichen 
    total_players = len(st.session_state['names'])
    all_likes = st.session_state['player_likes']

    restaurant_counts = {}
    for likes in all_likes.values():
        for restaurant in likes:
            restaurant_id = restaurant['id']
            if restaurant_id not in restaurant_counts:
                restaurant_counts[restaurant_id] = {
                    'count': 0,
                    'details': restaurant
                }
            restaurant_counts[restaurant_id]['count'] += 1

    liked_by_all = [info['details'] for info in restaurant_counts.values() if info['count'] == total_players]

    if liked_by_all:
        st.title("Ihr alle mögt:")
        st.divider()
        open_at_datetime = datetime.datetime.fromtimestamp(st.session_state['open_at'])#zeit importieren um die öffnungszeit anzuzegen
        #anzeige Für Die Restaurants in 2 Kollonnen analog des st.form
        for restaurant in liked_by_all:
            col1, col2 = st.columns([5,5])

            with col1:
                st.markdown(
                """
                <style>
             .image {
             height: 300px;
             width: 300px;
                object-fit: cover;
             }
                </style>
             """, unsafe_allow_html=True)
                
                if 'image_url' in restaurant and restaurant['image_url']:
                    st.markdown(f"<img class='image' src='{restaurant['image_url']}'/>", unsafe_allow_html=True)
                else:
                    st.write("No image available.")
                    
            with col2:
                st.write(f"**Name:** {restaurant['name']}")
                st.write(f"**Bewertungg:** {restaurant.get('rating', 'N/A')} ⭐")
                st.write(f"**Preis:** {restaurant.get('price', 'N/A')}")
                categories = ', '.join([cat['title'] for cat in restaurant.get('categories', [])])
                st.write(f"**Küche:** {categories}")
                address = ', '.join([restaurant['location'].get(key, '') for key in ['address1', 'city', 'state', 'zip_code']])
                st.write(f"**Adresse:** {address}")
                st.write(f"**Geöffnet am {open_at_datetime.strftime('%Y-%m-%d')} um {open_at_datetime.strftime('%H:%M')}**")
                    
                st.markdown(f'**Webseite:** [Auf Yelp anschauen]({restaurant.get("url")})', unsafe_allow_html=True)
            
            st.markdown("---")
    else: #wenn keine übereinstimmungen festgestellt wurden
        st.title("Keine Gemeinsamen Lieblinge")
        #Notiz: der Folgende Code wurde mithilfe von ChatGPT geschrieben, um das Layout ansehnlich zu gestalten!! (da es nicht in der Vorlesung geleehrt wurde, wurde auf ChatGPT zurückgegriffen)

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

       

# Verwende HTML für die Textanzeige
        st.markdown("""
            <div class="color-box">
            <h2>Versucht etwas Neues!</h2>
            <p>1. Das erste Asiatisch Restaurant Welches Google vorschlägt</p>
            <p>2. Das erste Italienische Restaurant welches Google vorschlägt</p>
            <p>3. Das erste Afrikanische Restaurant welches Google vorschlägt</p>
           
            </div>
            """, unsafe_allow_html=True)

  
    
