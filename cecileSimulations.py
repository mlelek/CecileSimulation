# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

indent = 100
filamentNum = 30
nbreProtLabeled = 100
locError = 0.000000000015
AbLenMax = 0.0000001
proteinDist = 0.050

xx = np.array([])
yy = np.array([])

#lengthOfFilament = .6+1*np.random.rand(1,1)
lengthOfFilament = 1
Fil_init = np.linspace(1,1+lengthOfFilament,np.int(lengthOfFilament/proteinDist)+1)

filament = np.zeros([np.size(Fil_init,0)])
for k in range(0, np.size(filament)):
    ktmp = Fil_init[k]+0.015*np.random.randn(1,1)
    filament[k] = ktmp

idx = np.random.permutation(np.size(filament))
filament = filament[idx]
nbis = (nbreProtLabeled/100)*np.size(filament)
filament_x = filament[0:np.int(nbis)]
filament_y = np.ones(np.size(filament_x))

for k in range(0,np.int(nbis)):
    nbreLoc = np.int(100*np.random.rand(1))
    AbLength = (AbLenMax-0)*np.random.rand(1)
    xtemp = (filament_x[k]+np.sqrt(2)*AbLength)+locError*np.random.randn(nbreLoc)
    ytemp = (filament_y[k]+np.sqrt(2)*AbLength)+locError*np.random.randn(nbreLoc)
    xx = np.append(xx,xtemp)
    yy = np.append(yy,ytemp)
    
plt.figure()
plt.plot(xx,yy,'k+')
plt.ylim([1-.2,1+.2])    


    

    
    
