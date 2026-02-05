import math
import numpy as np
import matplotlib.pyplot as plt
import os.path
import glob
import matplotlib.colors as clr
import matplotlib.cm as cmx

def plot_cum_sfh(inpre,out,lab):
    plt.rcParams['axes.linewidth'] = '2'
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    fig.set_size_inches(6.0,5.0)
    zcf = inpre
    sfh = np.genfromtxt (zcf,dtype='double',skip_header=6)
    age = (10.0**(sfh[:,0]))/1.0e9
    rows = len(sfh[:,1])-1
    age = np.append(age,(10.0**(sfh[rows,1]))/1.0e9)
    frac = np.append(sfh[:,12],[0.0])
    fracerrl = np.append(sfh[:,14],[0.0])
    fracerrh = np.append(sfh[:,13],[0.0])
    doubleage = np.append(age,age)
    doublesfrlo = np.append(frac-fracerrl,frac-fracerrl)
    doublesfrhi = np.append(frac+fracerrh,frac+fracerrh)
    i = np.argsort(doubleage)
    doubleage = doubleage[i]
    doublesfrlo = doublesfrlo[i]
    doublesfrhi = doublesfrhi[i]
    doubleage=doubleage[1:(len(i)-1)] # trim ends
    doublesfrlo=doublesfrlo[2:(len(i))] # trim ends
    doublesfrhi=doublesfrhi[0:(len(i)-2)] # trim ends
    
    polyx=np.append(doubleage,doubleage[::-1])
    polyy=np.append(doublesfrhi,doublesfrlo[::-1])
    #ax.plot(age,frac,'-',linewidth=2.0,alpha=0.1)
    ax.plot(age,frac,'-',linewidth=2.0)
    ax.fill(polyx,polyy,
                #facecolor='gray',alpha=0.05, edgecolor='none')
                facecolor='gray', edgecolor='none')
    plt.ylim([0,1.05])
    plt.xlim([14,0])

    #plt.rcParams['axes.linewidth'] = '2'
    #plt.rcParams['xtick.major.pad']='10'
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=16)
    plt.xlabel('Lookback Time (Gyr)',fontsize=18)
    plt.ylabel('Cumulative Fraction of Stellar Mass',fontsize=18) 

    ax.xaxis.set_tick_params(width=2)
    ax.yaxis.set_tick_params(width=2)
    plt.text(0.7, 0.1,lab,
     horizontalalignment='center',
     verticalalignment='center',
             transform = ax.transAxes,fontsize=24)
    name = out+".png"
    fig.savefig(name,bbox_inches='tight')
def main():
    inzc = "16730_N205-4163ne-2497_gst.zc"
    out = 'unweighted'
    lab = 'NHALO1_UVIS'
    plot_cum_sfh(inzc,out,lab)
main()
