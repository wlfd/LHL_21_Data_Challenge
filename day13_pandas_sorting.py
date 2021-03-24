import pandas as pd
wine_df = pd.read_csv('winequality-red.csv')
wine_df

# which wine had a quality of 8 or higher and residual sugar level above 5?

filter_quality = wine_df['quality'] >= 8
filter_sugar = wine_df['residual sugar'] > 5

# filtered_df = wine_df[filter_quality]
# filtered_df = filtered_df[filter_sugar]
filtered_df = wine_df[filter_quality & filter_sugar]
filtered_df


# how many wines in total had quality of 8 and 7 and a citric acid level below 0.4?

filter_citric = wine_df['citric acid'] < 0.4
filtered_df = wine_df[filter_citric]
filtered_df['quality'].value_counts()

# other solutions
wine_df[(wine_df['quality'] >= 8) & (wine_df['residual sugar'] > 5)].index
wine_df[(wine_df['quality'].isin([7,8])) & (wine_df['citric acid'] < 0.4)].count()