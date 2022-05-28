import streamlit as st
from utility_functions import Lottie
from streamlit_lottie import st_lottie

def app():
    l=Lottie()
    lottie_hello=l.lottieurl("https://assets9.lottiefiles.com/packages/lf20_agpinljl.json")
    lottie_arrowRight=l.lottieurl("https://assets3.lottiefiles.com/packages/lf20_bS9j3g.json")

    _left,_right=st.columns(2)
    
    with _left:
        st.title("Welcome")
        st.subheader("Track 2: Data Analytics submission for Microsoft Engage 2022 by Daksh Bagga")
    with _right:
        l.load(lottie_hello,300,300)
    
    st.markdown("---")
    
    st.title("About the Application")
    st.subheader("Nowadays, most people turn to online portal to buy used cars, but sometimes, we need to make informed decisions in order to post a listing on such portals." 
                 "This is a simple data analytics app, which shows the data and its manual cleaning process as well as a manual Exploratory data analysis with custom visualizations as well!")
    
    st.markdown("---")
    col1,col2=st.columns([1.5,2])
    with col1:
        l.load(lottie_arrowRight,200,200)
    with col2:
         st.markdown("## Open the sidebar to navigate through the application")  
         