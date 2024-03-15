import streamlit as st

st.set_page_config(
    page_title="TA Chatbot",
    page_icon="🤖",)

st.title("Main Page")

# Add "Talent Analytics Chatbot" as content
st.header("Talent Analytics Chatbot")
st.write("Welcome to the Talent Analytics Chatbot. Here, you can interact with our chatbot to get insights on your data.")

# Add a sidebar with a selectbox
# selected_page = st.sidebar.selectbox("Select a page", ["Page 1", "Page 2", "Page 3"])

# Show a message based on the selected pa

# Get the path to the folder containing the files
folder_path = "/Pages"

# List all files in the folder
files = os.listdir(folder_path)

# Display the selectbox with file names as options
selected_file = st.sidebar.selectbox("Select a file", files)

# Add your code to handle the selected file here
