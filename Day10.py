import pandas as pd

df = pd.read_csv('milk_32.csv')
df = df.drop(columns=['Unnamed: 0'])

df.head()

df['Total Milk Production'] = df[
    'Monthly milk production: pounds per cow'] * df['Number of Cows']
df['Total Revenue'] = df['Total Milk Production'] * df['Price_Per_Pound']

year_2020 = df['Month'].str[:3] == '20-'
df[year_2020]['Total Revenue'].sum()