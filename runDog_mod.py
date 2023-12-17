#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:48:51 2023

@author: williamzheng
"""

from dog_mod import Dog
import matplotlib.pyplot as plt

dog1 = Dog("acdc")

dog1.name = "shadow"
dog1.age = 7
dog1.sit()
dog1.bark()

'''
    dog2 = Dog()
    dog2.name = "Lassie"
    dog2.bark()


'''
fig = plt.figure()
ax = fig.add_axes([.1,.2,.8,.9])

import numpy as np
x = np.linspace(0, 10, 20) # Generates 20 data points between 0 and 10 in array x
y = x**2 # Generates array y from square of array x values
ax.plot(x, y, 'purple') # Adds data series to plot

dog2 = Dog("apc")
#Set the dog’s name to
#Scooby and age 8
#Have Scooby sit.
dog2.name = "Scooby"
dog2.age = 8
dog2.sit()


dog3 = Dog("lps")
print(dog3.name)

