import streamlit as st

st.set_page_config(
    page_title="TA Chatbot",
    page_icon="🤖",)

st.title("Main Page")

# Add "Talent Analytics Chatbot" as content
st.header("Talent Analytics Chatbot")
st.write("Welcome to the Talent Analytics Chatbot. Here, you can interact with our chatbot to get insights on your data.")

# Add a sidebar with a selectbox
selected_page = st.sidebar.selectbox("Select a page", ["Page 1", "Page 2", "Page 3"])

# Show a message based on the selected page
if selected_page == "Page 1":
    st.write("You selected Page 1.")
elif selected_page == "Page 2":
    st.write("You selected Page 2.")
elif selected_page == "Page 3":
    st.write("You selected Page 3.")
