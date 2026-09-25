import streamlit as st

st.set_page_config(page_title="Hello App", page_icon="👋")

st.title("Hello, world! 👋")
st.caption("Welcome to your Streamlit app.")
st.write("This page is a little cleaner and friendlier.")

if st.button("Click me"):
    st.success("Nice to meet you!")
