# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:13:17 2022

@author: admin
"""


# Gerekli Modülleri ekliyoruz.

from numpy import arange
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
from numpy import meshgrid
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
 

# Test Fonksiyonumuzu Tanımlıyoruz.

def objective(x, y):
	return 100*(y - x**2)**2 + (1 - x)**2

 
# Değer Aralıklarını Tanımlıyoruz.
r_min, r_max = -2.048, 2.048


# Aralık Değerinin Ölçütü
xaxis = arange(r_min, r_max, 0.1)
yaxis = arange(r_min, r_max, 0.1)
x, y = meshgrid(xaxis, yaxis)
results = objective(x, y)
figure = pyplot.figure()
axis = figure.gca(projection='3d')
axis.plot_surface(x, y, results, cmap='jet')
pyplot.show()