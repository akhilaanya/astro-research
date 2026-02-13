#CMD for ANDIV
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

hdul = fits.open("16730_N205-4163ne-2497.gst.fits")
data = hdul[1].data
hdul.close()

keep = np.where((data['F606W_VEGA'] <50) & (data['F814W_VEGA']<50))
data2 = data[keep]
color = data2['F606W_VEGA']-data2['F814W_VEGA']
mag = data2['F814W_VEGA']

fig, ax = plt.subplots(figsize = (15,15), constrained_layout = True)

ax.set_xlabel("F606W_VEGA - F814_VEGA", fontfamily = 'serif', fontsize = 25)
ax.set_ylabel("Apparent Magnitude", fontfamily = 'serif', fontsize = 25)
ax.invert_yaxis()
ax.set_title("N205 Color Magnitude Diagram", fontfamily = 'serif', fontsize = 30)

graph = ax.hexbin(mag, color, gridsize = 100, bins = 'log', cmap = 'magma')
bar_color = fig.colorbar(graph, ax = ax)
bar_color.set_label('amount')
plt.show()
