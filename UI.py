import streamlit as st
import app

@st.experimental_fragment
def restaurant_data_display(restaurant_data, current_player):
    if not restaurant_data:
        st.error("No data available.")
        return

    if 'liked_results' not in st.session_state:
        st.session_state['liked_results'] = []

    # Initialize or update 'liked' property in restaurant data if needed
    for restaurant in restaurant_data:
        if 'liked' not in restaurant:
            restaurant['liked'] = False

    with st.form("like_form"):
        for idx, restaurant in enumerate(restaurant_data):
            col1, col2 = st.columns([1, 2])

            with col1:
                if 'image_url' in restaurant and restaurant['image_url']:
                    st.image(restaurant['image_url'], width=300, use_column_width=True)
                else:
                    st.write("No image available.")

            with col2:
                st.write(f"**Name:** {restaurant['name']}")
                st.write(f"**Bewertungg:** {restaurant.get('rating', 'N/A')} ⭐")
                st.write(f"**Preis:** {restaurant.get('price', 'N/A')}")
                categories = ', '.join([cat['title'] for cat in restaurant.get('categories', [])])
                st.write(f"**Küche:** {categories}")
                st.write(f"**Adresse:** {restaurant.get('address', 'N/A')}")
                st.write(f"**Website:** {restaurant.get('website', 'N/A')}")
                st.write(f"**")

                # Checkbox for liking the restaurant, linked directly to its 'liked' property
                liked_key = f"liked_{idx}"
                restaurant['liked'] = st.checkbox("Like", key=liked_key, value=restaurant.get('liked', False))


        # Submit button for the form
        submitted = st.form_submit_button("Submit Likes")
    
    
    if submitted:
        current_likes = set(restaurant['id'] for restaurant in restaurant_data if restaurant.get('liked'))
        st.session_state['liked_results'] = [restaurant for restaurant in restaurant_data if restaurant['id'] in current_likes]

        st.success("Likes updated successfully!")







def display_final_likes():
    if 'player_likes' not in st.session_state:
        st.write("No likes found.")
        return

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
        st.write("Restaurants liked by all participants:")
        for restaurant in liked_by_all:
            st.write(f"**Name:** {restaurant['name']}")
            st.write(f"**Bewertung:** {restaurant.get('rating')} ⭐")
            st.write(f"**Preis:** {restaurant.get('price')}")
            st.write(f"**Küche:** {', '.join([cat['title'] for cat in restaurant.get('categories', [])])}")
            st.write(f"**Adresse:** {restaurant.get('location', {}).get('address1', 'N/A')}")
            st.markdown("---")
    else:
        st.write("No restaurants liked by all participants.")

  
    
