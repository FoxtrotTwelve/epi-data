import streamlit as st
import worlddata

@st.cache_data #stores this so the cleaned file isn't written every interaction with the app
def cached_load():
    return worlddata.load_data_and_clean()

worldData_cleaned = cached_load()

st.title("World Data Interface")

FILTER_LABELS = {   #needed to make the filter display look better
    'continent': 'Continent',
    'region_un': 'Region',
    'subregion': 'Subregion',
    'type':      'Type',
}

filters = {}
for column, label in FILTER_LABELS.items():
    filters[column] = st.sidebar.multiselect(label, sorted(worldData_cleaned[column].dropna().unique()))
worldData_filtered = worlddata.get_filtered_dataframe(worldData_cleaned, filters)

#Displays the filtered data grid:
st.write(f"Showing {len(worldData_filtered)} of {len(worldData_cleaned)} countries")
st.subheader("Countries:")
st.dataframe(worldData_filtered.drop(columns='RowID'), hide_index=True) #better to use this because it can take parameters to drop columns
#st.write(worldData_filtered.drop(columns='RowID'))

st.write("")

#Displays the stats:
st.subheader("Statistics Summary")
st.dataframe(worlddata.get_summary_statistics(worldData_filtered))



