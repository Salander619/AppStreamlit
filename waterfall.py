import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import matplotlib as mpl

import plotly.express as px
import plotly.graph_objects as go

fn = "data/data_SO2a_snr_waterfall.c0.pkl"
T = np.load(fn, allow_pickle=True)
[z_mesh, Msource_mesh, SNR_mesh, SNR_std_mesh, waveform_params, pop] = T
   
levels = [10, 20, 50, 100, 200, 500, 1000, 4000]#, 2000, 4000, 2.e4]

cmap = plt.get_cmap('PiYG')
cmap = plt.cm.coolwarm
fig, ax = plt.subplots(1,1, figsize=[20,10])

SN_cl = np.clip(SNR_mesh, 1., 4000)#None)
cs1 = ax.contourf(Msource_mesh, z_mesh, SN_cl, levels=levels,
                  locator=ticker.LogLocator(), norm=mpl.colors.LogNorm(),
                  cmap=cmap)
#ax.clabel(cs1, fmt='%2.1f', colors='k', fontsize=14)
cbar = fig.colorbar(cs1, ax=ax)
ax.set_xscale('log')

plt.show()