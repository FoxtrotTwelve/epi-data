import streamlit as st
import worlddata

@st.cache_data #stores this so the cleaned file isn't written every interaction with the app
def cached_load():
    return worlddata.load_data_and_clean()

worldData_cleaned = cached_load()

st.title("World Data Interface")