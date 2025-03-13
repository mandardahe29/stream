import streamlit as st
from common_utils import capture_page, gallery_page
import os
import datetime
from pathlib import Path
import pandas as pd
from openpyxl import Workbook
from openpyxl.drawing.image import Image as OpenpyxlImage


# Helper function to generate Excel file with table data and images.
def save_test_results_to_excel(test_name, table_data, image_folder, output_filename):
    wb = Workbook()
    
    # Create first sheet for table data.
    ws_data = wb.active
    ws_data.title = f"{test_name} Data"
    
    if table_data:
        # Write header row from table_data keys.
        header = list(table_data[0].keys())
        ws_data.append(header)
        # Write each row of data.
        for row in table_data:
            ws_data.append(list(row.values()))
    
    # Create second sheet for images.
    ws_img = wb.create_sheet(title=f"{test_name} Images")
    row_pos = 1  # Starting row for images.
    if os.path.exists(image_folder):
        for file in os.listdir(image_folder):
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                img_path = os.path.join(image_folder, file)
                try:
                    img = OpenpyxlImage(img_path)
                    # Add the image to the sheet at column A.
                    cell_address = f"A{row_pos}"
                    ws_img.add_image(img, cell_address)
                    row_pos += 20  # Adjust spacing for each image.
                except Exception as e:
                    st.error(f"Error adding image {file}: {e}")
    else:
        ws_img.append(["No image folder found"])
    
    # Save the workbook to the given output filename.
    wb.save(output_filename)
    return output_filename

    
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
        column_config={ 
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


    # Section: Save results to Excel.
    st.markdown("### Save Test Results")
    if st.button("Save Test Results to Excel"):
        # Define the folder where images are stored for Impact Test.
        image_folder = "impact_images"
        # Create the folder if it doesn't exist (images would be saved here by your capture code).
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        # Generate an Excel file.
        excel_filename = f"impact_test_results_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        output_file = save_test_results_to_excel("Impact Test", st.session_state["impact_table_data"], image_folder, excel_filename)
        # Provide a download button for the generated Excel file.
        with open(output_file, "rb") as f:
            st.download_button("Download Excel File", f, file_name=excel_filename)
        st.success("Test results saved and ready for download.")
    # Display the table data for debugging (optional)
    #st.write("Current Table Data:", st.session_state["impact_table_data"])

    nav_options = ["Capture", "Gallery"]
    selection = st.radio("Navigation", nav_options, horizontal=True)

    if selection == "Capture":
        capture_page("impact_images")
    else:
        gallery_page("impact_images")

