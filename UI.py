import streamlit as st

import app



##hier wird das Layout der Ausgabe bestimmt
def restaurant_data_display(restaurant_data, fav_restaurants):
    if not restaurant_data:
        #ein error bzw abruch des Systems wird vermiden, indem ein eigener Error eigefügt wird 
        st.error("No data available.")
        return
    #zugriff auf die API über restaurant_data mit einem for-loop 
    for restaurant in restaurant_data:
        
        col1, col2 = st.columns([1, 2]) 
        
        #In Spalte eins der Tabelle wird hier das Bild des Restaurants ausgegeben, welches einen kurzen Eindruck von diesem gibt 
        with col1:
            if restaurant['image_url']:
                #hier wird das Bild genauer beschrieben damit die Ausgabe der Bilder alle gleich ist
                st.image(restaurant['image_url'], width=300, use_column_width=True)
            
            #wenn kein Bild vorhanden ist soll es anzeigen, dass kein Bild Vorhanden ist 
            else:
                st.write("No image available.")

        #in der zweiten Spalte werden die Kriterien die oben ausgewählt wurden dargestellt sowie die klassischen Informationen über ein Restaurant gegeben 
        with col2:
            st.write(f"**Name:** {restaurant['name']}")#hier wird der Name des Restaurants ausgegeben 
            st.write(f"**Rating:** {restaurant.get('rating', 'N/A')} ⭐")#hier wird das Rating dargestellt in Sternen und als Gleitkommazahlen 
            st.write(f"**Preis:** {restaurant.get('price', 'N/A')}")#der Preis wird mit Dollarzeichen dargestellt von 1-4 Dollarzeichen 
            categories = ', '.join([cat['title'] for cat in restaurant.get('categories', [])])# hier wird die Kategorie des Restaurants benannt 
            st.write(f"**Kategorie:** {categories}")
            st.write(f"**Öffnungszeiten:** {restaurant.get('hours', 'Not available')}")#hier werden die Öffnungszeiten des Restaurants benannt 
        
        #hier wird der Like-Button am ende der Beschreibung eingeführt     
            if st.button(f"Like {restaurant['name']}"): #wenn der Like-Button gedrückt wird, wird das restaurant der Liste der fav_restaurants hinzugefügt 
                restaurant['liked'] = True
                fav_restaurants.append(restaurant)

##Übersichtliche gestaltung 
    #Trennlinien zwischen den einzelnen Ausgaben 
        st.markdown("---") 

    #Abstände zwischen den einzelnen Ausgaben 
        st.write("")
        
##Die erstellung der Favoriten 
    #hier wird die Applikation Favoriten erstellt 
def show_favourites(fav_restaurants):

    #wenn es noch keien Favoriten gibt wird folgendes zurückgegeben 
    if not fav_restaurants:
        st.write("Du hast noch keine Restaurants geliked")
    
    #wenn es schon Favoriten gibt wird Folgendes zurückgegeben 
    else:
        st.write("Deine lieblings Restaurants")
        for restaurant in fav_restaurants:
            col1, col2 = st.columns([1, 2])  #hier wird wieder eine Tabelle erstellt wie schon im oberen Teil mit den selben Inhalten --> Erklärung siehe erster Teil 

        
        with col1:
            if restaurant['image_url']:
                st.image(restaurant['image_url'], width=300, use_column_width=True)
            else:
                st.write("No image available.")

        
        with col2:
            st.write(f"**Name:** {restaurant['name']}")
            st.write(f"**Rating:** {restaurant.get('rating', 'N/A')} ⭐")
            st.write(f"**Preis:** {restaurant.get('price', 'N/A')}")
            categories = ', '.join([cat['title'] for cat in restaurant.get('categories', [])])
            st.write(f"**Kategorie:** {categories}")
            st.write(f"**Öffnungszeiten:** {restaurant.get('hours', 'Not available')}")
            
        st.markdown("---")
        st.write("")   # Leerzeile nach jedem Restaurant
        
        
        
'''if 'liked_restaurants' not in st.session_state:
    st.session_state.liked_restaurants = []

def restaurant_data_display(restaurant_data):
    if not restaurant_data:
        st.error("No data available.")
        return

    for restaurant in restaurant_data:
        # Create a row with two columns: one for the image and one for details
        col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed for visual balance

        # Column for the image
        with col1:
            if restaurant['image_url']:
                st.image(restaurant['image_url'], width=300, use_column_width=True)
            else:
                st.write("No image available.")

        # Column for the restaurant details
        with col2:
            st.write(f"**Name:** {restaurant['name']}")
            st.write(f"**Rating:** {restaurant.get('rating', 'N/A')} ⭐")
            st.write(f"**Preis:** {restaurant.get('price', 'N/A')}")
            categories = ', '.join([cat['title'] for cat in restaurant.get('categories', [])])
            st.write(f"**Kategorie:** {categories}")
            st.write(f"**Öffnungszeiten:** {restaurant.get('hours', 'Not available')}")
            if st.button(f"Like {restaurant['name']}"):
                restaurant['liked'] = True
                st.session_state.liked_restaurants.append(restaurant)  # Add the liked restaurant to session state

        # Add a horizontal line and some space after each restaurant
        st.markdown("---")
        st.write("")  # Adding a little extra space after the separator

def show_favourites():
    if st.session_state.liked_restaurants:
        st.write("Your liked restaurants:")
        for restaurant in st.session_state.liked_restaurants:
            st.write(f"- {restaurant['name']}")

'''
        
        
"""def show_restaurant(index, restaurants):
    if restaurants:
        restaurant = restaurants[index]
        st.subheader(f"{restaurant['name']} - {restaurant.get('rating', 'No rating available')}")
        categories = ", ".join([cat['title'] for cat in restaurant.get('categories', [])])
        st.write(f"Categories: {categories if categories else 'Not available'}")
        st.write(f"Price range: {restaurant.get('price', 'Not available')}")
        if restaurant.get('image_url'):
            st.image(restaurant['image_url'], caption=restaurant['name'])
        else:
            st.write("No image available for this restaurant.")
        st.write(f"**Open:** {'Yes' if not restaurant.get('is_closed', True) else 'No'}")
        if 'hours' in restaurant:
            st.write(f"**Hours:** {restaurant['hours'][0]['open']}")
        else:
            st.write("Hours not available")
        business_details = get_business_details(restaurant['id'], api_key)
        if business_details and 'hours' in business_details:
            st.write(f"**Detailed hours:** {business_details['hours']}")
"""
        

            
    