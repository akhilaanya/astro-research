#x and y for a fits file

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

hdul = fits.open("16730_N205-4163ne-2497.gst.fits")
data = hdul[1].data
hdul.close()

x = data['X']
y = data['Y']

plt.figure()
plt.scatter(x, y, s=1)
plt.show()
