# AIML Task 1 - Titanic Dataset Preprocessing

## Overview

This project focuses on preprocessing the Titanic dataset to prepare it for further analysis or model building. The dataset contains information about passengers on the Titanic, such as their age, sex, and whether they survived or not. The goal of this task is to clean the dataset by handling missing values, converting categorical variables to numeric, scaling the features, and removing outliers.

## Steps Taken

### 1. **Install Required Libraries**
   - Pandas
   - Numpy
   - Matplotlib
   - Seaborn
   - Scikit-learn

### 2. **Data Preprocessing**
   - Loaded the Titanic dataset using Pandas.
   - Checked the dataset for missing values and handled them appropriately:
     - Filled missing numerical values (e.g., Age) with the mean.
     - Filled missing categorical values (e.g., Embarked) with the mode.
   - Converted categorical variables (e.g., Sex and Embarked) into numerical values using label encoding and one-hot encoding.
   - Scaled numerical features (e.g., Age and Fare) using StandardScaler to standardize the data.
   - Identified and removed outliers using boxplots and the Interquartile Range (IQR) method.

### 3. **Output**
   - Cleaned dataset saved as `titanic_cleaned.csv`.

## Files in the Repository

- `titanic_cleaned.csv`: The cleaned Titanic dataset after preprocessing.
- `titanic_cleaning.py`: Python script containing the data preprocessing steps.
- `README.md`: This documentation file explaining the steps taken for preprocessing.

## How to Use

1. Clone this repository or download the files to your local machine.
2. Ensure you have Python and the necessary libraries installed.
3. Run the `titanic_cleaning.py` script to preprocess the Titanic dataset.
4. The cleaned dataset will be saved as `titanic_cleaned.csv`.

## Libraries Used

- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-learn


