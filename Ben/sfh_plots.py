#Plotting star formation histories

import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt("16730_N205-4163ne-2497_gst.zc", comments="#")

age_endpt = data[:,0]
sfh = data[:,3]
poserr_sfh = data[:,4]
negerr_sfh = data[:,5]


plt.figure()
plt.scatter(age_endpt, sfh, s=1)
plt.show()
