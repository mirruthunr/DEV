import pandas as pd 
import geopandas as gpd 
import matplotlib.pyplot as plt 
 
# Sample World Dataset 
world_data = pd.DataFrame({ 
    'Country': ['United States of America', 'Canada', 'India', 'Brazil', 'China'], 
    'Value': [100, 150, 200, 80, 120] 
}) 
 
# Sample India States Dataset 
india_states_data = pd.DataFrame({ 
    'State': ['Maharashtra', 'Karnataka', 'Tamil Nadu', 'Uttar Pradesh', 'Gujarat'], 
    'Value': [50, 75, 60, 40, 30] 
}) 
 
# Sample India Districts Dataset 
india_districts_data = pd.DataFrame({ 
    'District': ['Mumbai', 'Bengaluru', 'Chennai', 'Lucknow', 'Ahmedabad'], 
    'Value': [20, 30, 25, 15, 10] 
}) 
 
# Load World Map from GeoPandas 
world_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')) 
 
# For simplicity, reuse the world map for demo purposes 
# In real applications, replace with actual shapefiles for India states/districts 
india_states_map = world_map[world_map['name'] == 'India'] 
india_districts_map = world_map[world_map['name'] == 'India'] 
 
# Merge Data with GeoDataFrames 
world_data_geo = world_map.merge(world_data, how='left', left_on='name', 
right_on='Country') 
india_states_data_geo = india_states_map.copy() 
india_states_data_geo['State'] = ['Maharashtra']  # Add dummy match 
india_states_data_geo = india_states_data_geo.merge(india_states_data, how='left', 
on='State') 
 
india_districts_data_geo = india_districts_map.copy() 
india_districts_data_geo['District'] = ['Mumbai']  # Add dummy match 
india_districts_data_geo = india_districts_data_geo.merge(india_districts_data, 
how='left', on='District') 
 
# Plot the Maps 
2117230020159 
 
fig, axs = plt.subplots(1, 3, figsize=(18, 6)) 
 
# World Map Plot 
axs[0].set_title('World Data by Country') 
world_data_geo.boundary.plot(ax=axs[0], linewidth=0.5) 
world_data_geo.plot(column='Value', ax=axs[0], legend=True, cmap='viridis', 
legend_kwds={'label': "Value by Country"}) 
 
# India States Map Plot 
axs[1].set_title('India States Data') 
india_states_data_geo.boundary.plot(ax=axs[1], linewidth=0.5) 
india_states_data_geo.plot(column='Value', ax=axs[1], legend=True, cmap='plasma', 
legend_kwds={'label': "Value by State"}) 
 
# India Districts Map Plot 
axs[2].set_title('India Districts Data') 
india_districts_data_geo.boundary.plot(ax=axs[2], linewidth=0.5) 
india_districts_data_geo.plot(column='Value', ax=axs[2], legend=True, 
cmap='coolwarm', legend_kwds={'label': "Value by District"}) 
 
plt.tight_layout() 
plt.show() 
