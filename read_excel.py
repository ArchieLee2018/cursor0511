import pandas as pd

# Read the Excel file
file_path = "/Users/archieshen/Downloads/TP_2025_Q2.xlsx"
df = pd.read_excel(file_path)

# Get country names from row 3
country_names = df.iloc[2, 3:15]

# Iterate through each row
for index, row in df.iterrows():
    # Get values for current row
    row_values = df.iloc[index, 3:15]
    
    # Only process rows between "FP Push" and "FP SMS" in column 2
    if df.iloc[index, 1] in ["FP Push", "FP SMS"] or (
        index > df[df.iloc[:, 1] == "FP Push"].index[0] and 
        index < df[df.iloc[:, 1] == "FP SMS"].index[0]
    ):
        # Check if row has any non-empty country values and values are different from country names
        if row_values.notna().any() and not all(str(value) == str(country) for country, value in zip(country_names, row_values) if pd.notna(value)):
            # Group countries by their values
            value_to_countries = {}
            for country, value in zip(country_names, row_values):
                if pd.notna(value) and str(value) != str(country):
                    if str(value) not in value_to_countries:
                        value_to_countries[str(value)] = []
                    value_to_countries[str(value)].append(str(country))
            
            # Print in the requested format
            for value, countries in value_to_countries.items():
                countries_str = ', '.join(countries)
                print(f"[{value}/{value}] {countries_str} {df.iloc[index, 1]}")
