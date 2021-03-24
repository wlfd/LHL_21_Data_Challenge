# df['column_name'] = df['column_name'].fillna(value = 100)
# df['column_name'] = df['column_name'].fillna(method = 'backfill')

import pandas as pd
df = pd.read_csv('milk_2.csv')

print(
    df.head(3)
)  #Inputing the value 3 inside the brackets of the df.head() function allows us to override the default value of 5.
print('\n')  #

print(df.shape)

df.info()
df.dtypes()
df.isnull().sum(axis=0)

df['Monthly milk production: pounds per cow'] = df[
    'Monthly milk production: pounds per cow'].fillna(
        value=df['Monthly milk production: pounds per cow'].median(
        ))  # need df['...'].median()
df['Number of Cows'] = df['Number of Cows'].fillna(method='ffill')

df.describe()

print("Q1: The Average monthly milk prod is {}".format(
    round(df['Monthly milk production: pounds per cow'].mean(), 4)))
print("Q2: The standard diviation for monthly milk prod is {}".format(
    round(df['Monthly milk production: pounds per cow'].std(), 4)))
print("Q3: the average number of cows is {}".format(
    round(df['Number of Cows'].mean(), 4)))
