import pandas as pd

# Load CSV
df_csv = pd.read_csv("D:/5th sem/PA LAB/melb_data.csv")

# Load Excel
df_excel = pd.read_excel("D:/5th sem/PA LAB/COVID-19 multilingual glossary_.xlsx")

# Load JSON
df_json = pd.read_json("D:/5th sem/PA LAB/brazil_geo.json")

# View the first and last few rows
print(df_csv.head())    # first 5 rows
print(df_csv.tail())    # last 5 rows

# View the shape of the DataFrame
print(df_csv.shape)

# View column names
print(df_csv.columns)

# View data types
print(df_csv.dtypes)

# Information about DataFrame
print(df_csv.info())

# Descriptive statistics
print(df_csv.describe())

# Select a column by name
print(df_csv['Rooms'])

# Select multiple columns
print(df_csv[['Price', 'Postcode']])

# Select rows using slicing
print(df_csv[0:5])  # Rows from 0 to 4

# Select rows/columns using loc (label-based)
print(df_csv.loc[0, 'Price'])

# Select rows/columns using iloc (integer position-based)
print(df_csv.iloc[0, 0])  # First row, first column

