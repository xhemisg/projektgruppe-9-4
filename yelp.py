import streamlit as st
import requests

st.title('Restaurant Finder') #wie es in streamlit ausschaut
location = st.text_input('Enter a location to search for restaurants:')
rating = st.slider('Select minimum rating:', 1.0, 5.0, step=0.5)
st.button('Search')
    

def get_restaurant_data(location,min_rating): #funktion definiert um daten von API zu erhalten
    api_key = 'GjgxNlVcPtkDQOJsW9oZoSS0jjn74Yb6i3qoEoPxTu4ylG59rSNTvwVfA9knU42IaCSl1qIoIU0tGdnD-OJCPAFHNc_KvwjXF4pZhXw6RCZ4_hJfD6dz2fxYPawmZnYx'  # Replace this with your actual Yelp API key
    headers = {'Authorization': f'Bearer {api_key}'}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'location': location,
        'limit': 10,
        'rating': min_rating}  # You can customize parameters as needed
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data


def filter_by_rating(businesses, min_rating):
    return [biz for biz in businesses if biz['rating'] >= min_rating]

# In your main code
restaurant_data = get_restaurant_data(location)
filtered_restaurants = filter_by_rating(restaurant_data['businesses'], rating)
for restaurant in filtered_restaurants:
    # Display each restaurant





    restaurant_data = get_restaurant_data(location)
    for restaurant in restaurant_data['businesses']:
        st.subheader(restaurant['name'])
        st.write(f"Rating: {restaurant['rating']} ⭐")
        st.write(f"Address: {', '.join(restaurant['location']['display_address'])}")
        # Display image if available
        if 'image_url' in restaurant and restaurant['image_url']:
            st.image(restaurant['image_url'], caption='Restaurant Image')
else:
    st.error("No restaurant data found. Please check the API call and response.")