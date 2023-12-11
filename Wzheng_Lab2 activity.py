#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 14:43:22 2023

@author: williamzheng
"""

def main():
    file = open("July23_Flight_Delays.csv")
    airlines, delays, airports = build_dicts(file)
    apt1 = input("Name the first airport: ")
    apt2 = input("Name the second airportL: ")
    stats(airlines, delays, airports, apt1, apt2)
    file.close()
    
def build_dicts(file_1):
    airlines_dict, delays_dict, airports_dict = {},{},{}
    
    for line in file_1:
        data = line.split(",")
        #airline
        temp_airline = data[0]
        #origin
        temp_org = data[1]
        #destination
        temp_dst = data[2]
        #delay 
        temp_delay = data[3]
        
        if line.startswith("Airline"):
            #skips the header
            continue
        if temp_dst not in airlines_dict: # if the dst is not included in the diction,
            airlines_dict[temp_dst] = [temp_airline]
            delays_dict[temp_dst] = [int(temp_delay.strip())]
            airports_dict[temp_dst] = [temp_org]
        
        else: #if the destination is already included in the dictionary,
        #for airline
            if temp_airline not in airlines_dict[temp_dst]:
                airlines_dict[temp_dst].append(temp_airline)
        #airport 
            if temp_org not in airports_dict[temp_dst]:
                airports_dict[temp_dst].append(temp_org)
            #for delaytime 
            delays_dict[temp_dst].append(int(temp_delay.strip()))
                

    return airlines_dict, delays_dict, airports_dict

##############
###function###
##############
def stats(airlines_dict, delays_dict, airports_dict, airport_1, airport_2):
    file_name = airport_1 + "vs" + airport_2 + ".txt"
    file_2 = open(file_name, "w")
    #airlines
    file_2.write("These AIRLINES fly into %s: %s" % (airport_1, str(airlines_dict[airport_1])))
    file_2.write("\n")
    file_2.write("These AIRLINES fly into %s: %s" % (airport_2, str(airlines_dict[airport_2])))
    file_2.write("\n")
    
    #airports
    file_2.write("These AIRPORTS have direct flights into %s: %s" % (airport_1, str(airports_dict[airport_1])))
    file_2.write("\n")
    file_2.write("These AIRPORTS have direct flights into %s: %s" % (airport_2, str(airports_dict[airport_2])))
    file_2.write("\n")
    
    #some stats
    num_airlines_1 = len(airlines_dict[airport_1])
    num_airlines_2 = len(airlines_dict[airport_2])
    
    num_airports_1 = len(airports_dict[airport_1])
    num_airports_2 = len(airports_dict[airport_2])
    
    # stats comparison
    if num_airlines_1 > num_airlines_2:
        file_2.write("\n %s has %d more inbound airlines than %s. %d vs %d" % (airport_1, num_airlines_1 - num_airlines_2, airport_2, num_airlines_1, num_airlines_2))
    
    else:
        file_2.write("\n %s has %d more inbound airlines than %s. %d vs %d" % (airport_2, num_airlines_2 - num_airlines_1, airport_1, num_airlines_2, num_airlines_2))
        
    #stats comparison 2 
    if num_airports_1 > num_airports_2:
        file_2.write("\n %s has %d more airports that connects than %s. %d vs %d" % (airport_1, num_airports_1 - num_airports_2, airport_2, num_airports_1, num_airports_2))
    
    else:
        file_2.write("\n %s has %d more airports that connects than %s. %d vs %d" % (airport_2, num_airports_2 - num_airports_1, airport_1, num_airports_2, num_airports_1))
        
    
    #stats comparison -delay time
    avg_delay_1 = sum(delays_dict[airport_1])/ len(delays_dict[airport_1])
    avg_delay_2 = sum(delays_dict[airport_2]) /len(delays_dict[airport_2])
    
    file_2.write("\nAverage delay for %s: %.0f minutes" % (airport_1,avg_delay_1))
    file_2.write("\nAverage delay for %s: %.0f minutes" % (airport_2,avg_delay_2))
    lateflight_1 = sum( 1 for delay in delays_dict[airport_1] if delay > 14 ) /len(delays_dict[airport_1]) * 100
    lateflight_2 = sum( 1 for delay in delays_dict[airport_2] if delay > 14 ) /len(delays_dict[airport_2]) * 100
    file_2.write("\nFor %s in July, %d.1%% of flights were late" % (airport_1, lateflight_1))
    file_2.write("\nFor %s in July, %d.1%% of flights were late" % (airport_2, lateflight_2))
    #######
    #something for 14 min cut off time###
    #######
    ##incorporate function 2 and 3 in domain 1 

if __name__ == "__main__":
    main()


    
    
    
    
    
    
    
    
    
    
    
    
    
    