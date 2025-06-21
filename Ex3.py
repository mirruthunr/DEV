# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------
# PART 1: NumPy Operations
# -----------------------
print("---- NumPy Array Operations ----")
x = np.array([10, 20, 30, 40, 50])
y = np.array([[1, 2], [3, 4], [5, 6]])

print("Original 1D Array x:", x)
print("x + 10:", x + 10)
print("x squared:", x ** 2)
print("Mean of x:", np.mean(x))
print("Reshape x to (5,1):\n", x.reshape(5, 1))
print("Original 2D Array y:\n", y)
print("Transpose of y:\n", y.T)
print("Flatten y:", y.flatten())

# ----------------------------
# PART 2: Pandas DataFrame Ops
# ----------------------------
print("\n---- Pandas DataFrame Operations ----")
data = {
    'Name': ['Ravi', 'Meena', 'Amit', 'Sneha'],
    'Maths': [88, 92, 79, 95],
    'Science': [84, 95, 91, 89],
    'English': [78, 85, 87, 92]
}
df = pd.DataFrame(data)

print("\nStudent DataFrame:")
print(df)

print("\nColumn Names:", df.columns.tolist())
print("Shape of DataFrame:", df.shape)
print("\nData Types:")
print(df.dtypes)

df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)
df['Average'] = df['Total'] / 3
print("\nWith Total and Average Columns:")
print(df)

print("\nStudents scoring above 90 in Science:")
print(df[df['Science'] > 90])

print("\nSorted by Average Score:")
print(df.sort_values(by='Average', ascending=False))

# -----------------------
# PART 3: Matplotlib Plots
# -----------------------

# Line Plot – Subject Scores
plt.figure()
plt.plot(df['Name'], df['Maths'], label='Maths', marker='o')
plt.plot(df['Name'], df['Science'], label='Science', marker='s')
plt.plot(df['Name'], df['English'], label='English', marker='^')
plt.title('Subject Scores of Students')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.legend()
plt.grid(True)
plt.show()

# Bar Plot – Total Marks
plt.figure()
plt.bar(df['Name'], df['Total'], color='teal')
plt.title('Total Marks of Students')
plt.xlabel('Name')
plt.ylabel('Total Marks')
plt.show()

# Horizontal Bar Plot – Average Scores
plt.figure()
plt.barh(df['Name'], df['Average'], color='orange')
plt.title('Average Scores')
plt.xlabel('Average')
plt.ylabel('Name')
plt.show()

# Pie Chart – Average Score Distribution
plt.figure()
plt.pie(df['Average'], labels=df['Name'], autopct='%1.1f%%', startangle=90)
plt.title('Average Score Distribution')
plt.show()
