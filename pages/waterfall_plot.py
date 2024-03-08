""" Display the waterfall plot """

#!/usr/bin/python3

# display module
import plotly.graph_objects as go
import streamlit as st
from PIL import Image
import numpy as np

from st_pages import add_indentation
from config_manager import ConfigManager  # pylint: disable=import-error

##############################################################################
# Title gestion
apptitle = "FOM display facility"
im = Image.open("images/lisa.ico")
st.set_page_config(page_title=apptitle, page_icon=im, layout="wide")

add_indentation()


##############################################################################
@st.cache_data
def load_data(path_to_file):
    """load the datafile"""
    return np.load(path_to_file, allow_pickle=True)


##############################################################################

cm = ConfigManager("Waterfall", True, False)

cm.display_config()

##############################################################################
# loading the data

fn = None
if st.session_state["noise_budget"] == "scird":
    fn = "data/data_SO2a_snr_waterfall.c0_scird.pkl"
else:
    fn = "data/data_SO2a_snr_waterfall.c0.pkl"

T = load_data(fn)

[z_mesh, Msource_mesh, SNR_mesh, __, __, __] = T

SN_cl = np.clip(SNR_mesh, 1.0, 4000)

##############################################################################
# create the plot

fig2 = go.Figure(
    data=go.Contour(
        x=Msource_mesh,
        y=z_mesh,
        z=SN_cl,
        colorbar={"title": "Signal Noise Ratio", "titleside": "top"},
    )
)

# update axis of the plot
fig2.update_xaxes(type="log")
fig2.update_layout(width=500, height=500, yaxis_range=[0, 25], xaxis_range=[1, 2])
# set size of plot and min/max of axis (x is in log mode so range is 10 to 100)
fig2.update_traces(zmin=10, zmax=10000)  # set min and max of colorbar

# update title of axis
fig2["layout"]["yaxis"].title = "Redshift"
fig2["layout"]["xaxis"].title = "Total mass"

st.plotly_chart(fig2, theme=None, use_container_width=True)
