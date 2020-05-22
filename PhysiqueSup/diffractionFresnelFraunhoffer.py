# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:59:38 2020

@author: François Gachelin

Attention: diffraction à n ondes et donc plusieurs pics latéraux à cause du pas d'intégration.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

points_source=401
points_ecran=2001

#paramètres
D=0.5
a=1e-3
largeur_écran=20*a*D
lamb=633e-9

list_x=np.linspace(-a/2,a/2,points_source)
list_X=np.linspace(-largeur_écran/2,largeur_écran/2,points_ecran)

def intensité(X,source,D):
    amplitude=0
    for x in source:
        distance=(D**2+(x-X)**2)**0.5
        amplitude=amplitude+np.exp(1j*2*np.pi*distance/lamb)/distance
    return (np.absolute(amplitude))**2

m=max(intensité(list_X,list_x,D))
g1=plt.subplot(111)
g1.plot(list_X,intensité(list_X,list_x,D)/m)
    
'''
for D in [0.05,0.1,0.15]:
    m=max(intensité(list_X,list_x,D))
    plt.plot(list_X,intensité(list_X,list_x,D)/m,label=D)
'''
    
axD=plt.axes([0.2,0.01,0.6,0.02])
cD=Slider(axD,"$D$",-3,1)
def maj(_):
    D=5*10**cD.val
    largeur_écran=100*a*D
    list_X=np.linspace(-largeur_écran/2,largeur_écran/2,points_ecran)
    m=max(intensité(list_X,list_x,D))
    g1.clear()
    F=(str(a*a/(4*D*lamb)))[0:4]
    affichage=r"$F=\frac{a^2}{\lambda D}=$"+F+"\nD="+(str(D))[0:4]+"m\na=1,00mm"
    g1.text(-largeur_écran/2,0.8,affichage)
    g1.plot(list_X,intensité(list_X,list_x,D)/m)  
    g1.set_xlabel(r"$d(m)$",fontsize=20, labelpad=0)
    g1.set_ylabel(r"$\frac{I}{I_{max}}$",rotation=0,fontsize=20, labelpad=20)
    plt.show()
cD.on_changed(maj)

plt.show()
        