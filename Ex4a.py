import pandas as pd

data_temp = {
    'City': ['Chennai', 'Chennai', 'Chennai', 'Delhi', 'Delhi', 'Delhi', 'Mumbai', 'Mumbai', 'Mumbai'],
    'Month': ['June', 'July', 'August', 'June', 'July', 'August', 'June', 'July', 'August'],
    'Week': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'Temperature': [36, 38, 37, 40, 42, 41, 32, 34, 33]
}

df_temp = pd.DataFrame(data_temp)
grouped_temp = df_temp.groupby(['City', 'Month'])['Temperature'].sum().reset_index()
pivot_temp = grouped_temp.pivot(index='City', columns='Month', values='Temperature').fillna(0)
print("Pivot Table (City vs. Month Temperature Sum):\n")
print(pivot_temp)
pivot_temp['Summer_Total'] = pivot_temp[['June', 'July', 'August']].sum(axis=1)
max_city = pivot_temp['Summer_Total'].idxmax()
print("\nCity with highest total summer temperature:", max_city)
