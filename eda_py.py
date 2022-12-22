#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px


# In[2]:


# creating dataframe for S&P 500 COMPANIES DATA
data = pd.read_csv(r'd:/Users/hugo/python_projects/spy_distribution/constituents_financials_csv.csv')
data = pd.DataFrame(data)
data


# In[3]:


data.info()
# need to clean up data

# start off by lowercasing all column names
data.columns = data.columns.str.lower()
# lowercase all values within the sector column
data['sector'] = data['sector'].str.lower()
# filling all na values in price/book. filling with 0 because
# only 5 values and we are not going to use those values anyways
data['price/book'] = data['price/book'].fillna(0)

# In[4]:


# Objective here is to group data by sector and create a bar chart of what types of companies make
# up the S&P 500

# creating a sectors variable and finding the number of symbols per sector using groupby and .agg
sectors = data.groupby('sector').agg(
    {'symbol': 'count'}).sort_index(ascending=True)

# Using plotly to create a bar chart to chart the number of companies per sector in the S&P 500
sector_fig = px.bar(sectors, labels={'value': '# of companies',
                                     'variable': 'legend',
                                     'symbol': '# of symbols', },
                    title='Distribution of Companies in the S&P500 by Sector')

sector_fig.show()


# In[5]:


# For 2nd chart, I will calculate the average market cap for each sector
# to do this, i will group by sector and then calculate the mean values for each market cap

# for some reason, finding the mean didnt work and gave me a higher number as a result. so resorted
# to a different method to find the average market cap for each sector.

# defining the sum() and count() of each market cap so I can divide them to get the average mkt cap.
x = data.groupby('sector')['market cap'].count()
y = data.groupby('sector')['market cap'].sum()

# creating a new merged dataframe for x and y
mean_market_cap = pd.merge(x, y, left_index=True, right_index=True)
#
mean_market_cap['average_cap'] = mean_market_cap['market cap_y']//mean_market_cap['market cap_x']

avg_cap_fig = px.bar(mean_market_cap, y='average_cap',
                     labels={'average_cap': 'Market Cap',
                             'sector': 'Sector'},
                     title='Average Stock Market Cap of Each Sector')
avg_cap_fig.show()


# In[ ]:


# In[ ]:


# In[6]:


# creating a histogram based on number of companies per sector in the S&P
# this data is exactly the same as the bar chart but since the project requirement is to create a
# hist, i will create it again but using hist method
sector_histogram = px.histogram(data, x='sector',
                                labels={'count': 'Number of Companies',
                                        'sector': 'Sector'},
                                title='Number of Companies per Sector in the S&p 500')
sector_histogram.show()


# In[8]:


# need to create a scatter plot
'''
scatter plot will be x: price and y: market cap

'''
# creating the scatter plot with px.scatter and adding parameters
scatter = px.scatter(data, x='price', y='market cap', opacity=0.7,
                     labels={'market cap': 'Market Cap', 'price': 'Price'}, title='Scatterplot of Market Caps in the S&P500')
scatter


# In[18]:


# here I want to create 2 scatterplots. 1 that will show companies below 50 billion market cap
# and another that will show companies below 100 billion market cap. for easier viewing

# below 50 billion filter with .query method
data_below_50 = data.query("`market cap` <= 50000000000")
# and then introducing a variable to be able to use with streamlit on app.py
scatter_50 = px.scatter(data_below_50, x='price', y='market cap', opacity=0.7,
                        labels={'market cap': 'Market Cap', 'price': 'Price'})
scatter_50

# repeat process
data_below_100 = data.query("`market cap` <= 100000000000")

scatter_100 = px.scatter(data_below_100, x='price', y='market cap', opacity=0.7,
                         labels={'market cap': 'Market Cap', 'price': 'Price'})
scatter_100


# In[ ]:
