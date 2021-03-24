import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('boardgames.csv')
df.head(2)

# what are the top 5 boardgame categories in this dataset that are not targeted for young children?
# use filter to acquire boardgames with an intended age of 13+ in 'age' column

df_over_13 = df[df['age'] >= 13]
df_over_13_cat = df_over_13.groupby('category').count()
top_5_over_13_cat = df_over_13_cat.sort_values(by = ['names'], ascending = False).head() # can use any column other than 'names' b/c all have same count()

plt.figure()
plt.bar(top_5_over_13_cat.index, top_5_over_13_cat['names'], color = 'purple') # can use any column other than 'names' b/c all have same count()
plt.xlabel('Board games categories')
plt.xticks(rotation = 'vertical') # don't need for barh(), useful for bar()
plt.ylabel('Average Rating')
plt.show()

# which categories of boardgames that are not targeted for young children are the same compared to the top 5 boardgames cateogires in the overall dataset?
top_5_cat = df['category'].value_counts().head().index # value_counts() into series object for 'category', head() returns top 5, and index returns row names

# # solutions if separate categories
# dfAdults = df[df[‘age’] >= 13]
# #Find all the unique categories, seperated at commas
# allCategories = set(", “.join(dfAdults[‘category’].unique()).split(”,"))
# allCategories = set(x.strip() for x in allCategories)

# #Find the counts of each category in the adults df
# counts = {}
# for cat in allCategories:
# counts[cat] = dfAdults[df[‘category’].str.contains(cat)][‘category’].count()

# #Create a df of just the counts
# dfCounts = pd.DataFrame({“Category”:counts.keys(),“Count”:counts.values()})
# dfCounts = dfCounts.sort_values(‘Count’,ascending=False)

# plt.figure()
# plt.bar(dfCounts[‘Category’].head(10),height=dfCounts[‘Count’].head(10))
# plt.xticks(rotation = ‘vertical’)
# plt.title(“True counts of categories of non-children board games”)
# plt.show()

#Solution
df.category.value_counts().head(10).index

plt.figure(figsize = (14,7))
plt.bar(df.category.value_counts().head().index ,height = df.category.value_counts().head(), color = 'red')
plt.title('This is a bar plot!', fontsize =14) #Specifying a title
plt.xlabel('This is the x axis!', fontsize = 14)
plt.xticks(rotation = 'vertical')
plt.ylabel('This it the y axis!', fontsize = 14)
plt.show()

age_filter = df.age >= 13
df_2 = df[age_filter]

plt.figure(figsize = (14,7))
plt.bar(df_2.category.value_counts().head(5).index ,height = df_2.category.value_counts().head(5), color = 'red')
plt.title('Top 5, for above 13!', fontsize =14) #Specifying a title
plt.xticks(rotation = 'vertical')
plt.show()