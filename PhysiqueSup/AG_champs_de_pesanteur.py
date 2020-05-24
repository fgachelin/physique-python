# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 01:12:01 2019

@author: click
"""

from math import *
import matplotlib.pyplot as p
from matplotlib.widgets import Slider
import numpy as np

w=2*pi/86400
r=6.37e6
g=9.81

def g_app(th):
    return (g**2+(r*w**2*np.sin(th)**2)**2-2*g*r*w**2*np.sin(th)**2)**0.5

def deviation(th):
    return np.degrees(r*w**2*np.sin(th)*np.cos(th)/g)


angles=np.linspace(0,pi,100)

p.subplot(211)
p.plot(angles,g_app(angles),label="g_apparent")
p.legend()

p.subplot(212)
p.plot(angles,deviation(angles),label="déviation")

p.legend()
p.show()

