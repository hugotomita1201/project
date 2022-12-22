# my python project
# spy_distribution


# sorry for the bad submissions, I thought that everything worked because I was only checking my local streamlit file instead of the
# streamlit on render service.
# this project is based off of a csv file of all SPY 500 stocks and their
# technical characteristics (price, market cap, p/e ratio, etc.) the aim of this
# project is to visually present distributions of stocks within the SPY 500
# based on what sector they are in and their market cap. This is done through
# a histogram and multiple scatter plots.

# I have imported modules containing the charts shown in this app through
# the eda_py.py file.


import streamlit as st
import pandas as pd
import plotly.express as px

# importing certain variables from eda_py which is the .py version of the EDA jupyter notebook within
# the project-1 folder
#from eda_py import sector_histogram, data, scatter_100, scatter_50, scatter

# from here to line 76 is eda_py.py file
data = pd.read_csv(r'spy.csv')
data = pd.DataFrame(data)
data

data.info()

data.columns = data.columns.str.lower()
data['sector'] = data['sector'].str.lower()
data['price/book'] = data['price/book'].fillna(0)

sectors = data.groupby('sector').agg(
    {'symbol': 'count'}).sort_index(ascending=True)

sector_fig = px.bar(sectors, labels={'value': '# of companies',
                                     'variable': 'legend',
                                     'symbol': '# of symbols', },
                    title='Distribution of Companies in the S&P500 by Sector')

sector_fig.show()

x = data.groupby('sector')['market cap'].count()
y = data.groupby('sector')['market cap'].sum()


mean_market_cap = pd.merge(x, y, left_index=True, right_index=True)

mean_market_cap['average_cap'] = mean_market_cap['market cap_y']//mean_market_cap['market cap_x']

avg_cap_fig = px.bar(mean_market_cap, y='average_cap',
                     labels={'average_cap': 'Market Cap',
                             'sector': 'Sector'},
                     title='Average Stock Market Cap of Each Sector')
avg_cap_fig.show()

sector_histogram = px.histogram(data, x='sector',
                                labels={'count': 'Number of Companies',
                                        'sector': 'Sector'},
                                title='Number of Companies per Sector in the S&p 500')
sector_histogram.show()

scatter = px.scatter(data, x='price', y='market cap', opacity=0.7,
                     labels={'market cap': 'Market Cap', 'price': 'Price'}, title='Scatterplot of Market Caps in the S&P500')
scatter

data_below_50 = data.query("`market cap` <= 50000000000")

scatter_50 = px.scatter(data_below_50, x='price', y='market cap', opacity=0.7,
                        labels={'market cap': 'Market Cap', 'price': 'Price'})
scatter_50
data_below_100 = data.query("`market cap` <= 100000000000")
scatter_100 = px.scatter(data_below_100, x='price', y='market cap', opacity=0.7,
                         labels={'market cap': 'Market Cap', 'price': 'Price'})
scatter_100


# title of the website
st.header("S&P 500 COMPANIES WITH FINANCIAL INFORMATION")

# creating a table of the entire dataframe in website
st.write(data)

# plotting the histogram from eda_py. this is histogram of number of stocks per sector
st.plotly_chart(sector_histogram)

# plotting a scatterplot with st.plotly_chart. this is the scatterplot of individual stock market caps
st.plotly_chart(scatter)


# creating a checkbox to show stocks that are below 50 billion in market cap.
# here if i click, it will show a scatterplot that only shows stocks below 50billion in market cap.
below_50 = st.checkbox("Show only market caps below 50 billion?")

# using if condition. if box is check(true) then we will run the st.pltly function to plot the
# chart
if below_50:
    st.plotly_chart(scatter_50)

# same thing but 100 billion
below_100 = st.checkbox("Show only market caps below 100 billion?")
# using imported scatter plot to show
if below_100:
    st.plotly_chart(scatter_100)

# conclusions:
# Through the histogram which presents the sector distributions of the SPY 500, we
# have found that the top 2 holdings of the SPY are based in healthcare and information
# technologies.
# through the scatterplot we have found that a vast majority of stocks in the spy 500
# are worth 50-100 billion usd and within the range of $0-200 per share.
