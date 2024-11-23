import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load CSV
df_csv = pd.read_csv("D:/5th sem/PA LAB/melb_data.csv")

# Check for missing values summary
print(df_csv.isnull().sum())  # Shows count of missing values per column

# Fill missing values with 0
df_csv.fillna(value=0, inplace=True)

# Drop rows with missing values
df_csv.dropna(inplace=True)

# Interpolate missing values (useful for time-series data)
df_csv.interpolate(inplace=True)

# Apply Min-Max Scaling (replace 'Price' with the actual numerical column name)
scaler = MinMaxScaler()
df_csv['scaled_price'] = scaler.fit_transform(df_csv[['Price']])

# Apply Standard Scaling (replace 'Price' with the actual numerical column name)
scaler = StandardScaler()
df_csv['standard_scaled_price'] = scaler.fit_transform(df_csv[['Price']])

# Create dummy variables (replace 'Category' with the actual categorical column name)
df_dummies = pd.get_dummies(df_csv, columns=['SellerG'])

# View updated DataFrame
print(df_dummies.head())
