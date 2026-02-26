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

barswidth_gyr = np.abs(linear_age_endpt - linear_age_startpt) / (1e9)

cumulative = data[:,12]

errpos_csmf = data[:,13]
errpos_csmf = np.abs(errpos_csmf)
errneg_csmf = data[:,14]
errneg_csmf = np.abs(errneg_csmf)
errneg_csmf = np.where(errneg_csmf >= cumulative, cumulative, errneg_csmf)

verterr = np.array([errneg_csmf, errpos_csmf])

sort = np.argsort(LMA_gyr)
LMA_gyr_sort = LMA_gyr[sort]
cumulative_sort = cumulative[sort]

errpos_sort = (cumulative + errpos_csmf)[sort]
errneg_sort = (cumulative - errneg_csmf)[sort]

right_x = LMA_gyr_sort[-1]
right_errpos = errpos_sort[-1]
right_errneg = errneg_sort[-1]
half_barswidth_gyr = barswidth_gyr[sort][-1] / 2
right_xbar = right_x + half_barswidth_gyr


plt.figure(figsize = (5, 5), constrained_layout = True)

plt.errorbar(LMA_gyr_sort, cumulative_sort, yerr = verterr[:,sort], fmt = 'none', markersize = 4,
        ecolor = 'teal', elinewidth = 1.2, capsize = 2, zorder = 3, label = 'CSMF error')

LMA_extended = np.append(LMA_gyr_sort, right_xbar)

errpos_extended = np.append(errpos_sort, right_errpos)
errneg_extended = np.append(errneg_sort, right_errneg)

plt.fill_between(LMA_extended, errneg_extended, errpos_extended, color='hotpink', alpha=0.1)

plt.plot(LMA_extended, errpos_extended, color='orange', linewidth=1.5, label='Upper Error Best Fit')
plt.plot(LMA_extended, errneg_extended, color='cyan', linewidth=1.5, label='Lower Error Best Fit')

plt.xlabel("Linear mean age (in Gyr)")
plt.ylabel("Cumulative Stellar Mass Fraction")
plt.title("ANDIV CSMF/Age")

plt.legend()

plt.show()
