# -*- coding: utf-8 -*-
"""
Created on Sun May 24 01:30:24 2020

@author: Francois Gachelin
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation

#paramètres
a=10
d=100
X=10
lamb=5
#fin paramètres

s1x,s1y,s2x,s2y=0,a/2,0,-a/2
k=2*np.pi/lamb

f,g1=plt.subplots()
plt.subplots_adjust(bottom=0.2)#margin-bottom
g1.set_xlim(0,d)
g1.set_ylim(-50,50)
f.suptitle("Interférences de deux ondes synchrones")
s1,=g1.plot(0,s1y,"r+")
s2,=g1.plot(0,s2y,"b+")

x_data=np.linspace(0,1.2*d,500)
y_data=[np.sin(k*x)+s1y for x in x_data]
v_data=[np.sin(k*x)+s2y for x in x_data]

c1,=g1.plot(x_data,y_data,"r-")
c2,=g1.plot(x_data,v_data,"b-")

def rota(x,y,angle,decalage_vertical):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array(((c, -s), (s, c)))
    rx,ry=[],[]
    for i in range(len(x)):
        rx.append(c*x[i]-s*y[i])
        ry.append(s*x[i]+c*y[i]+decalage_vertical)
    return rx,ry
    
def frame(i):
    s1x,s1y,s2x,s2y=0,a/2,0,-a/2
    k=2*np.pi/lamb
    angle1,angle2=np.arctan((X-s1y)/d),np.arctan((X-s2y)/d)
    
    y_data=[np.sin(k*x-i) for x in x_data]
    rx,ry=rota(x_data,y_data,angle1,s1y)
    c1.set_data(rx,ry)
    
    v_data=[np.sin(k*x-i) for x in x_data]
    ru,rv=rota(x_data,v_data,angle2,s2y)
    c2.set_data(ru,rv)
    
    s1.set_ydata(s1y)
    s2.set_ydata(s2y)
    
    return c1, c2

animation=FuncAnimation(f,frame,frames=np.linspace(0,2*np.pi,20),interval=100)

axX=plt.axes([0.2,0.01,0.6,0.02])
sX=Slider(axX,"$X$",-50,50)
axlamb=plt.axes([0.2,0.04,0.6,0.02])
slamb=Slider(axlamb,r"$\lambda$",2,10)
axa=plt.axes([0.2,0.07,0.6,0.02])
sa=Slider(axa,r"$a$",0,30)

def maj(_):
    global X
    global lamb
    global a
    X,lamb,a=sX.val,slamb.val,sa.val

sX.on_changed(maj)
slamb.on_changed(maj)
sa.on_changed(maj)

plt.legend()
plt.show()