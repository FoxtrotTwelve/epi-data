import pandas as pd

pd.set_option('display.max_rows', None) #Allows me to see the data in full
pd.set_option('display.max_columns', None)


worldData = pd.read_csv('worldData.csv', keep_default_na=False, na_values=['#N/A', 0.0]) #Load data and convert only obvious missing data to NaN
#print(worldData)
worldData = worldData.rename(columns={'Unnamed: 0': 'RowID'}) #Fix this unnamed column

worldData_dupeRowsCleared = worldData.drop_duplicates(subset=['RowID'], keep='first') #remove duplicate rows based on country code
worldData_dupeRowsCleared = worldData_dupeRowsCleared.reset_index(drop=True) #reset the row index for each row
worldData_dupeColumnCleared = worldData_dupeRowsCleared.drop('iso_a2.1', axis=1) #remove second extraneous country code column
worldData_dupeColumnCleared['lifeExp'] = worldData_dupeColumnCleared['lifeExp'].mask(worldData_dupeColumnCleared['lifeExp'] > 100) #fixes impossible 600 year old tree life expectency
worldData_dupeColumnCleared['gdpPercap'] = worldData_dupeColumnCleared['gdpPercap'].mask(worldData_dupeColumnCleared['gdpPercap'] < 0) #fixes impossible negative GDP
worldData_dupeColumnCleared['pop'] = worldData_dupeColumnCleared['pop'].mask(worldData_dupeColumnCleared['pop'] < 1000) #removes too low population, if any
worldData_dupeColumnCleared['area_km2'] = worldData_dupeColumnCleared['area_km2'].mask(worldData_dupeColumnCleared['area_km2'] < 1000) #removes too low area, if any
print(worldData_dupeColumnCleared)
worldData_dupeColumnCleared.to_csv('worldData_cleanedOutput.csv', index=False)

worldData_cleaned = worldData_dupeColumnCleared #Changing variable names. Keeping the previous names and work to show my process. I would clean this up and refactor later.


#Which continent has the most countries in the data?
continent_mode = worldData_cleaned['continent'].mode() #extracts the item with the most
print("Continent with Most Countries: " + continent_mode[0])


#Which region has the largest combined area in sq. km?
regions_by_area = worldData_cleaned.groupby('region_un')['area_km2'].sum() #groups and sums the regions' area
#print(regions_by_area)
region_largest_area = regions_by_area.idxmax() #picks region with the most area
print("Region (Not Continent) with the Largest Area: " + region_largest_area) #Russia appears to be listed as Europe - ok fair enough


#Which country has the highest life expectancy?
highest_life_exp = worldData_cleaned.loc[worldData_cleaned['lifeExp'].idxmax(), 'name_long'] #picks the value of one column after determining the highest value in another column
print("Country with Highest Life Expectency: " + highest_life_exp)


#Which subregion has the lowest / highest average GDP per capita?
subregion_dataframe = worldData_cleaned.groupby('subregion')['gdpPercap'].mean() #makes dataframe based off of subregion and gdp and averages them
#print(subregion_dataframe)
subregion_max = subregion_dataframe.idxmax() #finds the maximum gdp and stores associated region
subregion_min = subregion_dataframe.idxmin() #finds the minimum gdp and stores associated region
print(f"Max: {subregion_max} (Average GDP: {subregion_dataframe.max()})")
print(f"Min: {subregion_min} (Average GDP: {subregion_dataframe.min()})")




filters = {
    "continent": set(),
    "region_un": set(),
    "subregion": set(),
    "type": set()
}

