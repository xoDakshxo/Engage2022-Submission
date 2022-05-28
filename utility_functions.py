import json
import requests  # pip install requests
import streamlit as st
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

class Lottie:
    def lottiefile(self, filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
    
    
    def lottieurl(self, url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    def load(self, name:str, height, width):
        st_lottie(
            name,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            # renderer="svg", # canvas
            height=height,
            width=width,
            key=None,
        ) 
class functions:
    def remove(self,df):
        df1=df.drop(['id','emi_starts_from','original_price','broker_quote'],axis=1)
        return df1
    
    def replace_missing_values(self,df):
        category_columns=df.select_dtypes(include=['object']).columns.tolist()
        integer_columns=df.select_dtypes(include=['int64','float64']).columns.tolist()
        for column in df:
            if df[column].isnull().any():
                if(column in category_columns):
                    df[column]=df[column].fillna(df[column].mode()[0])
                else:
                    df[column]=df[column].fillna(df[column].mean)
        
    
        
        