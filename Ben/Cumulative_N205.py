import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("16730_N205-4163ne-2497_gst.zc", skiprows = 7)

mean_age = (data[:,0] + data[:,1])/2
age_endpt = data[:,0]
age_startpt = data[:,1]
linear_age_endpt = 10**age_endpt
linear_age_startpt = 10**age_startpt
linear_mean_age = 10**mean_age
LMA_gyr = linear_mean_age / (1e9)

barswidth = np.abs(linear_age_endpt - linear_age_startpt) / 1e9

cumulative = data[:,12]

errpos_csmf = data[:,13]
errpos_csmf = np.abs(errpos_csmf)
errneg_csmf = data[:,14]
errneg_csmf = np.abs(errneg_csmf)
errneg_csmf = np.where(errneg_csmf >= cumulative, cumulative, errneg_csmf)

verterr = np.array([errneg_csmf, errpos_csmf])

plt.figure(figsize = (15,15), constrained_layout = True)

plt.bar(LMA_gyr, cumulative, width = barswidth, align = 'center',
        color = 'indigo', edgecolor = 'indigo', alpha = 0.3, label = 'N205 Cumulative Stellar Mass Fraction')

plt.errorbar(LMA_gyr, cumulative, yerr = verterr, fmt = '.',markersize = 4,
             ecolor = 'teal',elinewidth = 1.2, capsize = 2, zorder = 3)

plt.xlabel("Linear mean age (in Gyr)")
plt.ylabel("Cumulative Stellar Mass Fraction")
plt.title("N205 CSMF/Age")

plt.show()
