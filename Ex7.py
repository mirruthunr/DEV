import pandas as p
import numpy as n
import folium as f

# Step 1 & 2: Generate random data
n.random.seed(42)
a = 100
b = n.random.uniform(37.5, 38.5, a)
c = n.random.uniform(-123, -121, a)
d = n.random.randint(1, 100, a)

# Step 3: Create DataFrame and save
e = p.DataFrame({'Latitude': b, 'Longitude': c, 'Value': d})
e.to_csv('map_data.csv', index=False)

# Step 4: Load data
e = p.read_csv('map_data.csv')
print("Basic Statistics:\n", e.describe())

# Step 5 & 6: Create map with markers
g = f.Map(location=[e['Latitude'].mean(), e['Longitude'].mean()], zoom_start=10)
for i, r in e.iterrows():
    popup = f"Value: {r['Value']}"
    f.Marker([r['Latitude'], r['Longitude']], popup=popup).add_to(g)

# Save the interactive map
g.save("interactive_map.html")
