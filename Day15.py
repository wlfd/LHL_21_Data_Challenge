import pandas as pd
import matplotlib.pyplot as plt

# data visualization -> graphical representation of information and data
# visual elements such as charts and graphs provide accessible way of understanding trends, outliers, and relationships in data
# communicate data insights and understand data better

# popular visualization plugins for Pythong -> matplotlib, plotting library
# easy to build statistical plots

# import matplotlib as plt

seeds = {
    'Vegetable' : ['Carrots', 'Tomatoes', 'Potatoes', 'Eggplant', 'Cucumbers'],
    'Seeds_Count' : [300,10,90,100,15],
    'Each_Seed_Produces': [1,140,10,5, 90]
}

df = pd.DataFrame(seeds)

# which seeds produce largest harvest?
vegetable = df['Vegetable']
potential_harvest = df['Seeds_Count'] * df['Each_Seed_Produces']

plt.figure()
plt.bar(x = vegetable, height = potential_harvest)
plt.title('Potential Harvest by Vegetable Type')
plt.show()

# setting vegetable and potential_harvest as DataFrame
# produce same graph
df['potential_harvest'] = df['Seeds_Count'] * df['Each_Seed_Produces']

plt.figure()
plt.bar(x = df['Vegetable'], height = df['potential_harvest'])
plt.title('Potential Harvest by Vegetable Type')
plt.show()