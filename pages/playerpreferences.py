import streamlit as st 
import API
import UI

st.set_page_config(page_title="Bite Buddy", layout="wide", initial_sidebar_state="collapsed")

if 'current_index' not in st.session_state:
    st.session_state['current_index'] = 0

current_player = st.session_state['names'][st.session_state['current_index']]

st.title(f"{current_player}, bitte deine Präferenzen!")



location = st.session_state.get('location', "Zürich")


categories = st.multiselect("Welche Küche bevorzugst du", ["newamerican", "italian", "swissfood", "chineese", "mexican" ])
price = st.slider("Select a budget", 1, 4, 3 )
min_rating = st.slider("Select a minimum rating", 1.0, 5.0, 3.0, step =0.1)





if st.button("Finde mein Restaurant"):
    restaurant_data = API.get_restaurant_data(location, categories, price, min_rating)
    UI.restaurant_data_display(restaurant_data)
   
if st.button("Next Player"):
    if st.session_state['current_index'] < len(st.session_state['names']) - 1:
        st.session_state['current_index'] += 1
    else:
        st.session_state['current_index'] = 0  # Reset or move to a summary page
    st.experimental_rerun()  
