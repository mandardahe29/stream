import streamlit as st
from common_utils import capture_page, gallery_page

def cft_test_page():
    st.header("CFT Test")

    nav_options = ["Capture", "Gallery"]
    selection = st.radio("Navigation", nav_options, horizontal=True)

    if selection == "Capture":
        capture_page("cft_images")
    else:
        gallery_page("cft_images")
