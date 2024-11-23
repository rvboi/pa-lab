import pandas as pd

# Load the dataset from CSV
df = pd.read_csv("D:/5th sem/PA LAB/Telecom_customer churn.csv")

# Inspect the first few rows
print(df.head())



# Checking for missing values
print(df.isnull().sum())

# Dropping rows with missing values (or alternatively you can use .fillna())
df = df.dropna()

# For large datasets, filling missing values can be better
# df.fillna(df.mean(), inplace=True)


# Handling outliers using IQR (Interquartile Range)
# Specifying numeric_only=True to suppress the future warning
Q1 = df.select_dtypes(include=['number']).quantile(0.25, numeric_only=True)
Q3 = df.select_dtypes(include=['number']).quantile(0.75, numeric_only=True)
IQR = Q3 - Q1

# Align the DataFrame and Series before comparison to avoid future issues
df_numeric = df.select_dtypes(include=['number'])
outliers_condition = ~((df_numeric < (Q1 - 1.5 * IQR)) | (df_numeric > (Q3 + 1.5 * IQR))).any(axis=1)

# Remove outliers
df = df[outliers_condition]

# Reattach the non-numeric columns after removing outliers from numeric columns
df_cleaned = pd.concat([df_numeric[outliers_condition], df.select_dtypes(exclude=['number'])], axis=1)

# Inspect the cleaned dataframe
print(df_cleaned.head())







