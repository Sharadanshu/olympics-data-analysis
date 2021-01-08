# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path

#Code starts here

# Data Loading 
data  = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)

# Summer or Winter
data['Better_Event'] = np.where(data.Total_Summer == data.Total_Winter,'Both',np.where(data.Total_Summer > data.Total_Winter,'Summer','Winter'))
better_event = pd.DataFrame(data['Better_Event'].value_counts()).idxmax().item()

# Top 10
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(data.index[len(top_countries) -1],axis=0,inplace=True)
def top_ten(df,col):
    country_list = []
    top_values=top_countries.nlargest(10, col)
    country_list = list(top_values['Country_Name'])
    return country_list
top_10_summer = top_ten(top_countries,'Total_Summer')
top_10_winter = top_ten(top_countries,'Total_Winter')
top_10 = top_ten(top_countries,'Total_Medals')
common = ((set(top_10_summer)).intersection(set(top_10_winter))).intersection(set(top_10))

# Plotting top 10

#Summer

summer_df = data[data['Country_Name'].isin(top_10_summer)]

plt.bar(summer_df.Country_Name,summer_df.Total_Medals)
plt.xlabel("Countries")
plt.ylabel("No. Of Medal")
plt.xticks(rotation = 90)
plt.title('Summer Season')
plt.show()

#Winter

winter_df = data[data['Country_Name'].isin(top_10_winter)]
plt.bar(winter_df.Country_Name,winter_df.Total_Medals)
plt.xlabel("Countries")
plt.ylabel("No. Of Medal")
plt.xticks(rotation = 90)
plt.title('Winter Season')
plt.show()

#top

top_df = data[data['Country_Name'].isin(top_10)]
plt.bar(top_df.Country_Name,winter_df.Total_Medals)
plt.xlabel("Countries")
plt.ylabel("No. Of Medal")
plt.xticks(rotation = 90)
plt.title('Both Season')
plt.show()

# Top Performing Countries

#Summer

summer_df['Golden_Ratio'] = summer_df.Gold_Summer/summer_df.Total_Summer
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df[summer_df['Golden_Ratio'] == summer_max_ratio]['Country_Name'].item()

#Winter

winter_df['Golden_Ratio'] = winter_df.Gold_Winter/winter_df.Total_Winter
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df[winter_df['Golden_Ratio'] == winter_max_ratio]['Country_Name'].item()

#Top

top_df['Golden_Ratio'] = top_df.Gold_Total/top_df.Total_Medals
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df[top_df['Golden_Ratio'] == top_max_ratio]['Country_Name'].item()

# Best in the world 
data1 = data.drop(data.index[len(data) -1],axis=0)
data1['Total_Points'] = (data1.Gold_Total * 3) + (data1.Silver_Total * 2) + (data1.Bronze_Total * 1)
most_points = data1.Total_Points.max()
best_country = data1[data1.Total_Points == most_points]['Country_Name'].item()

# Plotting the best
best = data[data.Country_Name == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot(kind='bar',stacked= True)
plt.xlabel(best_country)
plt.ylabel('Medal Tally')
plt.xticks(rotation = 45)
plt.show()



