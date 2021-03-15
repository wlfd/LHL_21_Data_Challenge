import pandas as pd # alias pd (standard)

# df = pd.read_csv('paht/to/csv/sample.csv') # reads .csv and stores in pandas DataFrame
#DataFrame is representation of data in a table

# df.head(21) displays top 21 rows of dataframe; by default displays top 5 rows
# df.tail(4) displays bottom 4 rows of dataframe; by default bottom 5 rows 
# df.describe() provides descriptive statistics of all numerical columns
# df.unique() Number of unique items in a column
# df.shape() gets the number of rows and columns in the dataframe

# DataFrame Column Functions
# info() provides an overview of all the columns, number of non-nulls, and data types in a DataFrame
# max() gets the max value from a column
# min() gets the min value from a column
# mean() get the mean value from a column
# idxmax() gets the integer index position of the max value from a column
# idxmin() gets the integer index position of the min value from a column
# loc() gets rows (or columns) with particular labels from the index
# iloc() gets rows (or columns) with particular positions in the index (only takes integers)

# df['column_name'].max() gets max value from df column 'column_name'

df = pd.read_csv('milk.csv')
df.head()
df.describe() # count, mean, std, min, 25%, 50%, 75%, max

val_max_milk = df['Monthly milk production: pounds per cow'].min()
val_min_milk = df['Monthly milk production: pounds per cow'].max()

# print('max monthly milk production:', df['Monthly milk production: pounds per cow'].max())
# print('min monthly milk production:', df['Monthly milk production: pounds per cow'].max())

i_max_milk = df['Monthly milk production: pounds per cow'].idxmax()
i_min_milk = df['Monthly milk production: pounds per cow'].idxmin()


print(f'The maximum average milk production is {val_max_milk} during the year-month of {i_max_milk}.')
print(f'The minimum average milk production is {val_min_milk} during the year-month of {i_min_milk}.')

df.iloc[val_max_milk]
df.iloc[val_min_milk]

