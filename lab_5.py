import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import math

# Load the CSV file into a DataFrame
df = pd.read_csv("D:/5th sem/PA LAB/bodyPerformance.csv")

# Select only numeric columns for analysis
numeric_df = df.select_dtypes(include=[np.number])

# Measure of Central Tendency
mean = numeric_df.mean()

# Geometric Mean (for positive values)
geometric_mean = numeric_df.apply(lambda x: stats.gmean(x[x > 0]) if (x > 0).all() else np.nan)

# Harmonic Mean (for positive values)
harmonic_mean = numeric_df.apply(lambda x: stats.hmean(x[x > 0]) if (x > 0).all() else np.nan)

# Mode
mode = numeric_df.mode().iloc[0]

# Median
median = numeric_df.median()

print("Mean:\n", mean)
print("Geometric Mean:\n", geometric_mean)
print("Harmonic Mean:\n", harmonic_mean)
print("Mode:\n", mode)
print("Median:\n", median)

# Measure of Dispersion
# Variance
variance = numeric_df.var()

# Standard Deviation
std_dev = numeric_df.std()

# Skewness
skewness = numeric_df.skew()

# Interquartile Range (IQR)
Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
iqr = Q3 - Q1

# Range
data_range = numeric_df.max() - numeric_df.min()

# Mean Absolute Deviation (MAD)
mad = (numeric_df - numeric_df.mean()).abs().mean()

print("Variance:\n", variance)
print("Standard Deviation:\n", std_dev)
print("Skewness:\n", skewness)
print("Interquartile Range (IQR):\n", iqr)
print("Range:\n", data_range)
print("Mean Absolute Deviation (MAD):\n", mad)

# Pearson correlation coefficient (only for numeric columns)
correlation_matrix = numeric_df.corr()

print("Correlation Matrix:\n", correlation_matrix)

# Data Visualization
# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=numeric_df)
plt.title('Boxplot of Features')
plt.show()

# Histograms
numeric_df.hist(bins=20, figsize=(10, 8))
plt.suptitle('Histograms of Features')
plt.show()

# Density Plots
num_cols = len(numeric_df.columns)
rows = math.ceil(num_cols / 3)  # Adjust layout dynamically for 3 plots per row
layout = (rows, 3)

numeric_df.plot(kind='density', subplots=True, layout=layout, figsize=(12, 8), sharex=False)
plt.suptitle('Density Plots of Features')
plt.show()

# Scatterplot between height and weight
if 'height_cm' in df.columns and 'weight_kg' in df.columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df['height_cm'], y=df['weight_kg'])
    plt.title('Scatterplot between Height and Weight')
    plt.xlabel('height_cm')
    plt.ylabel('weight_kg')
    plt.show()

# Bar Chart (if there are categorical columns in the dataset)
categorical_columns = df.select_dtypes(include=['object']).columns

for col in categorical_columns:
    plt.figure(figsize=(8, 6))
    df[col].value_counts().plot(kind='bar')
    plt.title(f'Bar Chart of {col}')
    plt.show()
