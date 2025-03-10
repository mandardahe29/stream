import streamlit as st
from common_utils import capture_page, gallery_page

def rdt_test_page():
    st.header("RDT Test")

    nav_options = ["Capture", "Gallery"]
    selection = st.radio("Navigation", nav_options, horizontal=True)

    if selection == "Capture":
        capture_page("rdt_images")
    else:
        gallery_page("rdt_images")
