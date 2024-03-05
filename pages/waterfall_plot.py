""" Display the waterfall plot """

#!/usr/bin/python3

# display module
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.graph_objects as go
import streamlit as st
from PIL import Image
from matplotlib import ticker
from matplotlib import cm
import numpy as np

from st_pages import add_indentation
import config_manager

##########################################################################################
# Title gestion
apptitle = "FOM display facility"
im = Image.open("images/lisa.ico")
st.set_page_config(page_title=apptitle, page_icon=im, layout="wide")

add_indentation()


##########################################################################################
# definition of data loading function
@st.cache_data
def load_data(path_to_file):
    return np.load(path_to_file, allow_pickle=True)


##########################################################################################
### test shared parameter
config_manager.display_config()
st.write(st.session_state)

##########################################################################################
# loading the data
st.sidebar.title("Waterfall configuration")
data_to_load = st.sidebar.radio(
    "Configuration selection :", ["default", "scird"], key="data_waterfall"
)

fn = None
if data_to_load == "scird":
    fn = "data/data_SO2a_snr_waterfall.c0_scird.pkl"
else:
    fn = "data/data_SO2a_snr_waterfall.c0.pkl"

T = load_data(fn)

[z_mesh, Msource_mesh, SNR_mesh, SNR_std_mesh, waveform_params, pop] = T
# z_mesh = , Msource_mesh = , SNR_mesh = , reste = metadatas

levels = [10, 20, 50, 100, 200, 500, 1000, 4000]  # , 2000, 4000, 2.e4]

##########################################################################################
# with matplotlib

cmap = plt.get_cmap("PiYG")
cmap = cm.coolwarm
fig, ax = plt.subplots(1, 1, figsize=[20, 10])

SN_cl = np.clip(SNR_mesh, 1.0, 4000)  # None)
cs1 = ax.contourf(
    Msource_mesh,
    z_mesh,
    SN_cl,
    levels=levels,
    locator=ticker.LogLocator(),
    norm=mpl.colors.LogNorm(),
    cmap=cmap,
)
# ax.clabel(cs1, fmt='%2.1f', colors='k', fontsize=14)
cbar = fig.colorbar(cs1, ax=ax)
ax.set_xscale("log")

st.pyplot(fig, True)

##########################################################################################
# with plotly

# create the plot
fig2 = go.Figure(
    data=go.Contour(
        x=Msource_mesh,
        y=z_mesh,
        z=SN_cl,
        colorbar=dict(title="Signal Noise Ratio", titleside="top"),
    )
)

# update axis of the plot
fig2.update_xaxes(type="log")
fig2.update_layout(
    width=500, height=500, yaxis_range=[0, 25], xaxis_range=[1, 2]
)  # set size of plot and min/max of axis (x is in log mode so range is 10 to 100)
fig2.update_traces(zmin=10, zmax=10000)  # set min and max of colorbar

# update title of axis
fig2["layout"]["yaxis"].title = "Redshift"
fig2["layout"]["xaxis"].title = "Total mass"

st.plotly_chart(fig2, theme=None, use_container_width=True)
