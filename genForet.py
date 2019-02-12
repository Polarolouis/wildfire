# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:30:02 2019

@author: LordOf20th
"""
import numpy as np
import random
import tkinter as tk
"""
    Les états possibles de nos cases :
        - 0 : pas d'arbre
        - 1 : un arbre sain
        - -1 : un arbre en feu
        - -2 : un arbre mort
"""
#Fonctions agissant sur la matrice
def genForet(n,p):
    if n>=2:
        foret=np.full(shape=(n,n), fill_value=0)
        for i in range(0,foret.shape[0]):
            for j in range(0,foret.shape[1]):
                if random.random() <= p:
                    foret[i,j]=1 
        return foret
    else:
        raise ValueError("n doit prendre une valeur de 2 au moins")

def enflammer(foret,x,y): #Fonction mettant le feu aléatoirement à une case
    if x==-1:
        x=random.randint(0, foret.shape[0]-1)
    if y==-1:
        y=random.randint(0, foret.shape[1]-1)
    foretEnflammée = np.copy(foret)
    foretEnflammée[x,y]=-1
    return foretEnflammée

def propager(F,k,i,j):
    try:
        if F[k-1][i-1,j] == 1: #Si la case au dessus est un arbre
            F[k][i-1,j] = -1 #La case au dessus brûle
    except IndexError:
        pass
    try:
        if F[k-1][i+1,j] == 1: #Si la case au dessous est un arbre
            F[k][i+1,j] = -1 #La case en dessous brûle
    except IndexError:
         pass
    try:
        if F[k-1][i,j-1] == 1: #Si la case à gauche est un arbre
            F[k][i,j-1] = -1 #La case à gauche brûle
    except IndexError:
        pass
    try:
        if F[k-1][i,j+1] ==1: #Si la case à droite est un arbre
            F[k][i,j+1] = -1 #La case à droite brûle
    except IndexError:
        pass

def feuDeForet(n, tours, p=0.5, x=-1, y=-1):
    F=[genForet(n, p)]
    print(F[0], "Instant initial")
    F.append(enflammer(F[0],x,y)) #On stocke les deux premiers état de notre forêt
    print(F[1], "Rang : 1 (Départ de feu)")
    for k in range(2,tours): 
        F.append(np.copy(F[k-1])) #On copie la forêt du tour précédent
        for i in range(0,F[k].shape[0]):
            for j in range(0,F[k].shape[1]):
                
                if F[k][i,j]==-1:#Si la case est en feu au rang k
                    if F[k-1][i,j]==0: #Si cette case ne portait pas d'arbre au rang k-1 alors on propage le feu et la case s'éteint
                        propager(F,k,i,j)
                        F[k][i,j]=0
                    elif F[k-2][i,j]==-1: #Si la case était en feu au tour précédent : propage et mort de l'arbre
                        propager(F,k,i,j)
                        F[k][i,j]=-2
                    else: #La case a été mise en feu, elle propage le feu
                        propager(F,k,i,j)
        print(F[k], "Rang : {}".format(k))
    return F #Return temporaire
    
    
""" def affichage(foret):
    
    fenetre = tk.Tk() #Crée la fenêtre que l'on va modifier
    
    label = tk.Label(fenetre, text="Wildfire") #Met en place le titre
    label.pack()

    canvas = tk.Canvas(fenetre, width=(foret.shape[0]+2)*10, height=(foret.shape[1]+2)*10,background='red') #On définit le canevas qui affiche notre forêt
    canvas.create_rectangle(10,10,(foret.shape[0]+1)*10,(foret.shape[1]+1)*10,fill='#c68c53')
    for i in range(0,foret.shape[0]):
        for j in range(0,foret.shape[1]):
            if foret[i,j]== 1:
                canvas.create_rectangle((i+1)*10,(j+1)*10,(i+2)*10,(j+2)*10,fill='green',width=0)
            elif foret[i,j]==-1:
                canvas.create_rectangle((i+1)*10,(j+1)*10,(i+2)*10,(j+2)*10,fill='red',width=0)
    canvas.pack()
    bouton = tk.Button(fenetre, text="Quitter", command=fenetre.quit)
    bouton.pack()
    fenetre.mainloop() #affiche la fenêtre """ 
    
#Fonctions utiles à l'affichage 
def pause():
    input("Appuyer sur Entrée pour continuer . . .")
#def affichage(F):
    