import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt("16730_M31-4985ne-2597_gst.zc", skiprows = 7)

#mean_age = (data[:,0] + data[:,1])/2
age_endpt = data[:,0]
cumulative = data[:,12]
errpos_sfh = data[:,13]
errpos_sfh[errpos_sfh < 0] = 0
errneg_sfh = data[:,14]
errneg_sfh[errneg_sfh < 0] = 0

verterr = np.array([errneg_sfh, errpos_sfh])

#plt.(data[:,1], sfh, linestyle = '--')
#plt.xlim(7.5,8.0)
#plt.ylim(10 ** -7, 10 ** -1)
#plt.yscale('log')
plt.errorbar(age_endpt, cumulative, yerr = verterr, capsize = 2)
plt.show()
