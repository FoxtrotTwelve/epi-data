import pandas as pd
from pathlib import Path

FILE_PATH = Path(__file__).parent.parent / "worldData.csv"
OUTPUT_PATH = Path(__file__).parent.parent / "worldData_cleanedOutput.csv"
STATISTICS_COLUMNS = ['area_km2', 'pop', 'lifeExp', 'gdpPercap']


def load_data_and_clean(FILE_PATH=FILE_PATH):
    worldData = pd.read_csv(FILE_PATH, keep_default_na=False, na_values=['#N/A', 0.0]) #Load data and convert only obvious missing data to NaN
    #print(worldData)
    worldData = worldData.rename(columns={'Unnamed: 0': 'RowID'}) #Fix this unnamed column

    worldData_dupeRowsCleared = worldData.drop_duplicates(subset=['RowID'], keep='first') #remove duplicate rows based on country code
    worldData_dupeRowsCleared = worldData_dupeRowsCleared.reset_index(drop=True) #reset the row index for each row
    worldData_dupeColumnCleared = worldData_dupeRowsCleared.drop('iso_a2.1', axis=1) #remove second extraneous country code column
    worldData_dupeColumnCleared['lifeExp'] = worldData_dupeColumnCleared['lifeExp'].mask(worldData_dupeColumnCleared['lifeExp'] > 100) #fixes impossible 600 year old tree life expectency
    worldData_dupeColumnCleared['gdpPercap'] = worldData_dupeColumnCleared['gdpPercap'].mask(worldData_dupeColumnCleared['gdpPercap'] < 0) #fixes impossible negative GDP
    worldData_dupeColumnCleared['pop'] = worldData_dupeColumnCleared['pop'].mask(worldData_dupeColumnCleared['pop'] < 1000) #removes too low population, if any
    worldData_dupeColumnCleared['area_km2'] = worldData_dupeColumnCleared['area_km2'].mask(worldData_dupeColumnCleared['area_km2'] < 1000) #removes too low area, if any
    worldData_dupeColumnCleared.to_csv(OUTPUT_PATH, index=False)

    worldData_cleaned = worldData_dupeColumnCleared #Changing variable names. Keeping the previous names and work to show my process. I would clean this up and refactor later.

    return worldData_cleaned


def get_filtered_dataframe(worldData_filtered, filters):
    for column, chosen_values in filters.items():
        if chosen_values:
            worldData_filtered = worldData_filtered[worldData_filtered[column].isin(chosen_values)]

    return worldData_filtered


def get_summary_statistics(worlddata):
    statistics = worlddata[STATISTICS_COLUMNS].describe().T
    return statistics


def print_answers(worldData_cleaned):
    #Which continent has the most countries in the data?
    continent_mode = worldData_cleaned['continent'].mode() #extracts the item with the most
    #print("Continent with Most Countries: " + continent_mode[0])


    #Which region has the largest combined area in sq. km?
    regions_by_area = worldData_cleaned.groupby('region_un')['area_km2'].sum() #groups and sums the regions' area
    #print(regions_by_area)
    region_largest_area = regions_by_area.idxmax() #picks region with the most area
    #print("Region (Not Continent) with the Largest Area: " + region_largest_area) #Russia appears to be listed as Europe - ok fair enough


    #Which country has the highest life expectancy?
    highest_life_exp = worldData_cleaned.loc[worldData_cleaned['lifeExp'].idxmax(), 'name_long'] #picks the value of one column after determining the highest value in another column
    #print("Country with Highest Life Expectency: " + highest_life_exp)


    #Which subregion has the lowest / highest average GDP per capita?
    subregion_dataframe = worldData_cleaned.groupby('subregion')['gdpPercap'].mean() #makes dataframe based off of subregion and gdp and averages them
    #print(subregion_dataframe)
    subregion_max = subregion_dataframe.idxmax() #finds the maximum gdp and stores associated region
    subregion_min = subregion_dataframe.idxmin() #finds the minimum gdp and stores associated region
    #print(f"Max: {subregion_max} (Average GDP: {subregion_dataframe.max()})")
    #print(f"Min: {subregion_min} (Average GDP: {subregion_dataframe.min()})")

    return f"Continent with Most Countries: {continent_mode[0]}\nRegion (Not Continent) with the Largest Area: {region_largest_area}\nCountry with Highest Life Expectency: {highest_life_exp}\nSubregion with Max Average GDP: {subregion_max} (Average GDP: {subregion_dataframe.max()})\nSubregion with Min Average GDP: {subregion_min} (Average GDP: {subregion_dataframe.min()})"
