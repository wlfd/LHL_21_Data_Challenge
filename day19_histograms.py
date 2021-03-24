import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('boardgames.csv')
df.head(3)

# what type of distribution does the column avg_time have?
plt.figure()
plt.hist(df['avg_time'], bins = 400, range = (0,500))
plt.show()

# do games that have a avg_rating > 9.0 have longer play times?
filter = df['avg_rating'] > 9.0
df_filtered = df[filter]

plt.figure()
plt.hist(df_filtered['avg_time'], bins = 40)
plt.show()

# what type of distribution does weight have?

# what happens to the median and mean of a skewed distribution?

