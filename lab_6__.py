import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score)

# Load dataset
df = pd.read_csv("D:/5th sem/PA LAB/Telecom_customer churn.csv")  # Update the path if necessary

# EDA: Check the first few rows of the dataset
print(df.head())

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Visualize churn distribution
sns.countplot(x='churn', data=df)
plt.title('Distribution of Churned vs. Non-Churned Customers')
plt.xlabel('Churn')
plt.ylabel('Count')
plt.show()

# Visualizing the correlation matrix with numeric_only
plt.figure(figsize=(12, 8))
correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Separate numeric and categorical columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Handling missing values for numeric columns using the mean strategy
imputer_numeric = SimpleImputer(strategy='mean')
df[numeric_cols] = imputer_numeric.fit_transform(df[numeric_cols])

# Handling missing values for categorical columns using the most frequent strategy
imputer_categorical = SimpleImputer(strategy='most_frequent')
df[categorical_cols] = imputer_categorical.fit_transform(df[categorical_cols])

# Handling outliers using IQR method
Q1 = df[numeric_cols].quantile(0.25)
Q3 = df[numeric_cols].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df[numeric_cols] < (Q1 - 1.5 * IQR)) | (df[numeric_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]

# Feature scaling for numeric columns
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Drop columns that are irrelevant (like 'Customer_ID' if exists)
df.drop(columns=['Customer_ID'], inplace=True, errors='ignore')

# Encode categorical variables
le = LabelEncoder()
for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Check the unique values in the churn column
print("Unique values in 'churn' before conversion:", df['churn'].unique())

# If churn values are continuous, convert them into binary (0/1) using a threshold
df['churn'] = (df['churn'] > 0).astype(int)  # Adjust the threshold as necessary

# Verify the unique values after conversion
print("Unique values in 'churn' after conversion:", df['churn'].unique())

# Split into features (X) and target (y)
X = df.drop('churn', axis=1)
y = df['churn'].astype(int)  # Ensure churn is an integer type

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Linear Regression model
lin_reg = LinearRegression()

# Train the model
lin_reg.fit(X_train, y_train)

# Predict on the test data
y_pred = lin_reg.predict(X_test)

# Since y_pred is continuous, convert it to binary predictions using a threshold (0.5)
y_pred_binary = (y_pred > 0.5).astype(int)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred_binary)
precision = precision_score(y_test, y_pred_binary)
recall = recall_score(y_test, y_pred_binary)
f1 = f1_score(y_test, y_pred_binary)

# Print evaluation metrics
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

# Visualizing actual vs predicted churn
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred_binary)
plt.xlabel('Actual Churn')
plt.ylabel('Predicted Churn')
plt.title('Actual vs Predicted Churn')
plt.show()

# Update numeric_cols after dropping Customer_ID
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

# Plot histograms for numeric features
df[numeric_cols].hist(bins=30, figsize=(15, 10))
plt.suptitle('Histograms of Numeric Features')
plt.show()
