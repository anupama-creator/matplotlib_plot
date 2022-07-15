import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = plt.axes(projection='3d')
#x = [350, 300]
#plt.xlim((0,6))
path = '/home/anu/Desktop/anupama/work/write_up/supercooled_liq/tex/images/rdf/rdf_cntscw/'
X1,Y1,Z1 = np.loadtxt( path + 'rdf_350K.dat',unpack=True, usecols=[0,1,2])
ax.plot(X1,Y1,Z1)#color='r', label='350K')
ax.fill_between(X1,Y1,Z1, color='red')
X1 [X1<0] = np.nan
X1 [X1>6] = np.nan
X2,Y2,Z2 = np.loadtxt( path + 'rdf_300K.dat',unpack=True, usecols=[0,1,2])
ax.plot(X2,Y2,Z2, color='m', label='300K')
X2 [X2<0] = np.nan
X2 [X2>6] = np.nan
X3,Y3,Z3 = np.loadtxt( path + 'rdf_273K.dat',unpack=True, usecols=[0,1,2])
ax.plot(X3,Y3,Z3, color='y', label='273K')
X3 [X3<0] = np.nan
X3 [X3>6] = np.nan
X4,Y4,Z4 = np.loadtxt( path + 'rdf_250K.dat',unpack=True, usecols=[0,1,2])
ax.plot(X4,Y4,Z4, color='g', label='250K',alpha=0.4)
X4 [X4<0] = np.nan
X4 [X4>6] = np.nan
X5,Y5,Z5 = np.loadtxt( path + 'rdf_230K.dat',unpack=True, usecols=[0,1,2])
ax.plot(X5,Y5,Z5, color='c', label='230K',alpha=0.8)
X5 [X5<0] = np.nan
X5 [X5>6] = np.nan
X6,Y6,Z6 = np.loadtxt( path + 'rdf_210K.dat',unpack=True, usecols=[0,1,2])
ax.plot(X6,Y6,Z6, color='b', label='210K',alpha=0.8)
X6 [X6<0] = np.nan
X6 [X6>6] = np.nan
X7,Y7,Z7 = np.loadtxt( path + 'rdf_160K.dat',unpack=True, usecols=[0,1,2])
ax.plot(X7,Y7,Z7, color='b', label='160K',alpha=0.5)
X7 [X7<0] = np.nan
X7 [X7>6] = np.nan
X8,Y8,Z8 = np.loadtxt( path + 'rdf_100K.dat',unpack=True, usecols=[0,1,2])
ax.plot(X8,Y8,Z8, color='indigo', label='100K',alpha=0.5)
X8 [X8<0] = np.nan
X8 [X8>6] = np.nan
ax.set_xlim3d(0, 6)
plt.show() 
