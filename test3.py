import streamlit as st
import requests

# Funktion, um Daten von der Yelp API zu erhalten
def get_restaurant_data(location, min_rating):
    api_key = 'GjgxNlVcPtkDQOJsW9oZoSS0jjn74Yb6i3qoEoPxTu4ylG59rSNTvwVfA9knU42IaCSl1qIoIU0tGdnD-OJCPAFHNc_KvwjXF4pZhXw6RCZ4_hJfD6dz2fxYPawmZnYx'
    headers = {'Authorization': f'Bearer {api_key}'}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'location': location,
        'limit': 10,
        'rating': min_rating  # Mindestbewertungsparameter
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Fehler werfen, wenn die Anfrage fehlschlägt
        data = response.json()
        return data['businesses']  # Nur die Liste der Restaurants zurückgeben

    except requests.RequestException as e:
        st.error(f"API request error: {e}")
        return None

# Streamlit App
st.title('Restaurant Finder')
location = st.text_input('Enter a location to search for restaurants:')
min_rating = st.slider('Select minimum rating:', 1.0, 5.0, step=0.1)

if st.button('Search'):
    if min_rating > 1.0:  # Nur suchen, wenn das Mindestrating größer als 1.0 ist
        restaurant_data = get_restaurant_data(location, min_rating)

        if restaurant_data:
            filtered_restaurants = [restaurant for restaurant in restaurant_data if restaurant['rating'] >= min_rating]

            if filtered_restaurants:
                for restaurant in filtered_restaurants:
                    st.subheader(restaurant['name'])
                    st.write(f"Rating: {restaurant['rating']} ⭐")
                    st.write(f"Address: {', '.join(restaurant['location']['display_address'])}")
                    if 'image_url' in restaurant and restaurant['image_url']:
                        st.image(restaurant['image_url'], caption='Restaurant Image')
                    else:
                        st.warning("No image available for this restaurant.")
            else:
                st.warning(f"No restaurants found with a rating of {min_rating} or higher.")
        else:
            st.warning("No restaurants found. Please check your location and try again.")
    else:
        st.warning("Please select a minimum rating greater than 1.0.")