# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:49:32 2020

@author: osjac
"""


from numpy import random, arccos, pi, sin, cos, linspace,fabs
import neutrons #import given functions

L = 0.1 #Define side length of cube
Cube = [0.1,0.1,0.1] #difine cube
a = 0.017 #mean free path between the neutron hitting another nucleus and bouncing off
b = 0.21 #mean free path between the neutron hitting a nucleus and causing fission
R = (2*a*b)**0.5 #distance that a neutron diffuses away from its starting point before causing a fission 

def fiss():#function for fisson
    FP = [L*random.random(),L*random.random(),L*random.random()] #generate random 3d location in cube 
    SP = [0,0,0] #reset secound point
    nN = neutrons.neutrons() #number of secondary neutrons using the given function
    count = 0 #count to hold number of secondary fissions

    for i in range(0,nN): #loop for each secondary neutron
        phi = 2.0* pi * random.random() #generate random phi value
        theta = arccos(2.0* random.random() -1.0) #generate random theta value
        s = neutrons.diffusion()*R #the result from diffusion() must be scaled with R 
        
        #find new x y and z location of secondary neutron
        SP[0] = FP[0] + s*sin(theta)*cos(phi) 
        SP[1] = FP[1] + s*sin(theta)*sin(phi)
        SP[2] = FP[2] + s*cos(theta)
        
        #logic to check if location of secondary neutron is within the cube
        if ((SP[0] >= 0) and (SP[0] <= L)) and ((SP[1] >= 0) and (SP[1] <= L)) and ((SP[2] >= 0) and (SP[2] <= L)):
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
    
print("=========================================================================================================")#spacer    
print("Critical length:",CM) #print final Critical length
print("Critical Mass:",(CM**3)*18.7*(10**6)*(10**-3)) #calculate then print final Critical mas     

  
     
  