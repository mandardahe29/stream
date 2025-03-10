import streamlit as st
import win32com.client  # Only works locally on Windows with Excel installed

# ---------------------------------------------------------------------------
# 1. Define functions to call each of your VBA macros using win32com
# ---------------------------------------------------------------------------
def run_macro(workbook_path, macro_name):
    """
    Open an Excel workbook and run a specific macro.
    """
    try:
        excel_app = win32com.client.Dispatch("Excel.Application")
        excel_app.Visible = False
        wb = excel_app.Workbooks.Open(workbook_path)
        
        # Run the macro (macro_name must match exactly what’s in the VBA)
        excel_app.Application.Run(macro_name)
        
        # Save and close
        wb.Save()
        wb.Close()
        excel_app.Quit()
        
        st.success(f"Macro '{macro_name}' executed successfully.")
    except Exception as e:
        st.error(f"Error running macro '{macro_name}': {e}")

# ---------------------------------------------------------------------------
# 2. Streamlit Layout
#    We create a layout that resembles your VBA UserForm, but with a modern look.
# ---------------------------------------------------------------------------
st.title("Wheel & Tyre Test Automation")

st.write(
    """
    Use the buttons below to **take inputs** from different sheets or run macros.
    Fill in the form fields as needed, then click "Save Dataset" or "CREATE REPORT PPT".
    """
)

# We'll assume you have a local Excel file that contains all your VBA macros.
# For demonstration, set a placeholder path. Update it to the actual .xlsm file path.
excel_macro_file = r"D:\Report_auto\Report auto.xlsm"

# --- Top Row: 3 Buttons (Take inputs for IMPACT, TFT, Axial) ---
top_col1, top_col2, top_col3 = st.columns(3)

with top_col1:
    if st.button("Take inputs for IMPACT"):
        # Call macro: CopyDataFromSecondaryExcel
        run_macro(excel_macro_file, "CopyDataFromSecondaryExcel")

with top_col2:
    if st.button("Take inputs for TFT sheet"):
        # Call macro: CopyDataFromSecondaryRimApprovalExcel
        run_macro(excel_macro_file, "CopyDataFromSecondaryRimApprovalExcel")

with top_col3:
    if st.button("Take inputs for Axial"):
        # Call macro: CopyDataFromSecondaryAxialLoadExcel
        run_macro(excel_macro_file, "CopyDataFromSecondaryAxialLoadExcel")

# --- Middle Rows: Text inputs and dropdowns ---
st.subheader("Main Form Inputs")
form_col1, form_col2, form_col3, form_col4 = st.columns(4)

with form_col1:
    requested_by = st.selectbox(
        "Requested By",
        ["Aditya Goyal", "Chaitanya ELI", "Paras Trivedi"],
        index=0
    )
    part_no = st.text_input("Part No.")
    
with form_col2:
    test_request_no = st.text_input("Test Request No.")
    front_rear = st.text_input("Front/Rear")
    
with form_col3:
    model = st.text_input("Model")
    # e.g., could be "Impact Test", "Wheel Rim App", "Axial Load"
    test_name = st.selectbox(
        "Test Name",
        ["Impact Test", "Wheel Rim App", "Axial Load"],
        index=0
    )

with form_col4:
    # Additional combos from your code
    # (ComboBox3, ComboBox4, ComboBox5 for concatenating text in TextBox8)
    cbox3 = st.selectbox("Combo 3", ["Nitin Sonewane", "Ajit Chavan", "Anuj", "Niveen", 
                                     "Geetesh Keshwani", "Mandar Dahe", "Nikita", 
                                     "Yogita", "Sahil", "Gaurav"], index=0)
    cbox4 = st.selectbox("Combo 4", ["/Nitin Sonewane", "/Ajit Chavan", "/Anuj", "/Niveen",
                                     "/Geetesh Keshwani", "/Mandar Dahe", "/Nikita",
                                     "/Yogita", "/Sahil", "/Gaurav", " "], index=0)
    cbox5 = st.selectbox("Combo 5", ["/Nitin Sonewane", "/Ajit Chavan", "/Anuj", "/Niveen",
                                     "/Geetesh Keshwani", "/Mandar Dahe", "/Nikita",
                                     "/Yogita", "/Sahil", "/Gaurav", " "], index=0)

# Concatenate combos to simulate the "UpdateTextBox" logic
text_box8_val = f"{cbox3} {cbox4} {cbox5}"



# --- Another Row for Additional Buttons: "Open Test Form" etc. ---
mid_col1, mid_col2, mid_col3 = st.columns(3)

with mid_col1:
    if st.button("Open Test Form"):
        # In VBA, this triggers UserForm2, UserForm3, or UserForm4 depending on the test
        # In Python, you might open a new page, or set a session state variable to show more inputs
        if test_name == "Impact Test":
            run_macro(excel_macro_file, "UserForm2.Show")
        elif test_name == "Wheel Rim App":
            run_macro(excel_macro_file, "UserForm3.Show")
        elif test_name == "Axial Load":
            run_macro(excel_macro_file, "UserForm4.Show")
        else:
            st.warning("Please select a valid Test Name first.")

with mid_col2:
    if st.button("Save Dataset"):
        # In VBA, this calls CommandButton2_Click
        # We can replicate or directly run a macro named "CommandButton2_Click" if you have it
        run_macro(excel_macro_file, "CommandButton2_Click")

with mid_col3:
    if st.button("CREATE REPORT PPT"):
        # In VBA, this calls CommandButton4_Click
        # The macro picks which sub to run based on the test name
        run_macro(excel_macro_file, "CommandButton4_Click")

# ---------------------------------------------------------------------------
# 3. Display any instructions or footers
# ---------------------------------------------------------------------------
st.info(
    """
    **Instructions**  
    1. Click **Take inputs** for each test type to fetch data from a secondary Excel.  
    2. Fill out the main form fields (Part No., Test Request No., etc.).  
    3. Click **Open Test Form** (or the relevant macros) for additional test-specific details.  
    4. Click **Save Dataset** to store your inputs in a new Excel file.  
    5. Finally, click **CREATE REPORT PPT** to generate/update the PowerPoint report.
    """
)
