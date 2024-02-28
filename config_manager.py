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

#import for test and future upgrade
import pandas as pd

def display_config():
    st.session_state.update(st.session_state)

    st.sidebar.header('Common configuration')

    # initialisation for first run
    if "noise_budget" not in st.session_state:
        st.session_state['noise_budget'] = "config 1"
    if "duration" not in st.session_state:
        st.session_state['duration'] = "4 years"

    # setup noise config
    st.sidebar.radio("Select your noise configuration", ["config 1","config 2", "config 3"], key = "noise_budget")

    # setup mission duration
    st.sidebar.radio("Select the mission duration", ["4 years","7 years"], key = "duration")
