""" Display the waterfall plot """

#!/usr/bin/python3

# display module
import plotly.graph_objects as go
import streamlit as st
from PIL import Image
import numpy as np

from st_pages import add_indentation, add_page_title
from config_manager import ConfigManager

##############################################################################
# Title gestion
apptitle = "FOM display facility"
im = Image.open("images/lisa.ico")
st.set_page_config(page_title=apptitle, page_icon=im, layout="wide")

add_indentation()
add_page_title()


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

# pylint: disable=unused-variable
[z_mesh, Msource_mesh, SNR_mesh, SNR_std_mesh, waveform_params, pop] = T

SN_cl = np.clip(SNR_mesh, 1.0, 4000)
tickvals = [10, 20, 50, 100, 200, 500, 1000, 4000]
fig2 = go.Figure(
    data=go.Contour(
        x=Msource_mesh[0, :],
        y=z_mesh[:, 0],
        z=np.log10(SN_cl),
        colorbar=dict(
            title="Signal Noise Ratio",
            titleside="top",
            tickvals=np.log10(tickvals),
            ticktext=tickvals,
        ),
    )
)
# update axis of the plot
fig2.update_xaxes(type="log")
# update title of axis
fig2["layout"]["yaxis"].title = "Redshift"
fig2["layout"]["xaxis"].title = "Total mass"

st.plotly_chart(fig2, theme=None, use_container_width=True)

with open("notebooks/waterfallPlot.ipynb", "r", encoding="utf-8") as file:
    st.download_button(
        label="Download as a notebook",
        data=file,
        file_name="waterfall_plot_generation_display.ipynb",
        mime="application/x-ipynb+json",
    )

with open("installationInstruction.md", "r", encoding="utf-8") as file:
    st.download_button(
        label="Download installation guide",
        data=file,
        file_name="installation_guide.md",
        mime="text/markdown",
    )
