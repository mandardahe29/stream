import streamlit as st
from impact_test import impact_test_page
from cft_test import cft_test_page
from tft_test import tft_test_page
from rdt_test import rdt_test_page
from axial_test import axial_test_page

def main():
 st.write(f"Streamlit Version: {st.__version__}")  
 st.title("Test Selection")

    test_options = [
        "Impact Test",
        "CFT Test",
        "TFT Test",
        "RDT Test",
        "Axial Test"
    ]
    choice = st.selectbox("Select a test:", test_options)

    if choice == "Impact Test":
        impact_test_page()
    elif choice == "CFT Test":
        cft_test_page()
    elif choice == "TFT Test":
        tft_test_page()
    elif choice == "RDT Test":
        rdt_test_page()
    elif choice == "Axial Test":
        axial_test_page()

if __name__ == '__main__':
    main()
