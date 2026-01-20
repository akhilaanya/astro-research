#RA and Dec for a fits file

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

hdul = fits.open("16730_N205-4163ne-2497.gst.fits")
data = hdul[1].data

print(data.columns)
hdul.close()

ra = data['RA']
dec = data['DEC']


plt.figure()
plt.scatter(ra, dec, s=1)
#plt.hist2d(ra,dec,bins=100) #plots a 2d histogram
plt.show()
