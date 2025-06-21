import pandas as pd

data_hours = {
    'Employee': ['E1', 'E2', 'E3', 'E4', 'E5', 'E6'],
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Hours_Worked': [38, 42, 45, 44, 40, 41]
}

df_hours = pd.DataFrame(data_hours)
grouped_hours = df_hours.groupby('Department')['Hours_Worked'].agg(['sum', 'mean']).reset_index()
grouped_hours.columns = ['Department', 'Total_Hours', 'Average_Hours']
pivot_hours = grouped_hours.set_index('Department')
print("Department-wise Work Hours Summary:\n")
print(pivot_hours)
max_avg_dept = pivot_hours['Average_Hours'].idxmax()
print("\nDepartment with highest average working hours:", max_avg_dept)
