import streamlit as st
from common_utils import capture_page, gallery_page

def axial_test_page():
    st.header("Axial Test")

    nav_options = ["Capture", "Gallery"]
    selection = st.radio("Navigation", nav_options, horizontal=True)

    if selection == "Capture":
        capture_page("axial_images")
    else:
        gallery_page("axial_images")
