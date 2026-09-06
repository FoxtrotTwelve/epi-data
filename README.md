# World Data Coding Challenge

Loads, cleans, and shows the visualization of country data from supplied data from EPI.

Built with Python 3.13 and pandas.

The project covers loading the raw data and cleaning it, then exporting a cleaned version to csv. A few questions get answered about the cleaned data, and filtering functionality allows the user to narrow their search. There is also a way to view summary statistics.

---

## Requirements

- Python 3.13.15
- pandas 3.0.5
- numpy 2.5.2 (a pandas dependency and installs with it).
- streamlit 1.63.0

## How to run

Navigate to the folder you want to save it. In PowerShell, run each line in order:

```powershell
git clone https://github.com/FoxtrotTwelve/world-data-filter-visualization.git
cd world-data-filter-visualization

python -m venv .venv
.venv\Scripts\python.exe -m pip install pandas

.venv\Scripts\python.exe src\project.py
```

The last line is the only one you need if the repository and python/panda are already intalled. The menu is interactive, so run it in a terminal rather than an output pane.

For the secondary GUI, install with:
```
.venv\Scripts\python.exe -m pip install pandas streamlit
```
Then run with:
```
.venv\Scripts\streamlit.exe run src\app.py
```

## Cleaning assumptions

- Some rows in the data were repeated, so I edited it to keep one of the lines.
- An extraneous iso_a2 column, which I dropped
- Renamed the unlabeled column to RowID
- Changed 0 to N/A in the number data
- Preserve the "NA" for Namibia instead of it defaulting to N/A
- Any life expectancy that was greater than 100 was voided to N/A
- Any negative gdp was voided to N/A
- Any population or area that was less than 1000 was voided to N/A (the data was checked to make sure this wouldn't eliminate micronations and there were none in the data)

I kept the rows that had missing or voided information, as the other information within the row about the country is likely valid and useful. Pandas' mean and sum functions skip N/A automatically.

Some missing values are also correct, like with Antarctica not having a population.

## Answers to the questions

Run the program via the console app, these should appear after the cleaned data is listed and before the menu.

## Visualization

This will appear in the GUI only. The bar charts are average population density by continent and subregion because these seemed more interesting than by region.