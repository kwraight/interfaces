import streamlit as st
import streamlit.components.v1 as components

st.title("Welcome to the URL app")
st.write("Intended to test running a _streamlit_ app using URL")

components.iframe("https://open.spotify.com")
