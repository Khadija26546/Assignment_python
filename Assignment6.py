
import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Amit', 'Riya', 'Rahul', 'Sneha', 'Amit'],
    'Marks': [85, 90, None, 75, 85],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Pune']
}

df = pd.DataFrame(data)

# Display original dataset
print("Original Dataset:")
print(df)

# Display first five records
print("\nFirst 5 Records:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with mean
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# Remove duplicate records
df = df.drop_duplicates()

# Select students having marks greater than 80
print("\nStudents with Marks Greater Than 80:")
print(df.loc[df['Marks'] > 80])

# Display final cleaned dataset
print("\nFinal Cleaned Dataset:")
print(df)
