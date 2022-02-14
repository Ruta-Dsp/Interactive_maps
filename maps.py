import streamlit as st 
import pandas as pd 
import numpy as np 
import pydeck as pdk 
import altair as alt 
from datetime import datetime



DATA_URL = ('https://raw.githubusercontent.com/nikkisharma536/streamlit_app/master/covid.csv')
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
    return data
df = load_data()

# show data on streamlit
 st.write(df)