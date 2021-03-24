import pandas as pd
df = pd.read_csv('avocado.csv', index_col = 0)

filter_AveragePrice = df['AveragePrice'] >= 2.00
filtered_df = df[filter_AveragePrice]

filtered_df # display filtered dataframe

filtered_df.groupby(['year', 'type']).count()

# groupby first then filter
# filter_AveragePrice = df['AveragePrice'] >= 2.00
# group_year_type = df.groupby(['year', 'type']).max()
# filtered_df = group_year_type[filter_AveragePrice]
