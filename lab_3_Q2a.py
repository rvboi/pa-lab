import numpy as np

# Load a dataset (CSV File)


data = np.genfromtxt("D:/5th sem/PA LAB/melb_data.csv", delimiter=',', skip_header=1)

print("Data Loaded from CSV:\n", data)
# Handling Missing Values
# Replace NaN values with the mean of each column
data_cleaned = np.where(np.isnan(data), np.nanmean(data, axis=0), data)
print("\nData After Handling Missing Values:\n", data_cleaned)
# Normalization (Min-Max)
data_min = np.min(data_cleaned, axis=0)  # Min value for each column
data_max = np.max(data_cleaned, axis=0)  # Max value for each column

data_normalized = (data_cleaned - data_min) / (data_max - data_min)
print("\nNormalized Data (Min-Max Scaling):\n", data_normalized)
# Standardization (Z-score)
mean = np.mean(data_cleaned, axis=0)  # Mean for each column
std_dev = np.std(data_cleaned, axis=0)  # Standard Deviation for each column

data_standardized = (data_cleaned - mean) / std_dev
print("\nStandardized Data (Z-score Scaling):\n", data_standardized)
# Statistical Measures: Mean, Median, Std Dev, Variance
mean_values = np.mean(data_cleaned, axis=0)  # Mean for each column
median_values = np.median(data_cleaned, axis=0)  # Median for each column
std_values = np.std(data_cleaned, axis=0)  # Standard Deviation for each column
variance_values = np.var(data_cleaned, axis=0)  # Variance for each column

print("\nStatistical Measures:")
print("Mean:\n", mean_values)
print("Median:\n", median_values)
print("Standard Deviation:\n", std_values)
print("Variance:\n", variance_values)
