import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('books.csv')

# how many books over 4000 pages?
plt.figure()
plt.boxplot(df['num_pages'], vert = False)
plt.show()

# what are the average ratings for books that have over 4000 pages?
filter_pages = df['num_pages'] > 4000
filtered_df = df[filter_pages]

plt.figure()
plt.boxplot(filtered_df['average_rating'], vert = False)
plt.show # b/c only 2, look at boxplot's min and max

filtered_df
print(filtered_df['average_rating']) # b/c only 2, can print and look at average rating