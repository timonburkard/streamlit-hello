import streamlit as st

st.set_page_config(page_title="Hello App", page_icon="👋")

st.title("Hello, world! 👋")
st.caption("Welcome to my Streamlit app.")
st.write("It is just a simple test.")

if st.button("Click me"):
    st.success("Nice to meet you!")
