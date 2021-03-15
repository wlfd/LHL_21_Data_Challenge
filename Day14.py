import pandas as pd
df = pd.read_csv('winequality-red_2.csv')
df = df.drop(columns = ['Unnamed: 0'])
df.head()

# Where is Stellenbosch? How many wines from Stellenbosch are there in the entire dataset? 
df.groupby(['region']).count() # groupby 'region' then count for each region category
df['region'].value_counts() # same as above

# filter by:
# sulfates cannot be higher than 0.6
# price has to be less than $20
filter_sulfate = df['sulphates'] <= 0.6
filter_price = df['price'] < 20
filtered_df = df[filter_sulfate & filter_price]

# After filtering, what is the average price of wine from the Bordeaux region?
filtered_df.groupby(['region']).mean()

# After filtering, what is the least expensive wine that's of the highest quality from the Okanagan Valley?
filtered_df = filtered_df['region'] == 'Okanagan Valley'
filtered_df.sort_values(by = ['quality', 'price'], ascending = [False, True])