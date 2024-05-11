import streamlit as st

import app
import API


def restaurant_data_display(restaurant_data, fav_restaurants):
    if restaurant_data:
        for restaurant in restaurant_data:
            place_id = restaurant['place_id']
            details_url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key=YOUR_GOOGLE_PLACES_API_KEY'
            details_response = requests.get(details_url)
            details = details_response.json()

            if 'result' in details:
                result = details['result']
                place_name = result['name']
                place_address = result['formatted_address']
                place_rating = result['rating']
                place_open_now = result['opening_hours']['open_now']
                place_open_hours = result['opening_hours']['weekday_text']
                place_cuisine = result['types']
                place_image = result['photos'][0]['html_attributions'][0] if 'photos' in result else None

                st.subheader(place_name)
                st.write(f"Address: {place_address}")
                st.write(f"Rating: {place_rating}")
                st.write(f"Open now: {place_open_now}")
                st.write(f"Opening hours: {place_open_hours}")
                st.write(f"Cuisine: {place_cuisine}")
                st.image(place_image, caption=f"Image of {place_name}")

                if st.button("Add to favorites"):
                    fav_restaurants.append(restaurant)
                    st.success("Restaurant added to favorites")
    else:
        st.warning("No restaurants found")

# ui.py
"""def restaurant_data_display(restaurants, fav_restaurants):
    if not restaurants:
        st.error("No data available.")
        return

    for restaurant in restaurants:
        col1, col2 = st.columns([1, 2])

        with col1:
            # Check if photos are available and construct image URL
            if 'photos' in restaurant and len(restaurant['photos']) > 0:
                photo_reference = restaurant['photos'][0]['photo_reference']
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key=YOUR_API_KEY"
                st.image(photo_url, width=300, use_column_width=True)
            else:
                st.write("No image available.")

        with col2:
            st.write(f"**Name:** {restaurant['name']}")
            st.write(f"**Rating:** {restaurant.get('rating', 'N/A')} ⭐")
            st.write(f"**Price Level:** {restaurant.get('price_level', 'N/A')}")
            st.write(f"**Address:** {restaurant.get('vicinity', 'N/A')}")
            if st.button(f"Like {restaurant['name']}"):
                restaurant['liked'] = True
                fav_restaurants.append(restaurant)

        st.markdown("---")

"""
        
        
        
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
        

            
    