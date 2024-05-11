
# Funktion, um Daten von der Yelp API zu erhalten
import requests
import streamlit as st

   
def get_restaurant_data(city_name, min_rating, price, categories):
    api_key = 'AIzaSyAEKMkNu-Q-sq9d2FkhED6cvBiR9Z74Yx8'
    geocoding_url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city_name}&key={api_key}'
    geocoding_response = requests.get(geocoding_url)
    geocoding_data = geocoding_response.json()
    lat = geocoding_data['results'][0]['geometry']['location']['lat']
    lng = geocoding_data['results'][0]['geometry']['location']['lng']
    params = {
        'location': f'{lat},{lng}',
        'radius': 5000,
        'type': 'estaurant',
        'keyword': categories,
        'inprice': price,
        'opennow': True,
        'key': api_key
    }
    try:
        response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json', params=params)
        response.raise_for_status()
        restaurant_data = response.json()
        restaurants = restaurant_data.get('results', [])
        return restaurants
    except requests.RequestException as e:
        st.error(f"API request error: {e}")
        return None