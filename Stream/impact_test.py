import streamlit as st
from common_utils import capture_page, gallery_page

def impact_test_page():
    st.header("Impact Test")
    
    st.markdown("""
    **Before test run out measurement**  
    **FRONT WHEEL RIM**  

    **Specification**: Run out = 0.5 max
    """)

    # Keep our editable table in session_state
    if "impact_table_data" not in st.session_state:
        # Initialize with some rows matching your screenshot
        st.session_state["impact_table_data"] = [
            {
                "Make": "Endurance",
                "Sample No": "S1_200",
                "Axial (Disc Side)": "0.17",
                "Axial (Opposite Side)": "0.31",
                "Radial (Disc Side)": "0.08",
                "Radial (Opposite Side)": "0.16"
            },
            {
                "Make": "Endurance",
                "Sample No": "S2_200",
                "Axial (Disc Side)": "0.13",
                "Axial (Opposite Side)": "0.35",
                "Radial (Disc Side)": "0.01",
                "Radial (Opposite Side)": "0.15"
            },
            {
                "Make": "Endurance",
                "Sample No": "S3_400",
                "Axial (Disc Side)": "0.20",
                "Axial (Opposite Side)": "0.30",
                "Radial (Disc Side)": "0.12",
                "Radial (Opposite Side)": "0.16"
            },
            {
                "Make": "Endurance",
                "Sample No": "S4_400",
                "Axial (Disc Side)": "0.15",
                "Axial (Opposite Side)": "0.39",
                "Radial (Disc Side)": "0.06",
                "Radial (Opposite Side)": "0.19"
            },
        ]
    
    # We also keep a counter to help generate new rows like S5_200, S6_200, etc.
    if "impact_sample_counter" not in st.session_state:
        st.session_state["impact_sample_counter"] = 5  # next row will be S5_200

    # Display the data_editor for the table
    edited_data = st.data_editor(
        st.session_state["impact_table_data"],
        key="impact_data_editor",
        columns={
            "Make": "Make",
            "Sample No": "Sample No",
            "Axial (Disc Side)": "Axial (Disc Side)",
            "Axial (Opposite Side)": "Axial (Opposite Side)",
            "Radial (Disc Side)": "Radial (Disc Side)",
            "Radial (Opposite Side)": "Radial (Opposite Side)",
        },
    )
    # Save any edits back to session_state
    st.session_state["impact_table_data"] = edited_data

    # Button to add a new row
    if st.button("Add New Row"):
        new_sample_no = f"S{st.session_state['impact_sample_counter']}_200"
        st.session_state["impact_sample_counter"] += 1
        new_row = {
            "Make": "Endurance",  # or you can leave blank
            "Sample No": new_sample_no,
            "Axial (Disc Side)": "",
            "Axial (Opposite Side)": "",
            "Radial (Disc Side)": "",
            "Radial (Opposite Side)": ""
        }
        st.session_state["impact_table_data"].append(new_row)
        # Re-run to update table display
        st.experimental_rerun()
    
    # Debug / display final data
    st.write("**Current Table Data:**", st.session_state["impact_table_data"])

    nav_options = ["Capture", "Gallery"]
    selection = st.radio("Navigation", nav_options, horizontal=True)
    
     if selection == "Capture":
        capture_page("impact_images")
     else:
        gallery_page("impact_images")


