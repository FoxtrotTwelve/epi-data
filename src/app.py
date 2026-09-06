import streamlit as st
import worlddata

st.set_page_config(layout="wide") #widens the page so all table columns appear instead of a horizontal scroll

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
if len(worldData_filtered) == 0:
    st.write("No countries match the current filters.")
else:
    st.subheader("Countries:")
    st.dataframe( #better to use this because it can take parameters to drop columns
        worldData_filtered.drop(columns='RowID'), 
        hide_index=True,
        column_config={
            'iso_a2':    'ISO',
            'name_long': 'Country',
            'continent': 'Continent',
            'region_un': 'Region',
            'subregion': 'Subregion',
            'type':      'Type',
            'area_km2':  'Area (km²)',
            'pop':       'Population',
            'lifeExp':   'Life Expectancy',
            'gdpPercap': 'GDP per Capita',
        }
    )
    #st.write(worldData_filtered.drop(columns='RowID'))

    st.write("")

    #Displays the stats:
    st.subheader("Statistics Summary")
    st.dataframe(worlddata.get_summary_statistics(worldData_filtered))
    st.write("")

    #Bonus: "bar chart visualisation of the average population density by region for the filtered data"
    st.subheader("Average Population Density by Region:")
    st.bar_chart(
        worlddata.get_population_density(worldData_filtered),
        x_label="Region",
        y_label="People per km²"
    )







