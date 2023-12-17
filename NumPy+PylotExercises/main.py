#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:28:30 2023

@author: williamzheng
"""

import labactivity3 as ut

def main():
     
    # Display app header informative information
    print("\nHeart Attack Analysis")
    print("\nThese are the factors related to heart attacks that are considered in this data:")
    print("\t1. Heart Attack Percentage is calculated based on all data to see if the data is skewed.")
    print("\t2. Gender Percent is used to distinguish between the heart attack rates in men and women.")
    print("\t3. Four types of Chest Pain are considered, along with the associated heart attack percentages.")
    print("\t4. Fasting Blood Sugar levels are considered to determine possible coronary heart disease.")
    print("\t5. EKG is considered, as it detects heart problems that can forecast chance of future heart attacks.")
    print("\t6. Exercise is considered to see if likelihood of heart attack increases when physically active.")  
    
    # Perform Heart Attack Percents
    ut.getHeartAttack()
  
    # Perform Gender Percents
    ut.getGender()
    
    
    # Perform EKG Analysis
    ut.getEKG()
    

    # Perform Exercise Analysis
    ut.getExercise()
  
#---------------------------Code Entry Point---------------------------#
if __name__ == "__main__":
    main()