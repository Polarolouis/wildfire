# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:30:02 2019

@author: LordOf20th
"""
import numpy as np
import random
import matplotlib.pyplot as plt

def genForet(n):
    foret=np.full(shape=(n,n), fill_value=0)
    for i in range(0,foret.shape[0]):
        for j in range(0,foret.shape[1]):
            if random.random() < 0.12:
                foret[i,j]=1 
    return foret