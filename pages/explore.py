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
    
    col1,col2=st.columns([2,1.2])
    with col1:
        st.markdown("# Let's Analyze the data and try to answer some queries! ")
    with col2:
        lottie_analyze=l.lottieurl("https://assets3.lottiefiles.com/packages/lf20_bdlrkrqv.json")
        l.load(lottie_analyze,250,250)
    
    
    st.markdown("## Which body type has the highest sales price?")
    fig1= plt.figure(figsize=(12,8))
    sns.barplot(df1['body_type'],df1['sale_price'])
    st.pyplot(fig1)
    st.markdown("### As we can see, Luxury SUV has some of the highest sale prices")       
    
    st.markdown("---")
    
    st.markdown("## Which body type has the highest cumulative sales?")
    fig2=px.pie(df1,values="sale_price", names="body_type")
    st.write(fig2)
    st.markdown("### Now, Hatchbacks are having most of the market share!")
    st.markdown("### Even though Hatchbacks have lower price, their market share is more")
    
    st.markdown("---")
    
    st.markdown("## Which body type is most viewed?")
    fig3=px.pie(df1, values="times_viewed",names="body_type")
    st.write(fig3)
    st.markdown("### Now again, as we can see, hatchbacks are the most viewed body type!")
    
    st.markdown("---")
    
    st.markdown("## How year of manufacture can affect the sales price (Based on the body type)?")
    fig4=plt.figure(figsize=(12,8))
    sns.lineplot(x='yr_mfr',y='sale_price',data=df,hue='body_type')
    st.pyplot(fig4)
    st.markdown("### As we can see, the variation in the prices is dependant on year of manufacture!")
    
    st.markdown("---")
    
    st.markdown("## What are the top 10 listed brands on the used cars sphere")
    col1,col2=st.columns([1,2])
    with col1:
        brand_count=pd.DataFrame(df1.make.value_counts())
        st.dataframe(brand_count.head(10))    
    with col2:
        st.text("\n\n\n")
        st.markdown("### As we can see, Maruti has the highest listings followed by hyundai,honda,toyota,renault etc")
    
    st.markdown("---")
    
    st.markdown("## Which of the brands have the highest sale based on car's year of manufacture?")

    carsales_year_df = pd.DataFrame(df1.groupby('yr_mfr').make.value_counts())
    carsales_year_df.rename(columns={'make':'sales'}, inplace=True)
    carsales_year_df.reset_index(inplace=True)

    fig=plt.figure(figsize=(12,8))
    sns.lineplot(x='yr_mfr',y='sales',data=carsales_year_df,hue='make')
    st.pyplot(fig)
    st.markdown("### As we can see, most of the cars manufactured near 2015 has highest number of sales!")
    
    st.markdown("---")
    
    #Function that returns particular year sales
    def get_SalesByYear(year):
        return carsales_year_df[carsales_year_df.yr_mfr == year]
    # Function that returns rank of a car
    def get_CarSalesRankByYear(r):
        result = get_SalesByYear(r.yr_mfr).sales.unique()
        i, = np.where(result == r.sales)
        return i[0]+1
    
    st.markdown("## What are the recent top car brands listed? ")
    carsales_year_df['year_rank'] = carsales_year_df.apply(get_CarSalesRankByYear, axis=1)
    recenttopcars = carsales_year_df[(carsales_year_df.year_rank <=5) &  (carsales_year_df.yr_mfr >= 2009)].make.unique()  
    _col1,_col2=st.columns([1,2])
    with _col1:
        st.write(recenttopcars) 
    with _col2:
        st.markdown("### As we can see, based on the calculated year rankings, these are the most recent top manufacturers")
    
    st.markdown("---")
    
    st.markdown("## Which car brand is most viewed(Amongst the top 10 viewed brands)? ")
    brand_views_df=pd.DataFrame(df1.groupby('make').times_viewed.sum())
    brand_views_df.rename(columns={'make':'views'}, inplace=True)
    brand_views_df.reset_index(inplace=True)
    brand_views_df=brand_views_df.sort_values(by=['times_viewed'], ascending=False, ignore_index=True)
    brand_views_df=brand_views_df.head(10)    
    fig6=px.pie(brand_views_df,values='times_viewed', names='make')
    st.write(fig6)
    st.markdown("### As we can see, Maruti is the most viewed brand")
    
    st.markdown("---")
    
    st.markdown("## Which city has the most number of listings?")
    fig7 = px.histogram(df1,x="city")
    st.write(fig7)
    st.markdown("### As we can see, Mumbai has the highest number of listings")
    
    st.markdown("---")
    
    st.markdown("## Which Transmission is more famous amongst the listings? ")
    fig8 = px.histogram(df1,x="transmission")
    st.write(fig8)
    st.markdown("### As we can see, Manual transmission has the highest number of listings")

    st.markdown("---")
    
    st.markdown("## What is the relation between sales price and year of manufacture (Based on the transmission)?")
    fig9=plt.figure(figsize=(12,8))
    sns.lineplot(x='yr_mfr',y='sale_price',data=df1,hue='transmission')
    st.pyplot(fig9)
    st.markdown("### We can observe the variation in prices of cars of two transmission categories in relation to their manufacturing year.")
    
    st.markdown("---")
    
    st.markdown("## How does total owners affect the sales price? ")
    fig10=plt.figure(figsize=(12,8))
    sns.lineplot(x='total_owners',y='sale_price',data=df1)
    st.pyplot(fig10)
    st.markdown("### We can observe the variability in prices of cars of two transmission categories in relation to their total_owners.We can see if total_owners are more the price of that car is generally less")
    
    st.markdown("---")
    
    st.markdown("## Which transmission category is more expensive? ")
    fig11=plt.figure(figsize=(12,8))
    sns.barplot(df1['transmission'],df1['sale_price'])
    st.pyplot(fig11)
    st.markdown("### As we can see, Automatic is generally more expensive")
    
    st.markdown("---")
    
    st.markdown("## Which city has the most expensive listings? ")
    fig12=plt.figure(figsize=(20,10))
    sns.barplot(df1['city'],df1['sale_price'])
    st.pyplot(fig12)
    st.markdown("### As we can see, Chennai has the most expensive used cars!")
    
    st.markdown("---")
    
    c1,c2=st.columns(2)
    with c1:
        st.text("\n\n\n\n\n")
        st.markdown("## We can use all these observations to make informed decisions in the Used Cars segment")
    with c2:
        lottie_analyst=l.lottieurl("https://assets3.lottiefiles.com/packages/lf20_5tl1xxnz.json")
        l.load(lottie_analyst, 350,350)