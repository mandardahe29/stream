# main_app.py
import streamlit as st
from impact_test import impact_test_page

# Add imports for other test pages when they're ready

def main():
    st.set_page_config(page_title="Wheel Testing App", layout="wide")
    st.sidebar.title("Test Menu")
    
    test_choice = st.sidebar.radio("Select Test Type", [
        "Impact Test",
        # "CFT Test",
        # "RDT Test",
        # "Axial Test",
        # "RDT Repeated Test"
    ])

    if test_choice == "Impact Test":
        impact_test_page()

if __name__ == "__main__":
    main()
