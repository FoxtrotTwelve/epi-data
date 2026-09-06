import streamlit as st
import worlddata

@st.cache_data #stores this so the cleaned file isn't written every interaction with the app
def cached_load():
    return worlddata.load_data_and_clean()

worldData_cleaned = cached_load()

st.title("World Data Interface")

filters = {}
for column in ['continent', 'region_un', 'subregion', 'type']:
    filters[column] = st.sidebar.multiselect(column, sorted(worldData_cleaned[column].dropna().unique()))
worldData_filtered = worlddata.get_filtered_dataframe(worldData_cleaned, filters)

st.write(f"Showing {len(worldData_filtered)} of {len(worldData_cleaned)} countries")