# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:25:31 2020

@author: François Gachelin
"""


import matplotlib.pyplot as plt
import numpy as np


#etoile de masse me et planete de masse mp d'abscisse d, centre de masse en O

me=1
mp=0.1

#abscisses des astres
xe=-mp/(me+mp)
xp=me/(me+mp)

#champ ressenti
def g(x,y):
    return -(mp/((x-xp)**2+y**2)**0.5)-(me/((x-xe)**2+y**2)**0.5)-0.5*(x**2+y**2)

X = np.arange(-2,2, 0.01)
Y = np.arange(-2,2, 0.01)
X, Y = np.meshgrid(X, Y)
Z = g(X, Y)
g=plt.contour(X, Y, Z,np.linspace(-2,-1,50))
plt.scatter([xp,xe],[0,0])
g.changed()
plt.show()


    
