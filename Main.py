#!/usr/bin/python3

import streamlit as st
from PIL import Image
import config_manager

from st_pages import Page, Section, show_pages, add_page_title, add_indentation

#### main init
apptitle = 'FOM display facility'
im = Image.open("images/lisa.ico")
st.set_page_config(page_title=apptitle,
                   page_icon=im,
                   layout="wide")

add_page_title()

config_manager.display_config()
st.write(st.session_state)

# pages and sections gestion
show_pages(
    [
        Page("main.py", "Home"),

        Section(name="FOM"),

        Page("pages/sensitivity_plot.py", "Sensitivity"),
        Page("pages/waterfall_plot.py", "Waterfall"),

        Section(name="Tests for fun"),

        Page("pages/app_uber.py", "App uber from Streamlit doc"),
    ]
)