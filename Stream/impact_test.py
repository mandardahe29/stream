import streamlit as st
from common_utils import capture_page, gallery_page

def impact_test_page():
    st.header("Impact Test")

    # Optional headings above the table
    st.markdown("""
    **Before test run out measurement**  
    FRONT WHEEL RIM  

    **Specification**: Run out = 0.5 max
    """)

    # 1) Editable label (e.g., "Endurance")
    if "endurance_label" not in st.session_state:
        st.session_state["endurance_label"] = "Endurance"
    st.session_state["endurance_label"] = st.text_input(
        "Test Label:", 
        value=st.session_state["endurance_label"]
    )

    st.markdown(f"### {st.session_state['endurance_label']}")

    # 2) Initialize table data in session_state if it doesn't exist
    if "impact_table_data" not in st.session_state:
        st.session_state["impact_table_data"] = [
            {
                "Sample No": "S1_200",
                "Axial (Disc Side)": "",
                "Axial (Opposite Side)": "",
                "Radial (Disc Side)": "",
                "Radial (Opposite Side)": ""
            },
            {
                "Sample No": "S2_200",
                "Axial (Disc Side)": "",
                "Axial (Opposite Side)": "",
                "Radial (Disc Side)": "",
                "Radial (Opposite Side)": ""
            },
            # Add more default rows if you want:
            # {
            #     "Sample No": "S3_400",
            #     "Axial (Disc Side)": "",
            #     "Axial (Opposite Side)": "",
            #     "Radial (Disc Side)": "",
            #     "Radial (Opposite Side)": ""
            # },
            # {
            #     "Sample No": "S4_400",
            #     "Axial (Disc Side)": "",
            #     "Axial (Opposite Side)": "",
            #     "Radial (Disc Side)": "",
            #     "Radial (Opposite Side)": ""
            # },
        ]

    # 3) Show the editable table (data_editor)
    edited_data = st.data_editor(
        st.session_state["impact_table_data"],
        key="impact_editor",
        column_config={  # ✅ Correct way
            "Sample No": st.column_config.TextColumn("Sample No"),
            "Axial Run Out (Disc Side)": st.column_config.NumberColumn("Axial Run Out (Disc Side)"),
            "Axial Run Out (Opposite Side)": st.column_config.NumberColumn("Axial Run Out (Opposite Side)"),
            "Radial (Disc Side)": st.column_config.NumberColumn("Radial (Disc Side)"),
            "Radial (Opposite Side)": st.column_config.NumberColumn("Radial (Opposite Side)")
        }
    )

    # Update session_state with any user edits
    st.session_state["impact_table_data"] = edited_data

    # 4) Button to add a new row
    if st.button("Add New Row"):
        next_idx = len(st.session_state["impact_table_data"]) + 1
        new_row = {
            "Sample No": f"S{next_idx}_200",
            "Axial (Disc Side)": "",
            "Axial (Opposite Side)": "",
            "Radial (Disc Side)": "",
            "Radial (Opposite Side)": ""
        }
        st.session_state["impact_table_data"].append(new_row)

    # Display the table data for debugging (optional)
    st.write("Current Table Data:", st.session_state["impact_table_data"])

    nav_options = ["Capture", "Gallery"]
    selection = st.radio("Navigation", nav_options, horizontal=True)

    if selection == "Capture":
        capture_page("impact_images")
    else:
        gallery_page("impact_images")

