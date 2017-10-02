# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 10:55:18 2017

@author: brian
"""

from pylab import *

t = linspace(0,1,100)

x = 3*sin(2*pi*t)
y = 2*cos(2*pi*t)

vx = 6*pi*cos(2*pi*t)
vy = 4*pi*-sin(2*pi*t)

ax = 12*pi**2*-sin(2*pi*t)
ay = 8*pi**2*-cos(2*pi*t)

figure(1)

for it in arange(len(t)):
    clf()
    #subplot(131)
    plot(x,y)
    plot([0,x[it]],[0,y[it]],'b-o')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*x[it],1.2*y[it],r'$\vec{x}$',color='blue',size=15)

    text(1.1*ax[it]/10,1.1*ay[it]/10,r'$\vec{a}$',color='green',size=15)
    grid()
    

    plot(vx,vy)
    plot([0,vx[it]],[0,vy[it]],'b-o')
    #axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    #text(1.2*x[it],1.2*y[it],r'$\vec{x}$',color='blue',size=15)

    text(1.1*vx[it]/10,1.1*vy[it]/10,r'$\vec{a}$',color='blue',size=15)
    grid()


    plot(ax,ay)
    plot([0,ax[it]],[0,ay[it]],'b-o')
    #axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    #text(1.2*x[it],1.2*y[it],r'$\vec{x}$',color='blue',size=15)

    text(1.1*ax[it]/10,1.1*ay[it]/10,r'$\vec{a}$',color='red',size=15)
    grid()
    savefig('frame_%03d.png' % it)


    pause(.001)
    
   