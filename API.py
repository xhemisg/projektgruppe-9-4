import streamlit as st
import requests
import datetime
import pytz
import UI
import app 

# Funktion, um Daten von der Yelp API zu erhalten
def get_restaurant_data(location, min_rating, price, categories):
    api_key = 'GjgxNlVcPtkDQOJsW9oZoSS0jjn74Yb6i3qoEoPxTu4ylG59rSNTvwVfA9knU42IaCSl1qIoIU0tGdnD-OJCPAFHNc_KvwjXF4pZhXw6RCZ4_hJfD6dz2fxYPawmZnYx'
    headers = {'Authorization': f'Bearer {api_key}'}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'location': location,
        'limit': 10,
        'rating': min_rating,# Mindestbewertungsparameter
        'categories': categories,
        'price': str(price)

    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Fehler werfen, wenn die Anfrage fehlschlägt
        restaurant_data = response.json()
        return restaurant_data['businesses']  # Nur die Liste der Restaurants zurückgeben

    except requests.RequestException as e:
        st.error(f"API request error: {e}")
        return None
    
    
'''def get_business_details(business_id, api_key):
    """Fetch detailed business data including hours of operation."""
    details_url = f'https://api.yelp.com/v3/businesses/{business_id}'
    headers = {'Authorization': f'Bearer {api_key}'}
    try:
        response = requests.get(details_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Failed to fetch business details: {e}")
        return None


    
    
    
def is_business_open_now(hours):
    # Get current time and day
    timezone = pytz.timezone(hours[0]['hours_type'])  # assuming the API returns timezone
    now = datetime.datetime.now(timezone)
    current_day = now.weekday()  # Monday is 0 and Sunday is 6
    current_time = now.strftime('%H%M')

    # Check current day and time against the business hours
    for day in hours[0]['open']:
        if int(day['day']) == current_day:
            start_time = int(day['start'])
            end_time = int(day['end'])
            if start_time <= int(current_time) <= end_time:
                return "Open now"
            else:
                return f"Closed, opens next at {day['start'][:2]}:{day['start'][2:]}"
    return "Closed today"

def add_open_status(businesses, api_key):
    """Add open status to each business based on current time and business hours."""
    for business in businesses:
        details = get_business_details(business['id'], api_key)
        if 'hours' in details:
            business['open_now'], business['next_open_time'] = is_business_open_now(details['hours'])
        else:
            business['open_now'] = "Hours not available"
    return businesses
    '''
    




