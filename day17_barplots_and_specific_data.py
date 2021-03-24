import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('books.csv')
df.head(2)

# what are the top 5 rated books in the dataset? (most ratings)
most_ratings = df.sort_values(by = ['ratings_count'], ascending = False) # head() default 5
most_ratings['title'].head()

plt.figure()
plt.barh(most_ratings['title'], most_ratings['ratings_count']) # barh() horizontal bar graph
plt.show()

# alternative
# df.sort_values(‘ratings_count’, ascending = False).head()

# what are the top 5 books with the highest average rating? filter out books that have low 'ratings_count' less than the mean
filter_low_rating_count = df['ratings_count'] > df['ratings_count'].mean()
filtered_df = df[filter_low_rating_count]

top_5 = filtered_df.sort_values(by = ['average_rating'], ascending = False).head()
top_5['title']

plt.figure()
plt.barh(top_5['title'], top_5['average_rating'])
plt.show()

# alternative
# df[ df[‘ratings_count’] > df[‘ratings_count’].mean() ].sort_values(‘average_rating’, ascending = False).head()

# what are the top 5 authors with the most books in the dataset?
top_author = df[df['book_count'].head()] # filter top 5 books with highest 'book_count'
top_author

plt.figure()
plt.barh(top_author['author'], top_author['book_count']) # authors who wrote the top 5 books sold
plt.show()

# alternative
df['authors'].value_counts().head() # top 5 most frequent author