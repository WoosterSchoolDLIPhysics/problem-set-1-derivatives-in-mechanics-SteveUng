# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 13:49:24 2017

@author: Steven
"""

from pylab import *

#allocate an array, t, for time. It runs from t=0 to t=4 seconds in steps of .01 seconds
t = arange(0,4,.01)

x= t**4 - 4*t**3 + 3*t - 6
v= 4*t**3 - 12*t**2 + 4*t +3
a= 12*t**2 - 24*t + 4
j=  24*t - 24


figure(1)
subplot(411)
plot(t,x)
subplot(412)
plot(t,v)
subplot(413)
plot(t,a)
subplot(414)
plot(t,j)
