import streamlit as st
import streamlit.components.v1 as components

st.title("Welcome to the URL app")
st.write("Intended to test running a _streamlit_ app using URL")

if st.checkbox("embedded?"):
    components.iframe("https://docs.streamlit.io/library/components/components-api", width=800, height=600, scrolling=True)


st.write("Tot ziens!")
