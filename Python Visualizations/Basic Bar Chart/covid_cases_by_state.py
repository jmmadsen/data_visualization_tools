"""
1. in order to use libraries in our program, we must first import them at the top of the file
2. you can read more about methods of importing libraries in Python at https://www.geeksforgeeks.org/import-module-python/#:~:text=Import%20in%20python%20is%20similar,is%20not%20the%20only%20way.
"""
import pandas as pd
import matplotlib.pyplot as plt


# import the raw data from the csv file in this folder
csv_data = './us_states_covid_data.csv'

# read the raw data into a pandas dataframe
df = pd.read_csv(csv_data, header=0)

"""
several things are going on in line 20
1. we create a new variable, grouped_data
2. we call the group_by() function on the column 'state'
3. after grouping, we select the column 'cases' by appending ['cases'] after our groupby() function
4. we call the sum() function on 'cases' grouped by 'state', which turns our grouped_data variable into a Series
5. we then call the sort_values function on our Series in descending order
6. we limit our series to the top 10 rows using the function .iloc, and slicing from the beginning to 10
"""
grouped_data = df.groupby('state')['cases'].sum().sort_values(ascending=False).iloc[:10]

"""
1. assign a new variable, using the .plot function
2. use the .bar() function to select a graph type of bar chart
"""
ax = grouped_data.plot.bar()

# call the .legend() function to display, and supply a parameter of "best" to let matplotlib automatically choose
plt.legend(loc='best')

# display the graph
plt.show()