import streamlit as st

# Define functions for the menu options
def file_menu():
    st.sidebar.write("File Menu Selected")
    file_action = st.sidebar.selectbox("Choose Action", ["Open", "Close"])
    if file_action == "Open":
        st.write("Opening File...")
    elif file_action == "Close":
        st.write("Closing File...")

def view_menu():
    st.sidebar.write("View Menu Selected")
    view_action = st.sidebar.selectbox("Choose Action", ["View File", "Print File"])
    if view_action == "View File":
        st.write("Viewing File...")
    elif view_action == "Print File":
        st.write("Printing File...")

def save_menu():
    st.sidebar.write("Save Menu Selected")
    save_action = st.sidebar.selectbox("Choose Action", ["Save File", "Save As"])
    if save_action == "Save File":
        st.write("Saving File...")
    elif save_action == "Save As":
        st.write("Saving File As...")

def table_menu():
    st.sidebar.write("Table Menu Selected")
    table_action = st.sidebar.selectbox("Choose Action", ["Table One", "Table Two"])
    if table_action == "Table One":
        st.write("Table One Content")
        st.table({"Column A": [1, 2, 3], "Column B": [4, 5, 6]})
    elif table_action == "Table Two":
        st.write("Table Two Content")
        st.table({"Column X": [7, 8, 9], "Column Y": [10, 11, 12]})

def log_menu():
    st.sidebar.write("Log Menu Selected")
    log_action = st.sidebar.selectbox("Choose Action", ["Log In", "Log Off"])
    if log_action == "Log In":
        st.write("Logging In...")
    elif log_action == "Log Off":
        st.write("Logging Off...")

# Main Streamlit App
st.title("Streamlit Dropdown Menu Example")
st.sidebar.title("Menu")

menu = st.sidebar.selectbox("Choose Menu", ["File", "View", "Save", "Table", "Log"])

# Display the selected menu
if menu == "File":
    file_menu()
elif menu == "View":
    view_menu()
elif menu == "Save":
    save_menu()
elif menu == "Table":
    table_menu()
elif menu == "Log":
    log_menu()