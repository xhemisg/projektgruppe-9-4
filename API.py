
# Funktion, um Daten von der Yelp API zu erhalten
import requests
import streamlit as st

def get_restaurant_data(location, price, categories):
    api_key = 'AIzaSyAEKMkNu-Q-sq9d2FkhED6cvBiR9Z74Yx8'
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    # Ensure categories is a list and is not empty before joining
    if categories and isinstance(categories, list):
        category_str = ','.join(categories)
    else:
        category_str = ''  # Default to an empty string if categories is None or not a list

    params = {
        'location': location,
        'radius': 5000,
        'type': 'restaurant',
        'keyword': category_str,  # Use the safe category string
        'minprice': price,
        'key': api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an error for bad requests
        restaurant_data = response.json()
        restaurants = restaurant_data.get('results', [])
        return restaurants  # Return the list of restaurants

    except requests.RequestException as e:
        st.error(f"API request error: {e}")
        return None