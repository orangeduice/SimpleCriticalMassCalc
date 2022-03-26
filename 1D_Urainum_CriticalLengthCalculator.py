# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:22:08 2020

@author: osjac
"""

from numpy import random, fabs, linspace
import neutrons #import given functions

#define variables
L = 0.1 #length of fuel rod
a = 0.017 #mean free path between the neutron hitting another nucleus and bouncing off
b = 0.21 #mean free path between the neutron hitting a nucleus and causing fission
R = (2*a*b)**0.5 #distance that a neutron diffuses away from its starting point before causing a fission 

def fiss():#function for fisson
    FP = L*random.random() #find a random point on the rod
    
    nN = neutrons.neutrons() #number of secondary neutrons using the given function
    count = 0 #count to hold number of secondary fissions
    
    for i in range(0,nN): #loop for each secondary neutron
        if (random.random() > 0.5): #50% chance for secondary neutron go left or right
            SP = FP + R #if right add the diffuse distance
        else:
            SP = FP - R #if left minus the diffuse distance 
        if ((SP >= 0) and (SP <= L)): #check if the secondary neutron is within rod
            count = count + 1 #if it is there is a secondary fission, add one to the count
    return count #return the number of secondary fissions
    
pCM = 0 #pervious critical mass (set to 0 so that the code runs the first time)
CM = 1 #set critical mass to 1 so the code runs the first time

LB = 0.01 #set upper bound of vaules to be tested for critical mass
UB = 0.5  #set lower bound of vaules to be tested for critical mass

intervalN = 100 #set number of vaules tested in the range
calN = 10000 #number of inital fissions (the higher the better, but not too high)

#While loop that stops when the diffence
# in the calculated critical sizes is very small.
while ( fabs (CM - pCM ) >1.0e-4* fabs ( CM )): 
    interval = linspace(LB,UB,intervalN) #create the testing interval
    for o in interval: #loop through testing vaules in the interval
        L = o #set L to the current test vaule
        a = 0 #set the total secondary fission count to 0 to avoid errors
        
        for i in range(0,calN): #loop for set number of inital fissions
            a = a + fiss() #add to total number of secondary fissions 

        #if the total number of secondary fissions is larger than the number of inital fissions
        #this value is the critical (but a more accurate value can be found)
        if a > calN: 
            pCM = CM #set previous value as old critical vlaue
            CM = o #set new critical value
            LB = CM - (UB-LB)/4 #set new lower bound
            UB = CM + (UB-LB)/4 #set new upper bound
            #calN = calN*5 #old method to increse number of inital fissions for better accuracy
            break 
        
    print("Current Critical length:",CM," | ","Testing range:",LB,"to",UB)#print working values 
    
print("Critical length:",CM) #print final Critical length

