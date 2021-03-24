import pandas as pd
df = pd.read_csv('avocadoes.csv', index_col = 0)
df.head() # shows first 5 row by default

groupRegionYear = df.groupby(['region', 'year']).mean() # mean() is aggregate fn
df.head() 

groupRegionYear.loc[('Albany', 2017)] # loc[(column1, column2)]