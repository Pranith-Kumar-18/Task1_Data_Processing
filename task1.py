import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Step 1: Load dataset properly with correct parsing
df = pd.read_csv('titanic_newdata_set.csv', delimiter=',', quotechar='"')
df.columns = df.columns.str.strip()  # Remove any leading/trailing spaces in column names
print("✅ Dataset Loaded Successfully!")
print("📋 Column names:", df.columns.tolist())
print(df.head())

# Step 2: Check for missing values
print("\n🔍 Missing values before cleaning:")
print(df.isnull().sum())

# Step 3: Handle missing values
if 'Age' in df.columns:
    df['Age'] = df['Age'].fillna(df['Age'].median())
if 'Fare' in df.columns:
    df['Fare'] = df['Fare'].fillna(df['Fare'].mean())
if 'Embarked' in df.columns:
    df.dropna(subset=['Embarked'], inplace=True)

print("\n✅ Missing values handled!")
print(df.isnull().sum())

# Step 4: Encode categorical data
le = LabelEncoder()
if 'Sex' in df.columns:
    df['Sex'] = le.fit_transform(df['Sex'])
if 'Embarked' in df.columns:
    df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Step 5: Normalize numerical columns
scaler = StandardScaler()
for col in ['Age', 'Fare']:
    if col in df.columns:
        df[[col]] = scaler.fit_transform(df[[col]])

# Step 6: Visualize outliers
if 'Age' in df.columns:
    print("\n📈 Boxplot for Age")
    sns.boxplot(x=df['Age'])
    plt.show()

if 'Fare' in df.columns:
    print("\n📈 Boxplot for Fare")
    sns.boxplot(x=df['Fare'])
    plt.show()

# Step 7: Save cleaned data
df.to_csv('titanic_cleaned.csv', index=False)
print("\n✅ Cleaned data saved as 'titanic_cleaned.csv'")

input("✅ Press Enter to exit...")
