#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:53:49 2019

@author: jhongesell
"""

import numpy as np

def funcion(x):
    return np.sqrt(x +2) # ( x + 2 ) ** 0.5
x = np.array([-1 , 0, 3, 5, 10, 15])
y = funcion(x)
print(y)

import pandas as pd

tabla = pd.DataFrame( list(zip(x, y)), columns=['x', 'f(X)'])
print(tabla)

#%matplotlib inline

#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


def move_spines():
    """Esta funcion divide pone al eje y en el valor 0
    de x para dividir claramente los valores positivos
    y negativos"""
    fix, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")
        
    for spine in ["right", "top"]:
        ax.spines[spine].set_color("none")
    
    return ax

x = np.linspace(-2, 6, num=30)

ax = move_spines()
ax.grid()
ax.plot(x, funcion(x))
plt.title(r"Grafico de $f(x)=\sqrt{x +2}$")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()