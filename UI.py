import streamlit as st

import app



##hier wird das Layout der Ausgabe bestimmt
def restaurant_data_display(restaurant_data, fav_restaurants):
    if not restaurant_data:
        #ein error bzw abruch des Systems wird vermiden, indem ein eigener Error eigefügt wird 
        st.error("No data available.")
        return

    for restaurant in restaurant_data:
        
        col1, col2 = st.columns([1, 2]) 
        
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
            if st.button(f"Like {restaurant['name']}"):
                restaurant['liked'] = True
                fav_restaurants.append(restaurant)

       
        st.markdown("---")
 
        st.write("")
        
       
def show_favourites(fav_restaurants):
    if not fav_restaurants:
        st.write("Du hast noch keine Restaurants geliked")
    else:
        st.write("Deine lieblings Restaurants")
        for restaurant in fav_restaurants:
            col1, col2 = st.columns([1, 2])  

        
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
        st.write("")
        
        
        
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
        

            
    