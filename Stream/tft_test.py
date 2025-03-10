import streamlit as st
from common_utils import capture_page, gallery_page

def tft_test_page():
    st.header("TFT Test")

    nav_options = ["Capture", "Gallery"]
    selection = st.radio("Navigation", nav_options, horizontal=True)

    if selection == "Capture":
        capture_page("tft_images")
    else:
        gallery_page("tft_images")
