
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating a sample dataset
data = {
    'Name': ['Amit', 'Riya', 'Rahul', 'Sneha', 'Priya'],
    'Marks': [85, 90, 75, 80, 95],
    'Attendance': [80, 90, 70, 85, 95],
    'Study_Hours': [4, 5, 2, 3, 6]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# 1. Line Plot
plt.figure()
plt.plot(df['Name'], df['Marks'], marker='o')
plt.title("Line Plot - Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()

# 2. Bar Plot
plt.figure()
plt.bar(df['Name'], df['Marks'])
plt.title("Bar Plot - Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()

# 3. Scatter Plot
plt.figure()
plt.scatter(df['Study_Hours'], df['Marks'])
plt.title("Scatter Plot - Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# 4. Heatmap
plt.figure()
correlation = df[['Marks', 'Attendance', 'Study_Hours']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Heatmap - Correlation Matrix")
plt.show()
