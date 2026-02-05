#CMD for M31
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

hdul = fits.open("16730_M31-4985ne-2597.gst.fits")
data = hdul[1].data

print(data.columns)
hdul.close()

keep = np.where((data['F606W_VEGA'] <50) & (data['F814W_VEGA']<50))
data2 = data[keep]
color = data2['F606W_VEGA']-data2['F814W_VEGA']
mag = data2['F814W_VEGA']


plt.figure()
plt.scatter(color, mag, s=1)
plt.show()
#reverse y axis
