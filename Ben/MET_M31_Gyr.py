import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("16730_M31-4985ne-2597_gst.zc", skiprows = 7)

mean_age = (data[:,0] + data[:,1])/2
age_endpt = data[:,0]
age_startpt = data[:,1]

linear_age_endpt = 10**age_endpt
LAE_gyr = linear_age_endpt / 1e9

linear_age_startpt = 10**age_startpt
LAS_gyr = linear_age_startpt / 1e9

linear_mean_age = 10**mean_age
LMA_gyr = linear_mean_age / (1e9)

metallicity = data[:,6]

errpos_met = data[:,7]
errpos_met[errpos_met < 0] = 0
errneg_met = data[:,8]
errneg_met[errneg_met < 0] = 0

verterr = np.array([errneg_met, errpos_met])

plt.hlines(metallicity,LAS_gyr, LAE_gyr, colors = 'blue', linestyle = '--')

plt.gca().invert_xaxis()


plt.errorbar(LMA_gyr, metallicity, yerr = verterr, fmt='o',
             markersize = 5, capsize = 2)

plt.xlabel("Linear mean age in Gyr; oldest on left")
plt.ylabel("Best-fit metallicity")
plt.title("M31 Metallicity/Age")


plt.show()
