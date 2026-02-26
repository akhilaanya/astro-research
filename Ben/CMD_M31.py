#CMD for M31
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

hdul = fits.open("16730_M31-4985ne-2597.gst.fits")
data = hdul[1].data
hdul.close()

keep = np.where((data['F606W_VEGA'] <50) & (data['F814W_VEGA']<50))
data2 = data[keep]
color = data2['F606W_VEGA']-data2['F814W_VEGA']
mag = data2['F814W_VEGA']

fig, ax = plt.subplots(figsize=(15, 15), constrained_layout=True)

ax.set_xlabel("Apparent Magnitude", fontfamily = 'serif', fontsize = 25)
ax.set_ylabel("F606W_VEGA - F814W_VEGA", fontfamily = 'serif', fontsize = 25)
ax.invert_yaxis()
ax.set_title("M31 Color-Magnitude Diagram", fontfamily = 'serif', fontsize = 30)

graph = ax.hexbin(color, mag, gridsize=100, bins = 'log', cmap = 'plasma')
bar_color = fig.colorbar(graph, ax=ax)
bar_color.set_label('amount')
plt.show()
