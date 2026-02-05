import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt("16730_ANDIV-601sw-6792_gst.zc", skiprows = 7)

age_endpt = data[:,0]
sfh = data[:,3]
errpos_sfh = data[:,4]
errpos_sfh[errpos_sfh < 0] = 0
errneg_sfh = data[:,5]
errneg_sfh[errneg_sfh < 0] = 0

verterr = np.array([errneg_sfh, errpos_sfh])

plt.figure()
plt.errorbar(age_endpt, sfh, yerr = verterr, fmt='o', markersize = 2, capsize = 2)
plt.show()
