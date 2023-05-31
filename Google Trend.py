#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pytrends.request import TrendReq
   
pytrend = TrendReq()
pytrend.build_payload(kw_list=['baju melayu'], geo='MY')


# In[3]:


data = pytrend.interest_over_time()
print(data.head())


# In[4]:


import matplotlib.pyplot as plt

plt.plot(data.index, data['baju melayu'])
plt.show()


# In[5]:


from pytrends.request import TrendReq
import pandas as pd

pytrend = TrendReq()

# Build the payload for the search term "baju melayu"
pytrend.build_payload(kw_list=['baju melayu'])

# Get the related queries for the search term, along with their search volumes
related_queries_dict = pytrend.related_queries()

# Convert the "rising" related queries to a dataframe
keyword_suggestions_df = pd.DataFrame(related_queries_dict['baju melayu']['rising'])

# Set the column names of the dataframe
keyword_suggestions_df.columns = ['Keyword', 'Search Volume']

# Print the dataframe as a table
print(keyword_suggestions_df.to_string(index=False))


# In[6]:


from pytrends.request import TrendReq
import pandas as pd

pytrend = TrendReq()

# Loop through each year from 2017 to 2021
for year in range(2017, 2022):
    # Build the payload for the search term "baju melayu" for the current year
    pytrend.build_payload(kw_list=['baju melayu'], timeframe=f'{year}-01-01 {year}-12-31', geo='MY')

    # Get the related queries for the search term, along with their search volumes
    related_queries_dict = pytrend.related_queries()

    # Convert the "rising" related queries to a dataframe
    keyword_suggestions_df = pd.DataFrame(related_queries_dict['baju melayu']['rising'])

    # Set the column names of the dataframe
    keyword_suggestions_df.columns = ['Keyword', 'Search Volume']

    # Print the dataframe as a table for the current year
    print(f'Baju Melayu Related Queries ({year}):')
    print(keyword_suggestions_df.to_string(index=False))
    print('\n')


# In[7]:


from pytrends.request import TrendReq
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pytrend = TrendReq()

# Create an empty dictionary to store the search volumes for each related query for each year
search_volumes_dict = {}

# Loop through each year from 2017 to 2021
for year in range(2017, 2022):
    # Build the payload for the search term "baju melayu" for the current year
    pytrend.build_payload(kw_list=['baju melayu'], timeframe=f'{year}-01-01 {year}-12-31', geo='MY')

    # Get the related queries for the search term, along with their search volumes
    related_queries_dict = pytrend.related_queries()

    # Convert the "rising" related queries to a dataframe
    keyword_suggestions_df = pd.DataFrame(related_queries_dict['baju melayu']['rising'])

    # Set the column names of the dataframe
    keyword_suggestions_df.columns = ['Keyword', 'Search Volume']

    # Add the search volumes for each related query to the dictionary
    for i, row in keyword_suggestions_df.iterrows():
        keyword = row['Keyword']
        search_volume = row['Search Volume']
        if keyword in search_volumes_dict:
            search_volumes_dict[keyword][year] = search_volume
        else:
            search_volumes_dict[keyword] = {year: search_volume}

# Convert the dictionary to a dataframe
search_volumes_df = pd.DataFrame(search_volumes_dict)

# Create the heatmap using Seaborn
sns.heatmap(search_volumes_df, cmap='Blues')

# Set the title of the plot
plt.title('Baju Melayu Related Queries Search Volumes (2017-2021)')

# Show the plot
plt.show()


# In[8]:


# Set the keyword and timeframe
keyword = 'baju melayu'
timeframe = '2022-01-01 2022-12-31'

# Build the payload
pytrend.build_payload(kw_list=[keyword], timeframe=timeframe, geo='MY')

# Get the interest over time data
interest_over_time_df = pytrend.interest_over_time()

# Sort the data by descending order of search volume
sorted_df = interest_over_time_df.sort_values(by=keyword, ascending=False)

# Get the top 20 search terms with the highest volume in 2022
top_20 = sorted_df.head(20)

# Print the top 20 search terms as a table
print(top_20.to_string())


# In[ ]:





# In[ ]:




