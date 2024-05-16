import streamlit as st
import requests
import datetime
import pytz
import UI
import app

# Funktion, um Daten von der Yelp API zu erhalten
def get_restaurant_data(location,open_at, categories, min_rating, price, limit):
    api_key = 'gPtjGrH3r9Me-BwkN7X-beLbp61tSEpx7TTMFyJm2TviEPqkHZryUJM5z763-lilKTr6yCwjXhBR5-VlNvVjZP5f7Qug24u1L_EPVF574oGk_YnCCjlQ3fbv3S9GZnYx'
    headers = {
    'Authorization': f'Bearer {api_key}',
    'User-Agent': 'StudentProjectHSG'
    }
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'location': location,
        'limit': limit,
        'categories': categories,
        'rating': price,# Mindestbewertungsparameter
        'price': min_rating,
        'open_at' : open_at

    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Fehler werfen, wenn die Anfrage fehlschlägt
        restaurant_data = response.json()
        print("Response Data: ", response.json()) 
        return restaurant_data['businesses']  # Nur die Liste der Restaurants zurückgeben

    except requests.RequestException as e:
        st.error(f"API request error: {e}")
        return None
    
    
