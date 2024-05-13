import streamlit as st 
import API
import UI


st.set_page_config(page_title="Bite Buddy", layout="wide", initial_sidebar_state="collapsed")

def display_likes():
    # Display liked results
    if 'liked_results' in st.session_state and st.session_state['liked_results']:
        st.write("Liked results:")
        for result in st.session_state['liked_results']:
            st.write(f"**Name:** {result['name']}")
            st.write(f"**Rating:** {result.get('rating', 'N/A')} ⭐")
            st.write(f"**Price:** {result.get('price', 'N/A')}")
            categories = ', '.join([cat['title'] for cat in result.get('categories', [])])
            st.write(f"**Category:** {categories}")
            st.write(f"**Hours:** {result.get('hours', 'Not available')}")
            st.markdown("---")
    else:
        st.write("No results liked yet.")




display_likes()