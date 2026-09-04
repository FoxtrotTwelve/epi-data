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