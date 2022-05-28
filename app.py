import streamlit as st
from multipage import MultiPage
from pages import Home,data_desc,explore,visualization

app = MultiPage()
# Add all your application here
app.add_page("Home", Home.app)
app.add_page("Data", data_desc.app)
app.add_page("Exploratory Data Analysis", explore.app)
app.add_page("Custom Visualizations", visualization.app)

# app.add_page("Upload", upload.app)
app.run()