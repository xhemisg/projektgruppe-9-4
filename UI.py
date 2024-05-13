import streamlit as st
import app

@st.experimental_fragment
def restaurant_data_display(restaurant_data):
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
                st.write(f"**Rating:** {restaurant.get('rating', 'N/A')} ⭐")
                st.write(f"**Price:** {restaurant.get('price', 'N/A')}")
                categories = ', '.join([cat['title'] for cat in restaurant.get('categories', [])])
                st.write(f"**Category:** {categories}")
                st.write(f"**Hours:** {restaurant.get('hours', 'Not available')}")

                # Checkbox for liking the restaurant, linked directly to its 'liked' property
                liked_key = f"liked_{idx}"
                restaurant['liked'] = st.checkbox("Like", key=liked_key, value=restaurant['liked'])

        # Submit button for the form
        submitted = st.form_submit_button("Submit Likes")
    
    if submitted:
        # Append new likes to existing liked results or create new if not present
        new_likes = [restaurant for restaurant in restaurant_data if restaurant.get('liked')]
        if 'liked_results' in st.session_state:
            st.session_state['liked_results'] += new_likes  # Append new likes
        else:
            st.session_state['liked_results'] = new_likes  # Initialize if not already present

        st.success("Likes processed successfully!")
        



   
    
