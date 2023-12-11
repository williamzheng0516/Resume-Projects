#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 11:49:28 2023

@author: williamzheng
"""

class Dog:
    name =""
    age = 1
    state =""
    
    def __init__(self,name):
        self.name = name
        print("Object constructed!")
    
    def walk(self):
        self.state = "walking"
        
    def sit(self):
        self.state = 'sitting'
    def bark(self):
        print(self.name, "is barking!")
        
        # Destructor
    def __del__(self):
        print("Object destructed!")
        

import mymodule as mm
print(mm.root(4,2))
print(mm.constants)