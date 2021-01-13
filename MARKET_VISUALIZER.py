# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:36:56 2020

@author: alexx
"""

import numpy as np
import random as rm 

import time, threading

#starile posibile in piata forex
states = ["consolidation", "uptrend", "downtrend"]
#definim variabile cu numele starilor pentru a evita typos 
#evitam accesarea vectorului de fiecare data 
consolidation = "consolidation"
uptrend = "uptrend"
downtrend = "downtrend"
#numele tranzitiilor si secventele in care pot aparea 
tName = [["CC", "CD", "CU"], ["DC", "DD", "DU"], ["UC", "UD", "UU"]]
#matricea de tranzitii 
tMatrix = [
    [0.344006453704011,0.5266567943788216,0.12933675191716737],
    [0.12933675191716737,0.344006453704011,0.5266567943788216],
    [0.344006453704011, 0.5266567943788216, 0.12933675191716737]
    ]

consolidation = "consolidation"
uptrend = "uptrend"
downtrend = "downtrend"

def verifyTMatrix():
    if(sum(tMatrix[0]) + sum(tMatrix[1]) + sum(tMatrix[2])) != 3:
        print ("Transition Matrix not does not have correct data as an input!")
        return 0
    else:
        print ("Transition Matrix has a corect data input format")
        return 1
    
def forecast_State(timeframe, curr_state):
    print("The current state of the system is: " + curr_state)
    state_list = [curr_state]
    ti = 0
    probability = 1
    
    while ti != timeframe:
        if curr_state == "consolidation":
            change_state = np.random.choice(tName[0], replace = True, p = tMatrix[0])
            #change hard cooded tName state
            if change_state == "CC":
                probability = probability * tMatrix[0][0]
                state_list.append(curr_state)
                pass
            elif change_state == "CD":
                probability = probability * tMatrix[0][1]
                curr_state = "downtrend"
                state_list.append(curr_state)
                pass
            elif change_state == "CU":
                probability = probability * tMatrix[0][2]
                curr_state = "uptrend"
                state_list.append(curr_state)
        elif curr_state == "downtrend":
            change_state = np.random.choice(tName[1], replace = True, p = tMatrix[1])
            if change_state == "DC":
                probability = probability * tMatrix[1][0]
                curr_state = "consolidation"
                state_list.append(curr_state)
                pass
            elif change_state == "DD":
                probability = probability * tMatrix[1][1]
                curr_state = "downtrend"
                state_list.append(curr_state)
                pass
            elif change_state == "DU":
                probability = probability * tMatrix[1][2]
                curr_state = "uptrend"
                state_list.append(curr_state)
        elif curr_state == "uptrend":
            chenge_state = np.random.choice(tName[2], replace = True, p = tMatrix[2])
            if change_state == "UC":
                probability = probability *  tMatrix[2][0]
                curr_state = "consolidation"
                state_list.append(curr_state)
                pass
            elif change_state == "UD":
                probability = probability * tMatrix[2][1]
                curr_state = "downtrend"
                state_list.append(curr_state)
                pass
            elif change_state == "UU":
                probability = probability * tMatrix[2][2]
                curr_state = "uptrend"
                state_list.append(curr_state)
        ti += 1
        
    print("Possible states: " + str(state_list))
    print("End state after "+ str(timeframe) + " days: " + curr_state)
    print("Probability of the possible sequence of states: " + str(probability))
    
    return state_list 

#calculeaza probabilitatea pentru fiecare ending state
#pentru un numar de "tries" ori 
def runTestEndingState(tries, start_state):
    trial_list = []
    
    p_consolidation = 0
    p_uptrend = 0
    p_downtrend = 0
    
    curr_final_state = []
    
    for it in range(1, tries):
        trial_list.append(forecast_State(2, start_state))
        print(forecast_State(2, start_state))
        

    
    for itp in trial_list:
        curr_final_state = itp.pop()
        if curr_final_state == consolidation:
            p_consolidation += 1
        elif curr_final_state == uptrend:
            p_uptrend += 1
        elif curr_final_state == downtrend:
            p_downtrend += 1 
            
            
    perc_consolidation = p_consolidation/tries * 100
    perc_uptrend = p_uptrend/tries * 100 
    perc_downtrend = p_downtrend/tries * 100 
    print("The probability of the following states to appear as an end state is: ")
    print("Consolidation: " + str(perc_consolidation) + "%")
    print("Uptrend: " + str(perc_uptrend) +  "%")
    print("Downtrend: " + str(perc_downtrend) + "%")
                
    
    
def main():
    
    print("The state of the tMatrix is the following: ")
    verifyTMatrix()
    
    start_state = consolidation
    forecast_State(4, start_state)
    tries = 1000
    
    print("When starting from the " + start_state + " state is: ")
    runTestEndingState(tries, start_state)
    
    
if __name__ == "__main__":
    main()