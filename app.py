import streamlit as st
import pandas as pd
import plotly.express as px

#importing certain variables from eda_py which is the .py version of the EDA jupyter notebook within
#the project-1 folder
from eda_py import sector_histogram, data, scatter_100, scatter_50, scatter

#title of the website
st.header("S&P 500 COMPANIES WITH FINANCIAL INFORMATION")

#creating a table of the entire dataframe in website
st.write(data)

#plotting the histogram from eda_py. this is histogram of number of stocks per sector
st.plotly_chart(sector_histogram)

#plotting a scatterplot with st.plotly_chart. this is the scatterplot of individual stock market caps
st.plotly_chart(scatter)


#creating a checkbox to show stocks that are below 50 billion in market cap. 
#here if i click, it will show a scatterplot that only shows stocks below 50billion in market cap. 
below_50 = st.checkbox("Show only market caps below 50 billion?")

#using if condition. if box is check(true) then we will run the st.pltly function to plot the 
#chart
if below_50: 
    st.plotly_chart(scatter_50)

#same thing but 100 billion
below_100 = st.checkbox("Show only market caps below 100 billion?")
#using imported scatter plot to show
if below_100: 
    st.plotly_chart(scatter_100)
