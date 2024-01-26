#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:48:07 2023

@author: williamzheng
"""

import pandas as pd
import matplotlib.pyplot as plt
#import the input dataframe
df = pd.read_csv("heart.csv")

#get gender * pie chase

def getGender():
    # male
    df_m = df.loc[(df.sex == 0) & (df.attack ==1)]
    m_heart_attacks = len(df_m)
    
    # female
    df_f = df.loc[(df.sex == 1) & (df.attack ==1)]
    f_heart_attacks = len(df_f)
    #total number of heart attacks 
    t_heart_attacks = m_heart_attacks + f_heart_attacks
    
    
    #texxt output for male
    male_percentage_notation = "{:,.2f}%".format(m_heart_attacks/t_heart_attacks*100)
    print("\nMale heart attacks:  " + male_percentage_notation)
    
    
    #text output for female 
    female_percentage_notation = "{:,.2f}%".format(f_heart_attacks/t_heart_attacks*100)
    print("\nFemale heart attacks:  " + female_percentage_notation)
    
    #piechart
    
    labels = 'Male', "Female"
    sizes = [m_heart_attacks, f_heart_attacks]
    
    #initiating a pie chart
    fig1, ax1 = plt.subplots()
    
    #drawing a pie chart
    ax1.pie(sizes, labels = labels, autopct = "%1.2f%%", startangle = 90)
    
    #equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    
    #set title
    ax1.set_title("Heart Attack Ratio between Male & Female")
    
    #Draw
    #fig1 = plt.gcf()
    plt.show()
    fig1.savefig('Gender.png')


def getExercise():
    
    # "exng" = exercise history
    exang_val_counts = df.groupby("exng")["attack"].value_counts()
    
    #exang_value_counts[1][1] - the number of heart attack patients who do exercise regularly i.e., Positive
    
    #exang_value_counts[1]01] - the number of heart attack patients who do NOT exercise regularly i.e., negative
    
    
    #portion of positive
    exang_heart_attack = (exang_val_counts[1][1]/(exang_val_counts[1][1]+exang_val_counts[1][0]))
    
    #portion of negative
    
    no_exang_heart_attack = (exang_val_counts[0][1]/(exang_val_counts[0][1]+exang_val_counts[0][0]))
    
    #text to output for postiive exercise
    percent_notation = "{:,.2f}%".format(exang_heart_attack*100)
    print("\nPercent who exercised and had heart attacks:  " + percent_notation)
    
    
    #text to output for negative 
    percent_notation = "{:,.2f}%".format(no_exang_heart_attack*100)
    print("\nPercent with no exercise and had heart attacks:  " + percent_notation)
    
    
    
    #create bar chart of heart attack percents by exercise
    data = {"yes":exang_heart_attack*100, "no":no_exang_heart_attack*100}
    
    #graph inputs
    courses = list(data.keys()) #Yes or not
    values = list(data.values()) #exang_heart_attack or no_exang_heart_attack
    
    
    #initiating plot
    fig1 = plt.figure(figsize = (10,5))
    plt.bar(courses, values ,color = 'purple', width = 0.7)
    plt.xlabel("Exercise")
    plt.ylabel("Percent Heartattack")
    plt.title("percent heart attack if exercising")
    #fig1 = plt.gcf()
    #draw
    plt.show()
    fig1.savefig("exercise.png")
    #plt.clf()












def getHeartAttack():
    """ Finds percent of patients with heart attack history.
    
    """
    val_counts = df["attack"].value_counts()
    no_heart_attack = (val_counts[0] / df.shape[0])
    heart_attack = (val_counts[1] / df.shape[0])
    percent_notation = "{:,.2f}%".format(no_heart_attack*100)
    print("\nThe percent of no heart attacks in the data: " + percent_notation)
    percent_notation = "{:,.2f}%".format(heart_attack*100)
    print("The percent of heart attacks in the data: " + percent_notation)
    
    
    
    # create pie chart
    labels = 'Heart Attack', 'No Heart Attack'
    sizes = [heart_attack, no_heart_attack]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.    
    ax1.set_title('Heart Attack Ratio in Data')
    #fig1 = plt.gcf()
    plt.show()
    fig1.savefig('HeartAttack.png')
    #plt.clf()




def getEKG():
    """ Looks at resting EKG.
    
    Finds percent of patients with heart attack in each EKG Type.
    """
    restecg_val_counts = df.groupby("restecg")["attack"].value_counts()
    e = []
    print("\nEKG type:\n\t0 - EKG was normal\n\t1 - EKG had an abnormality with ST-T Wave\n\t2 - EKG had an abnormality in the Left ventricular")
    for i in range(3):
        temp = (restecg_val_counts[i][1] / (restecg_val_counts[i][1]+restecg_val_counts[i][0]))
        e.append(temp*100)
        percent_notation = "{:,.2f}%".format(temp*100)
        print("Resting EKG Type %s" % (i) + " had this percent of heart attack: " + percent_notation)
        
    # create bar chart of pain types
    data = {'Normal':e[0], 'Abnormal ST-T Wave':e[1], 'Abnormal Left Ventricular':e[2]}
    courses = list(data.keys())
    values = list(data.values())   
    
    
    
    #initiating plot
    fig1 = plt.figure(figsize = (10,5))
    plt.bar(courses,values,color = 'red', width = 0.7)
    plt.xlabel("")
    plt.ylabel("Percent")
    plt.title("percent heart attack by resting EKG ")
    #fig1 = plt.gcf()
    #draw
    plt.show()
    fig1.savefig("EKG.png")
    #plt.clf()
    
    #####################
    ### add something ###	   
    #####################   



    
    
    
    
