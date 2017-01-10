#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 20:04:31 2017

@author: christophergreen
Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 
    197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
 73, 79, and 97.
How many circular primes are there below one million?
"""

import math;

def is_prime(x):
    for i in range(2,math.floor(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True
   
def is_circular(x): #pass it a string!
    rotes=[x];
    i=1;
    while i<len(x):
        rotes.append(x[i:]+x[:i]);
        i+=1;
    #print("the rotations of",x,"are:",rotes);   
    for r in rotes:
        if is_prime(int(r))!=True:
            #print("False");
            return False
    #print("all rotations of",x,"are prime, so True");
    return True
    
def find_circulars(maximum):
    circs=[];
    counter=13; #to account for the cicular primes below 100
    j=101
    while j<=maximum:
        if is_prime(j):
            if is_circular(str(j)):
                circs.append(j);
                counter+=1;
        j+=2 #can skip the evens becasue they won't be prime
    print("from zero through",maximum,"we have found",counter,"circulars:",circs);
    return counter;
    
find_circulars(1000000); #--> from zero through 1000000 we have found 55:
#[113, 131, 197, 199, 311, 337, 373, 719, 733, 919, 971, 991, 1193, 1931, 
#3119, 3779, 7793, 7937, 9311, 9377, 11939, 19391, 19937, 37199, 39119, 
#71993, 91193, 93719, 93911, 99371, 193939, 199933, 319993, 331999, 391939, 
#393919, 919393, 933199, 939193, 939391, 993319, 999331] CORRECT

