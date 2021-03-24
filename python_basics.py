import pandas as pd
import matplotlib.pyplot as plt

# Jupyter Notebook
# shift + enter executes cell or creates new cell from last cell
# [number] means order position cell successfuly ran
# [*] cell is still running
# when cell is blue, price 'd' twice to delete cell
# change cell order using arrow keys

data = {'item_1': 40, 'item_2':50, 'item_3':25}

# create dataframe
df = pd.DataFrame(data)

# read csv file and turn into panda dataframe
df = pd.read_csv('file_name')

# write to csv
df.to_csv('data_out.csv')

# summarizes descriptive statistics of numerical columns in pandas DataFrame
df.describe()

# access a group of rows and columns by label(s) or a boolean array
df.loc()

# count non-NULL cells for each row or column depending on what it's called on, doesn't put in order
df.count()

# return the index(row labels) of DataFrame
df.index

# day12_data_fitlering_with_pandas

# create filter
filter_averagePrice = df['AveragePrice'] >= 2.00
filter_region = df['region'] == 'Okanagan Valley'
# apply filter to dataframe and store in new var
filtered_df = df[filter_averagePrice]
filtered_df = df[filter_averagePrice & filter_region]
# display filtered dataframe by calling var
filtered_df

# day13_sorting_with_pandas

# allows reorder dataframe in asencding/descending order given column
df.sort_values()
# sorting dataframe by column 'pH' in ascending order
df.sort_values(by = ['pH'], ascending = True)
# ascending = False for descending order
df.sort_values(by = ['pH'], ascending = False)
# sorting multiple features where we want one feature in ascending order and another in descending open -> feed Boolean list to ascending param of sort_values() fn
filtered_df.sort_values(by = ['column_1_ascending', 'column_2_descending,' 'column_3_ascending'], ascending = [True, False, True])

# count number specific value/item occured in dataframe
# best used on specific col, ideally col representing categorical data
# doesn't require any parameter
# puts into descending order of frequency
# turns into series object, no DataFrame
df.value_counts()
# categorical data refers to statistical data type of categorical var
df['column'].value_counts()

# when sorting multiple features -> place features in a list
filtered_df.sort_values(by = ['column_1', 'column_2'], ascending = False)

# day14_combining_knowledge
# pandas filter, sort_values(), pandas groupby()

# drop rows or columns by 
pd.drop()
# drop column labelled 'Unnamed: 0'
pd.drop(columns = ['Unnamed: 0']) 

# day15_data_visualization
data = {'item_1': 40, 'item_2':50, 'item_3':25}
items = list(data.keys())
quantity = list(data.values())

plt.figure() # frame, start plot with a figure
plt.bar(x = items, height = quantity) # body, declaring specific bar plot statement, can use DataFrame columns as x and height
plt.title('example bar plot') # stylistic features, adding title
plt.show() # show plot

plt.figure()
plt.barh(df['title'], df['average_rating']) # barh() horizontal bar graph
plt.show()

plt.figure()
plt.boxplot(df['numerical_data'], vert = False) # boxplot for interquartile range, min, max, outliers etc., vert = False displays boxplot horizontally
plt.show()

# day18_matplotlib_stylistic_methods

plt.figure(figsize = (14,7)) #declaring the figsize will give the user control to shape the figure to size/shape the user wants.
plt.bar(df['categorical_data'], height = df['categorical_data'], color = 'red') #We can specify the color of our columns, default is blue
plt.xlabel('This is the x axis!', fontsize = 14) #Specify a title for the x axis
plt.xticks(rotation = 'vertical') #Specifying a rotation to the x ticks, to make it easier to view large strings
plt.ylabel('This it the y axis!', fontsize = 14) #Specify a title for the y axis
plt.show()

# day20_scatterplots
# specify correlation between 2 specific numerical columns in Pandas
df['column_1'].corr(df['column_1'])