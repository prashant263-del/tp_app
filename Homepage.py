import os
import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="TA Chatbot",
    page_icon="🤖",
)

# Define the paths to your pages
page_dir = "Pages"
page_files = os.listdir(page_dir)
page_paths = {file[:-3]: os.path.join(page_dir, file) for file in page_files if file.endswith(".py")}

# Display the title and header
st.title("Main Page")
st.header("Talent Analytics Chatbot")
st.write("Welcome to the Talent Analytics Chatbot. Here, you can interact with our chatbot to get insights on your data.")

# Add a sidebar with a selectbox for selecting pages
selected_page = st.sidebar.selectbox("Select a page", list(page_paths.keys()))

# Load and run the selected page
if selected_page in page_paths:
    with open(page_paths[selected_page], "r") as f:
        exec(f.read())
else:
    st.write("Page not found.")
