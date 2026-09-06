import pandas as pd
import worlddata

pd.set_option('display.max_rows', None) #Allows me to see the data in full
pd.set_option('display.max_columns', None)

worldData_cleaned = worlddata.load_data_and_clean()
print(worldData_cleaned)

print("-----ANSWERS TO QUESTIONS-----")
print(worlddata.print_answers(worldData_cleaned))
print("------------------------------")


filters = {
    "continent": set(),
    "region_un": set(),
    "subregion": set(),
    "type": set()
}

#loop to continue to see the menu unless program is exited
while True:
    filtered_data = worlddata.get_filtered_dataframe(worldData_cleaned, filters)

    print("----------MAIN MENU----------")
    print("")

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> shows the active filters converted to strings:
    hasContinentFilters = False
    hasRegionFilters = False
    hasSubregionFilters = False
    hasTypeFilters = False
    filters_continent_string = ""
    filters_region_string = ""
    filters_subregion_string = ""
    filters_type_string = ""
    if filters["continent"]:
        filters_continent_string = filters["continent"]
        hasContinentFilters = True
    if filters["region_un"]:
        filters_region_string = filters["region_un"]
        hasRegionFilters = True
    if filters["subregion"]:
        filters_subregion_string = filters["subregion"]
        hasSubregionFilters = True
    if filters["type"]:
        filters_type_string = filters["type"]
        hasTypeFilters = True

    hasFilters = False
    if hasContinentFilters == True or hasRegionFilters == True or hasSubregionFilters == True or hasTypeFilters == True: hasFilters = True

    if hasFilters == False:
        print(f"Active filters: None")
    else:
        print(f"Active filters:")
        if hasContinentFilters == True: print(f"• Continents: {filters_continent_string}")
        if hasRegionFilters == True: print(f"• Region: {filters_region_string}")
        if hasSubregionFilters == True: print(f"• Subregion: {filters_subregion_string}")
        if hasTypeFilters == True: print(f"• Type: {filters_type_string}")
    print("")
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


    print("1. Add Filter")
    print("2. Remove Filter")
    print("3. Clear All Filters")
    print("4. View Data with Applied Filters")
    print("5. Exit")
    print("-----------------------------")

    choice = input("> ")
    if choice == ("5"): #exits program
        break
    elif choice == ("1"): #presents a menu of filter categories to add
        print("Filter Categories: ")
        print("1. Continent")
        print("2. Region")
        print("3. Subregion")
        print("4. Type")
        print("")

        filter_category_choice = input("> ")


        if filter_category_choice == ("1"): #adds continent filter
            print(f"Current Continent Filters: {filters["continent"]}")
            print("Continent Filters to Add: ")
            continent_options = sorted(worldData_cleaned["continent"].dropna().unique())
            for i, continent_name in enumerate(continent_options, start=1):
                print(f"{i}. {continent_name}")

            continent_choice = input("> ")
            if continent_choice.isdigit() and 1 <= int(continent_choice) <= len(continent_options):
                filters["continent"].add(continent_options[int(continent_choice) - 1])

        elif filter_category_choice == ("2"): #adds region filter
            print(f"Current Region Filters: {filters["region_un"]}")
            print("Region Filters to Add: ")
            region_options = sorted(worldData_cleaned["region_un"].dropna().unique())
            for i, name in enumerate(region_options, start=1):
                print(f"{i}. {name}")
        
            region_choice = input("> ")
            if region_choice.isdigit() and 1 <= int(region_choice) <= len(region_options):
                filters["region_un"].add(region_options[int(region_choice) - 1])

        elif filter_category_choice == ("3"): #adds subregion filter
            print(f"Current Subregion Filters: {filters["subregion"]}")
            print("Subregion Filters to Add: ")
            subregion_options = sorted(worldData_cleaned["subregion"].dropna().unique())
            for i, name in enumerate(subregion_options, start=1):
                print(f"{i}. {name}")
                
            subregion_choice = input("> ")
            if subregion_choice.isdigit() and 1 <= int(subregion_choice) <= len(subregion_options):
                filters["subregion"].add(subregion_options[int(subregion_choice) - 1])

        elif filter_category_choice == ("4"): #adds type filter
            print(f"Current Type Filters: {filters["type"]}")
            print("Type Filters to Add: ")
            type_options = sorted(worldData_cleaned["type"].dropna().unique())
            for i, name in enumerate(type_options, start=1):
                print(f"{i}. {name}")
                        
            type_choice = input("> ")
            if type_choice.isdigit() and 1 <= int(type_choice) <= len(type_options):
                filters["type"].add(type_options[int(type_choice) - 1])


    elif choice == ("2"): #presents filter categories that can be removed
        print("Filter Categories to Remove: ")
        print("1. Continent")
        print("2. Region")
        print("3. Subregion")
        print("4. Type")
        print("")

        filter_category_choice = input("> ")


        if filter_category_choice == ("1"): #removes continent filter
            print(f"Current Continent Filters: {filters["continent"]}")
            print("Continent Filters to Remove: ")
            continent_options = sorted(worldData_cleaned["continent"].dropna().unique())
            for i, continent_name in enumerate(continent_options, start=1):
                print(f"{i}. {continent_name}")

            continent_choice = input("> ")
            if continent_choice.isdigit() and 1 <= int(continent_choice) <= len(continent_options):
                filters["continent"].discard(continent_options[int(continent_choice) - 1])

        elif filter_category_choice == ("2"): #removes region filter
            print(f"Current Region Filters: {filters["region_un"]}")
            print("Region Filters to Remove: ")
            region_options = sorted(worldData_cleaned["region_un"].dropna().unique())
            for i, name in enumerate(region_options, start=1):
                print(f"{i}. {name}")
        
            region_choice = input("> ")
            if region_choice.isdigit() and 1 <= int(region_choice) <= len(region_options):
                filters["region_un"].discard(region_options[int(region_choice) - 1])

        elif filter_category_choice == ("3"): #removes subregion filter
            print(f"Current Continent Filters: {filters["subregion"]}")
            print("Subregion Filters to Remove: ")
            subregion_options = sorted(worldData_cleaned["subregion"].dropna().unique())
            for i, name in enumerate(subregion_options, start=1):
                print(f"{i}. {name}")
                
            subregion_choice = input("> ")
            if subregion_choice.isdigit() and 1 <= int(subregion_choice) <= len(subregion_options):
                filters["subregion"].discard(subregion_options[int(subregion_choice) - 1])

        elif filter_category_choice == ("4"): #removes type filter
            print(f"Current Type Filters: {filters["type"]}")
            print("Type Filters to Remove: ")
            type_options = sorted(worldData_cleaned["type"].dropna().unique())
            for i, name in enumerate(type_options, start=1):
                print(f"{i}. {name}")
                        
            type_choice = input("> ")
            if type_choice.isdigit() and 1 <= int(type_choice) <= len(type_options):
                filters["type"].discard(type_options[int(type_choice) - 1])


    elif choice == ("3"): #clears filters
        filters["continent"].clear()
        filters["region_un"].clear()
        filters["subregion"].clear()
        filters["type"].clear()


    elif choice == ("4"): #displays filtered data
        print("---Displaying Data with Active Filters---")
        if hasFilters == False:
            print(f"Active filters: None")
        else:
            print(f"Active filters:")
            if hasContinentFilters == True: print(f"• Continents: {filters_continent_string}")
            if hasRegionFilters == True: print(f"• Region: {filters_region_string}")
            if hasSubregionFilters == True: print(f"• Subregion: {filters_subregion_string}")
            if hasTypeFilters == True: print(f"• Type: {filters_type_string}")
        print("")
    
        print(f"Showing {len(filtered_data)} of {len(worldData_cleaned)} countries")

        print("")
        print(filtered_data.drop(columns='RowID').to_string(index=False))
        print("")

