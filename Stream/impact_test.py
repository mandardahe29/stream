import streamlit as st
from common_utils import capture_page, gallery_page

def impact_test_page():
    st.header("Impact Test")

    nav_options = ["Capture", "Gallery"]
    selection = st.radio("Navigation", nav_options, horizontal=True)

    if selection == "Capture":
        # Save images to a folder named 'impact_images' (for example)
        capture_page("impact_images")
    else:
        gallery_page("impact_images")
