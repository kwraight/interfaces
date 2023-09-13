import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.title("Welcome to the URL app")
st.write("Intended to test running a _streamlit_ app using URL")

if st.button("Time check"):
    st.write("Het is:", datetime.now())

if st.checkbox("embedded?"):
    components.iframe("https://docs.streamlit.io/library/components/components-api", width=800, height=600, scrolling=True)

st.write("One more time!")

st.write("Tot ziens!")
