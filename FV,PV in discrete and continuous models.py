# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:54:07 2022

@author: Giri
"""
## PV AND FV IN DISCRETE AND CONTINUOUS MODEL
from math import exp as e

def future_discret_value(x,r,t):
    return x*(1+r)**t
def Present_discret_value(x,r,t):
    return x*(1+r)**-t

def future_continuos_value(x,r,t):
    return x*e(r*t)
def Present_continuous_value(x,r,t):
    return x*e(-r*t)

if __name__ =='__main__':
    
    x=100
    r=0.05
    t=5
    
    print("future value (discrete model) of x:%s" %future_discret_value(x, r, t))
    print("present value (discrete model) of x:%s" %Present_discret_value(x, r, t))
    
    print("future value (continuous model) of x:%s" %future_continuos_value(x, r, t))
    print("present value (continuos model) of x:%s" %Present_continuous_value(x, r, t))