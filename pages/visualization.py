import streamlit as st
import pandas as pd
import plotly.express as px
from utility_functions import Lottie,functions
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def app():
    #Loading the required utility functions
    l=Lottie()
    f=functions()
    plt.style.use('dark_background')
    
    df=pd.read_csv('data/used-cars.csv')
    
    # Cleaning the data again
    df1=f.remove(df)
    f.replace_missing_values(df1)
    
    #Categorizing columns into category as well as integer columns
    category_columns=df1.select_dtypes(include=['object']).columns.tolist()
    integer_columns=df1.select_dtypes(include=['int64','float64']).columns.tolist()
    
    col1,col2 = st.columns(2)
    with col1:
        st.markdown("# Dynamic Custom Visualizations for Data Analysis on Used Cars Data ")
    with col2:
        lottie_visualization=l.lottieurl("https://assets7.lottiefiles.com/packages/lf20_adfauj2c.json")
        l.load(lottie_visualization,250,250)
    
    st.markdown("---")
    
    st.markdown("## Input the columns to see relationship between them")
    x_axis=st.selectbox('Select x-axis',integer_columns)
    y_axis=st.selectbox('Select y-axis',integer_columns)
    
    if st.button("Show Relation using Line Plot"):
        fig1= plt.figure(figsize=(12,8))
        sns.lineplot(x=x_axis,y=y_axis,data=df1)    
        st.pyplot(fig1)
    
    if st.button("Show Relation using Scatter Plot"):
        fig2= plt.figure(figsize=(12,8))
        sns.scatterplot(x=x_axis,y=y_axis,data=df1)    
        st.pyplot(fig2)
        
    st.markdown("---")
    
    st.markdown("## Visualizing the data with respect to a particular category ")
    x_axis=st.selectbox('Select x',integer_columns)
    y_axis=st.selectbox('Select y',integer_columns)
    hue=st.selectbox('Select the hue',category_columns)
    
    if st.button("Show Relation using Line Plot (With Hue)"):
        fig3= plt.figure(figsize=(12,8))
        sns.lineplot(x=x_axis,y=y_axis,data=df1,hue=hue)    
        st.pyplot(fig3)
    
    st.markdown("---")
    
    st.markdown("## Visualizing the data with dynamically generated Pie Chart")
    values=st.selectbox('Select the value to display', integer_columns)
    names=st.selectbox('Select the Category', category_columns)
    if st.button("Generate Pie Chart"):
        fig4= px.pie(df1,values=values,names=names)
        st.write(fig4)
    
    st.markdown("---")
    
    st.markdown("## Find out the count of categories")
    count_category=st.selectbox('Enter the Category',category_columns)
    
    if st.button("Generate Histogram"):
        fig5 = px.histogram(df1,x=count_category)
        st.write(fig5)