# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:30:02 2019

@author: LordOf20th
"""
import numpy as np
import random
import tkinter as tk

def genForet(n,p=0.25):
    foret=np.full(shape=(n,n), fill_value=0)
    for i in range(0,foret.shape[0]):
        for j in range(0,foret.shape[1]):
            if random.random() <= p:
                foret[i,j]=1 
    return foret

def affichage(foret):
    
    fenetre = tk.Tk() #Crée la fenêtre que l'on va modifier
    
    label = tk.Label(fenetre, text="Wildfire") #Met en place le titre
    label.pack()

    canvas = tk.Canvas(fenetre, width=foret.shape[0]*10, height=foret.shape[1]*10,background='#c68c53') #On définit le canevas qui affiche notre forêt
    for i in range(0,foret.shape[0]):
        for j in range(0,foret.shape[1]):
            if foret[i,j]== 1:
                canvas.create_rectangle(i*10,j*10,(i+1)*10,(j+1)*10,fill='green',width=0)
    canvas.pack()
    
    fenetre.mainloop() #affiche la fenêtre