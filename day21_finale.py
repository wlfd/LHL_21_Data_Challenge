import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('video_games.csv')
df.head(2)

# what is the correlation between Critic_Score and User_score?
# may have to clean some of the columns and fill it with the median value

# plot the top 5 best selling games relased before the year 2000
# use Global_Sales

# Create a new column called Aggregrate_Score, which returns the proportional average between Critic Score and User_Score based on Critic_Score and User_Count.
# Plot a horizontal bar chart of the top 5 highest rated games by Aggregrate_Score, not published by Nintendo before the year 2000.
# From this bar chart, what is the highest rated game by Aggregate_Score?
# Critic_Count should be filled with the mean. User_Count should be filled with the median. 
