#!/usr/bin/python3

#homemade 
import LISA_GB_configuration as myGB
import LISA_noise_configuration as NOISE
import utils
#lisa
from fastgb.fastgb import FastGB
import lisaorbits
import lisaconstants
#display module
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from PIL import Image
#common
import math as m
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline as spline
#from config_manager import ConfigManager

#import for test  and future upgrade
import pandas as pd
import config_manager
from st_pages import Page, Section, show_pages, add_page_title, add_indentation

apptitle = 'FOM display facility'
im = Image.open("images/lisa.ico")
st.set_page_config(page_title=apptitle,
                   page_icon=im,
                   layout="wide")

### test shared parameter
#shared_data = ConfigManager()
#shared_data.display_parameter()

add_indentation()

config_manager.display_config()
st.write(st.session_state)

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
    
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

hist_values = np.histogram(
	data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h

filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)