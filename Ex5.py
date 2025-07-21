import pandas as p
import numpy as n
import matplotlib.pyplot as m

# Step 1: Sample dataset
a = {
    'ID': range(1, 11),
    'Age': n.random.randint(18, 60, 10),
    'Income': n.random.randint(30000, 90000, 10),
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
    'Education': ['High School', 'Bachelor', 'Master', 'PhD', 'Bachelor', 'Master', 'Bachelor', 'PhD', 'High School', 'Master']
}
b = p.DataFrame(a)

# Step 2: Display first few rows
print(b.head())

# Step 3: Check missing values
print(b.isnull().sum())

# Step 4: Variable filter
c = b[['Age', 'Income']]
print(c)

# Step 5: Row filters
d = b[b['Age'] > 30]
print(d)

e = b[b['Gender'] == 'Male']
print(e)

# Step 6: Visualization
m.hist(b['Age'], bins=5, edgecolor='black')
m.title('Age Distribution')
m.xlabel('Age')
m.ylabel('Frequency')
m.show()

m.boxplot(b['Income'])
m.title('Income Distribution')
m.ylabel('Income')
m.show()
