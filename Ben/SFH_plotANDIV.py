import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("16730_ANDIV-601sw-6792_gst.zc", skiprows = 7)

mean_age = (data[:,0] + data[:,1])/2
age_endpt = data[:,0]
age_startpt = data[:,1]
linear_age_endpt = 10**age_endpt
linear_age_startpt = 10**age_startpt
linear_mean_age = 10**mean_age
LMA_gyr = linear_mean_age / (1e9)

sfh = data[:,3]

errpos_sfh = data[:,4]
errpos_sfh[errpos_sfh < 0] = 0
errneg_sfh = data[:,5]
errneg_sfh[errneg_sfh < 0] = 0

verterr = np.array([errneg_sfh, errpos_sfh])

plt.step(LMA_gyr, sfh, linestyle = '--')

#plt.gca().invert_xaxis()

#plt.ylim(10 ** -7, 10 ** -1)
plt.yscale('log')

plt.errorbar(LMA_gyr, sfh, yerr = verterr, fmt='o', markersize = 5, capsize = 2)

plt.xlabel("Linear mean age; oldest on left")
plt.ylabel("Best-fit SFH")
plt.title("ANDIV SFH/Age")


plt.show()


