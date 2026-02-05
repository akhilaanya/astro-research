import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt("16730_M31-4985ne-2597_gst.zc", skiprows = 7)

mean_age = (data[:,0] + data[:,1])/2
sfh = data[:,3]
errpos_sfh = data[:,4]
errpos_sfh[errpos_sfh < 0] = 0
errneg_sfh = data[:,5]
errneg_sfh[errneg_sfh < 0] = 0

verterr = np.array([errneg_sfh, errpos_sfh])

plt.step(data[:,1], sfh, linestyle = '--')
#plt.xlim(7.5,8.0)
plt.ylim(10 ** -7, 10 ** -1)
plt.yscale('log')
plt.errorbar(mean_age, sfh, yerr = verterr, fmt='o', markersize = 5, capsize = 2)
plt.show()
