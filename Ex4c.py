import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load Titanic dataset
df = sns.load_dataset('titanic')

# Display first few rows
print("🔹 First 5 Rows of Titanic Dataset:\n")
print(df.head())

# ------------------ Visualization 1 ------------------
# Survival count by gender
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='sex', hue='survived', palette='Set2')
plt.title("Survival Count by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.tight_layout()
plt.show()

# ------------------ Visualization 2 ------------------
# Average age by class (future-proof: errorbar=None)
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x='class', y='age', hue='class', palette='pastel', errorbar=None, legend=False)
plt.title("Average Age by Passenger Class")
plt.xlabel("Class")
plt.ylabel("Average Age")
plt.tight_layout()
plt.show()

# ------------------ Visualization 3 ------------------
# Pie chart of survival rate
plt.figure(figsize=(5, 5))
surv_counts = df['survived'].value_counts()
plt.pie(surv_counts,
        labels=["Did not survive", "Survived"],
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette("Set2"))
plt.title("Survival Rate (Pie Chart)")
plt.axis('equal')
plt.tight_layout()
plt.show()
