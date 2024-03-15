import streamlit as st
import os

# Get the path to the folder containing the files
folder_path = "/Pages"

# List all files in the folder
files = os.listdir(folder_path)

# Display the selectbox with file names as options
selected_file = st.sidebar.selectbox("Select a file", files)

# Add your code to handle the selected file here
