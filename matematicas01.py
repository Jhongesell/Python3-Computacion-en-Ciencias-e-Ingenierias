#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:53:49 2019

@author: jhongesell
"""

# FUNCIONES

import numpy as np

def funcion(x):
    return np.sqrt((x**2) + (6*x) +5) # ( x + 2 ) ** 0.5
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

x = np.linspace(-2, 10, num=15)

ax = move_spines()
ax.grid()
ax.plot(x, funcion(x))
plt.title(r"Grafico de $f(x)=\sqrt{(x**2) + (6*x) +5}$")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()

# LIMITES

def f(x):
    return x**2 -x + 2
x = np.array([1, 1.5, 1.9, 1.95, 1.99, 2.001, 2.04, 2.005, 2.2, 2.5, 3])
y=f(x)
tabla = pd.DataFrame(list(zip(x,y)), columns=['X', 'f(x)'])
print(tabla)

x = np.linspace(-2, 4, num=30)
ax = move_spines()
ax.grid()
ax.plot(x, f(x))
ax.scatter(2, 4, label="limite cuando x tiende a 2", color='r')
plt.legend()
plt.title(r"Grafico de $f(x)=x^2 - x + 2$")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()
