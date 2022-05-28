import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import plotly.express as px
from utility_functions import Lottie,functions

def app():
    
    #Loading the required utility functions
    l=Lottie()
    f=functions()
    
    #Reading the Data
    df=pd.read_csv('data/used-cars.csv')
    
    #Horizontal menu to browse through
    top_menu = option_menu(None, ["Data Description", "Data Cleaning"], 
    icons=['journal-code', 'eraser','gear'], default_index=0, orientation="horizontal")
    top_menu
    
    #If we select Data Description in the horizontal option menu, we get this page
    if top_menu == "Data Description":
        
        #Adding arrowDown lottie animation    
        lottie_arrowDown=l.lottieurl("https://assets5.lottiefiles.com/packages/lf20_yky74my9.json")
        
        #Dividing the page into columns and then filling in data, just to make it look good
        col1,col2=st.columns([2,1])
        with col2:
            l.load(lottie_arrowDown,200,200)
        with col1:
            st.title("This is the True Value Used Cars Data used in this project")
        
        st.markdown("This dataset contains over **7000+** true value cars data across all major tier 1 and tier 2 cities in India which is ready to accept a different owner. The information includes car manufacturer, model, fuel type, year of manufacture to mention a few")
        
        #Adding a checkbox to dynamically display the dataset, with custom row count as input
        if st.checkbox("Show Dataset"):
            st.write("### Enter the number of rows to view")
            rows = st.number_input("", min_value=0,value=5)
            if rows > 0:
                st.dataframe(df.head(rows))
        
        #Manually adding description for each column
        with st.expander("Columnwise Description"):
            st.text("id: Unique ID for every car \n"
                    "car_name: Name of a car \n"
                    "yr_mfr: Car manufactured year \n"
                    "fuel_type: Type of fuel car runs on \n"
                    "kms_run: Number of kilometers run \n"
                    "body_type: Car body type. Ex: Sedan, hatchback etc. \n"
                    "transmission: Type of transmission. Ex: Manual, Automatic \n"
                    "variant: Car variant \n"
                    "make: Car manufacturing company \n"
                    "model: Car model name \n"
                    "is_hot: Is it a top selling car? Indicates the demand for a car. \n"
                    "car_availability: Car availability status \n"
                    "total_owners: How many owners have already owned it? \n"
                    "car_rating: How good is the car to buy? \n"
                    "fitness_certificate: Does the car have fitness certificate? \n"
                    "source: Method of selling a car \n"
                    "registered_city: City where the car is registered \n"
                    "registered_state: State where the car is registered \n"
                    "rto: Regional Transport Office where the car is registered \n"
                    "city: City where the car is being sold \n"
                    "times_viewed: Number of times people have shown interest for the car \n"
                    "assured_buy: Broker assured car \n"
                    "broker_quote: Price quoted for previous owner (in INR) \n"
                    "original_price: Original price of a car (in INR) \n"
                    "emi_starts_from: Opting for EMI? Monthly EMI for the car starts from! (in INR) \n"
                    "booking_down_pymnt: Decided to buy? Please pay the down payment (in INR) \n"
                    "ad_created_on: Listed date for selling a car \n"
                    "reserved: Car reserved status \n"
                    "warranty_avail: Warranty availability status` \n"
                    "sale_price: Selling price of a car (in INR) \n")
        if st.checkbox("Show dataset with selected columns"):
        # get the list of columns
            columns = df.columns.tolist()
            st.write("#### Select the columns to display:")
            selected_cols = st.multiselect("", columns)
            if len(selected_cols) > 0:
                selected_df = df[selected_cols]
                st.dataframe(selected_df)
        
        #User can download the dataset used using this button
        st.download_button(label='Download Dataset',data=df.to_csv(),mime='text/csv')
        
        
        
    #If we select Data Cleaning in the horizontal option menu, we get this page
    if top_menu == "Data Cleaning":
        
        #Separating the workspace into 2 parts to show the header
        c1,c2=st.columns([2,1])
        with c1:
            st.markdown("## Let's Clean the data")
            st.markdown("### By doing a thorough null value analysis")
        with c2:
            lottie_clean=l.lottieurl("https://assets5.lottiefiles.com/packages/lf20_qwbfemni.json")
            l.load(lottie_clean,200,200)
        
        #Works as horizontal rule
        st.markdown("---")
        
        #Showing the Data Correlation for Analysis
        st.markdown("## Let's First checkout the correlation between the data points")
        st.markdown("### Data Correlation")        
        st.write(df.corr())
        
        #Plotting a dynamic heatmap using the plotly express library and printing observation
        st.markdown("## Heatmap based on this correlation")
        fig1 = px.imshow(df.corr(),text_auto=".2f",width= 600,height=600)
        st.write(fig1)
        st.write("emi_starts_from , booking_down_payment,original_price,broker_qoute are highly correlated")
        
        st.markdown("---")
        
        #Showing the null value analysis by splitting the workspace into 2 parts
        col1,col2=st.columns(2)
        with col1:
            st.markdown("## Now, let's see the null value analysis ")
            st.markdown("#### Here original_price column contains more null values")
        with col2:
            st.write(df.isnull().sum())
        
        st.markdown("---")
        
        #An alternative for line break in streamlit
        st.text("\n")
        st.markdown("### As we can see the data is not looking linear, and has plenty of null values to fix this, let's try cleaning the dataframe by dropping some columns")
        
        #Using the remove function, from the functions class of Utility_functions.py(more details there)
        st.markdown("##### Dropping id,emi_starts_from,original_price,broker_quote columns from our current data")
        df1=f.remove(df)
        
        #Printing the dataframe with substantially lesser null values
        with st.expander("Checkout the new dataframe: "):
            st.dataframe(df1)
        st.markdown("---")
        
        #Again Showing the null value analysis by splitting the workspace into 2 parts
        _col1,_col2=st.columns([1,2])
        with _col2:
            st.markdown("## Now, let's see the null value analysis again")
        with _col1:
            st.write(df1.isnull().sum())
        st.markdown("---")
        
        #Using the replace_missing_value function, from the functions class of Utility_functions.py(more details there)
        st.markdown("### Replacing the remaining missing values with their mean(for integer columns) and mode(for object columns): ")        
        f.replace_missing_values(df1)
        with st.expander("Checkout the new dataframe: "):
            st.dataframe(df1)
        
        #Again Showing the null value analysis by splitting the workspace into 2 parts
        __col1,__col2=st.columns([2,1])
        with __col1:
            st.markdown("## Now, let's see the null value analysis again")
            st.markdown("#### As we can see, there are no missing values in the data now..")
        with __col2:
            st.write(df1.isnull().sum())
        st.markdown("---")
        
        st.text("\n\n\n\n")
        
        #Null value analysis completed, showing the results
        st.markdown("## The data cleaning process is done, now let's compare the correlation heatmaps")
        _fig1=px.imshow(df.corr(),text_auto=".2f",width=400,height=400)
        fig2=px.imshow(df1.corr(),text_auto=".2f",width=400,height=400)
        
        #Comparing both heatmaps again by splitting the workspace into 2 parts
        left,right=st.columns(2)
        with left:
            st.markdown("#### Old dataframe")
            st.write(_fig1)
        with right:
            st.markdown("#### New dataframe")
            st.write(fig2)
        st.text("\n\n\n\n")
        st.markdown("---")
        
        lottie_done = l.lottieurl("https://assets10.lottiefiles.com/private_files/lf30_z1sghrbu.json")
        cols1,cols2=st.columns([0.6,2.4])
        with cols1:
            l.load(lottie_done,150,150)
        with cols2:
            st.text("\n\n\n")
            st.markdown(" ## Finally, our dataset is clean with no null values")