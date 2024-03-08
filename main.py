""" Entry point of our application, organize the pages into sections """

#!/usr/bin/python3

import streamlit as st
from PIL import Image
from st_pages import Page, Section, show_pages, add_page_title
import config_manager

#### main init
app_title = "FOM display facility"
im = Image.open("images/lisa.ico")
st.set_page_config(page_title=app_title, page_icon=im, layout="wide")

add_page_title()

config_manager.display_config()

# pages and sections gestion
show_pages(
    [
        Page("main.py", "Home"),
        Section(
            name="SO1: Study the formation and evolution of compact binary stars and the structure of the Milky Way Galaxy"
        ),  # pylint: disable=line-too-long
        Page("pages/sensitivity_plot.py", "Sensitivity"),
        Section(
            name="SO2: Trace the origins, growth and merger histories of massive Black Holes"
        ),  # pylint: disable=line-too-long
        Page("pages/waterfall_plot.py", "Waterfall"),
    ]
)

# page layout
st.image("image/GW_for_everyone.jpg", caption="Scope of the LISA project")
