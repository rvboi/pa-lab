import pandas as pd

# Load CSV
df_csv = pd.read_csv("D:/5th sem/PA LAB/forestfires.csv")

# Verify the column names
print("Column names:", df_csv.columns)

# Group by a column and calculate the mean for each group
df_grouped_mean = df_csv.groupby('X').mean(numeric_only=True)

# Group by multiple columns and calculate the count
df_grouped_count = df_csv.groupby(['X', 'Y']).count()

# Create a pivot table
# Replace 'Type' with a valid column name
df_pivot = pd.pivot_table(df_csv, values='area', index='month', columns='day', aggfunc='mean')

# Example DataFrames for concatenation and merging
df1 = df_csv[['X', 'Y']]  # Define df1 with actual columns
df2 = df_csv[['X', 'Y']]  # Define df2 with actual columns

# Concatenate DataFrames vertically (rows)
df_concat_vertical = pd.concat([df1, df2], axis=0)

# Concatenate DataFrames horizontally (columns)
df_concat_horizontal = pd.concat([df1, df2], axis=1)

# Merge DataFrames with different join types
# Note: The `how` parameter should be one of 'inner', 'left', 'right', 'outer'
# Changed 'Y' to valid join types
df_merged_inner = pd.merge(df1, df2, on='X', how='inner')

# Left join
df_merged_left = pd.merge(df1, df2, on='X', how='left')

# Right join
df_merged_right = pd.merge(df1, df2, on='X', how='right')

# Outer join
df_merged_outer = pd.merge(df1, df2, on='X', how='outer')

# Print results to check
print("Grouped Mean:")
print(df_grouped_mean.head())

print("Grouped Count:")
print(df_grouped_count.head())

print("Pivot Table:")
print(df_pivot.head())

print("Concatenated Vertical:")
print(df_concat_vertical.head())

print("Concatenated Horizontal:")
print(df_concat_horizontal.head())

print("Merged Inner:")
print(df_merged_inner.head())

print("Merged Left:")
print(df_merged_left.head())

print("Merged Right:")
print(df_merged_right.head())

print("Merged Outer:")
print(df_merged_outer.head())
