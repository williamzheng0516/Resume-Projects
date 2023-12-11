#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 12:16:47 2023

@author: williamzheng
"""

from images import Image 


def main():
    image = Image("smokey.gif")
    blackandWhite(image)
    image.draw()

def blackandWhite(image):
    blackPixel = (0,0,0)
    whitePixel = (255,255,255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            r, g, b, = image.getPixel(x,y)
            average = (r+g+b)//3 
            if average < 128:
                image.setPixel(x,y,blackPixel)
            else:
                image.setPixel(x, y, whitePixel)
        
main()  