while True:
    print("----------MAIN MENU----------")
    print("")
    print(f"Active filters: {filters}")
    print("Showing ")
    print("")


    print("1. Add Filter")
    print("2. Remove Filter")
    print("3. Clear All Filters")
    print("4. View Data with Applied Filters")
    print("5. Exit")
    print("-----------------------------")

    choice = input("> ")
    if choice == ("5"):
        break
    elif choice == ("1"):
        print("Filter Categories: ")
        print("1. Continent")
        print("2. Region")
        print("3. Subregion")
        print("4. Type")
        print("")

        filter_category_choice = input("> ")


        if filter_category_choice == ("1"):
            print(f"Current Continent Filters: {filters["continent"]}")
            print("Continent Filters to Add: ")
            continent_options = sorted(worldData_cleaned["continent"].dropna().unique())
            for i, continent_name in enumerate(continent_options, start=1):
                print(f"{i}. {continent_name}")

            continent_choice = input("> ")
            if continent_choice.isdigit() and 1 <= int(continent_choice) <= len(continent_options):
                filters["continent"].add(continent_options[int(continent_choice) - 1])

        elif filter_category_choice == ("2"):
            print(f"Current Region Filters: {filters["region_un"]}")
            print("Region Filters to Add: ")
            region_options = sorted(worldData_cleaned["region_un"].dropna().unique())
            for i, name in enumerate(region_options, start=1):
                print(f"{i}. {name}")
        
            region_choice = input("> ")
            if region_choice.isdigit() and 1 <= int(region_choice) <= len(region_options):
                filters["region_un"].add(region_options[int(region_choice) - 1])

        elif filter_category_choice == ("3"):
            print(f"Current Subregion Filters: {filters["subregion"]}")
            print("Subregion Filters to Add: ")
            subregion_options = sorted(worldData_cleaned["subregion"].dropna().unique())
            for i, name in enumerate(subregion_options, start=1):
                print(f"{i}. {name}")
                
            subregion_choice = input("> ")
            if subregion_choice.isdigit() and 1 <= int(subregion_choice) <= len(subregion_options):
                filters["subregion"].add(subregion_options[int(subregion_choice) - 1])

        elif filter_category_choice == ("4"):
            print(f"Current Type Filters: {filters["type"]}")
            print("Type Filters to Add: ")
            type_options = sorted(worldData_cleaned["type"].dropna().unique())
            for i, name in enumerate(type_options, start=1):
                print(f"{i}. {name}")
                        
            type_choice = input("> ")
            if type_choice.isdigit() and 1 <= int(type_choice) <= len(type_options):
                filters["type"].add(type_options[int(type_choice) - 1])


    elif choice == ("2"):
        print("Filter Categories to Remove: ")
        print("1. Continent")
        print("2. Region")
        print("3. Subregion")
        print("4. Type")
        print("")

        filter_category_choice = input("> ")


        if filter_category_choice == ("1"):
            print(f"Current Continent Filters: {filters["continent"]}")
            print("Continent Filters to Remove: ")
            continent_options = sorted(worldData_cleaned["continent"].dropna().unique())
            for i, continent_name in enumerate(continent_options, start=1):
                print(f"{i}. {continent_name}")

            continent_choice = input("> ")
            if continent_choice.isdigit() and 1 <= int(continent_choice) <= len(continent_options):
                filters["continent"].discard(continent_options[int(continent_choice) - 1])

        elif filter_category_choice == ("2"):
            print(f"Current Region Filters: {filters["region_un"]}")
            print("Region Filters to Remove: ")
            region_options = sorted(worldData_cleaned["region_un"].dropna().unique())
            for i, name in enumerate(region_options, start=1):
                print(f"{i}. {name}")
        
            region_choice = input("> ")
            if region_choice.isdigit() and 1 <= int(region_choice) <= len(region_options):
                filters["region_un"].discard(region_options[int(region_choice) - 1])

        elif filter_category_choice == ("3"):
            print(f"Current Continent Filters: {filters["subregion"]}")
            print("Subregion Filters to Remove: ")
            subregion_options = sorted(worldData_cleaned["subregion"].dropna().unique())
            for i, name in enumerate(subregion_options, start=1):
                print(f"{i}. {name}")
                
            subregion_choice = input("> ")
            if subregion_choice.isdigit() and 1 <= int(subregion_choice) <= len(subregion_options):
                filters["subregion"].discard(subregion_options[int(subregion_choice) - 1])

        elif filter_category_choice == ("4"):
            print(f"Current Type Filters: {filters["type"]}")
            print("Type Filters to Remove: ")
            type_options = sorted(worldData_cleaned["type"].dropna().unique())
            for i, name in enumerate(type_options, start=1):
                print(f"{i}. {name}")
                        
            type_choice = input("> ")
            if type_choice.isdigit() and 1 <= int(type_choice) <= len(type_options):
                filters["type"].discard(type_options[int(type_choice) - 1])
