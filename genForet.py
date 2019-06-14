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
        - -1 : un arbre en feu
        - -2 : un arbre mort
        -  0 : pas d'arbre
        -  1 : un arbre sain
        -  2 : bordure
"""

# Fonctions agissant sur la matrice


def genForet(n, p):
    ''' Fonction générant la forêt '''
    if n >= 2:
        foret = np.full(shape=(n, n), fill_value=0)
        for i in range(0, foret.shape[0]):
            for j in range(0, foret.shape[1]):
                if random.random() <= p:
                    foret[i, j] = 1
        return foret
    else:
        raise ValueError("n doit prendre une valeur de 2 au moins")


def genForetBordure(n, p):
    ''' Fonction générant la forêt et une bordure '''
    if n >= 2:
        foret = np.full(shape=(n+1, n+1), fill_value=0)
        for i in range(0, foret.shape[0]):
            for j in range(0, foret.shape[1]):
                if i == 0 or j == 0 or j == n or i == n:
                    foret[i, j] = 2
                else:
                    if random.random() <= p:
                        foret[i, j] = 1
        return foret
    else:
        raise ValueError("n doit prendre une valeur de 2 au moins")


def enflammer(foret, x, y):
    ''' Fonction mettant le feu aléatoirement à une case '''
    if x == -1:
        x = random.randint(0, foret.shape[0]-1)
    if y == -1:
        y = random.randint(0, foret.shape[1]-1)
    foretEnflammée = np.copy(foret)
    foretEnflammée[x, y] = -1
    return foretEnflammée


def enflammerBordure(foret, x, y):
    ''' Fonction mettant le feu aléatoirement à une case
    en tenant compte de la bordure'''
    if x == -1 or x == 0 or x == foret.shape[0]-1:
        x = random.randint(1, foret.shape[0]-2)
    if y == -1 or y == 0 or y == foret.shape[1]-1:
        y = random.randint(1, foret.shape[1]-2)
    foretEnflammée = np.copy(foret)
    foretEnflammée[x, y] = -1
    return foretEnflammée


def propager(F, k, i, j):
    ''' Propage le feu au k ieme tour '''
    try:
        if F[k-1][i-1, j] == 1:  # Si la case au dessus est un arbre
            F[k][i-1, j] = -1  # La case au dessus brûle
    except IndexError:
        pass
    try:
        if F[k-1][i+1, j] == 1:  # Si la case au dessous est un arbre
            F[k][i+1, j] = -1  # La case en dessous brûle
    except IndexError:
        pass
    try:
        if F[k-1][i, j-1] == 1:  # Si la case à gauche est un arbre
            F[k][i, j-1] = -1  # La case à gauche brûle
    except IndexError:
        pass
    try:
        if F[k-1][i, j+1] == 1:  # Si la case à droite est un arbre
            F[k][i, j+1] = -1  # La case à droite brûle
    except IndexError:
        pass


def propager2(F, k, i, j):
    ''' Propage le feu au k ieme tour '''
    print("rang :" + str(k) + " (" + str(i) + "," + str(j) + ")")
    # On ajuste les indices pour rester dans les index
    i = i-1
    j = j-1
    if i == 0:  # On est sur la ligne du haut
        if F[k-1][i+1, j] == 1:  # Si la case au dessous est un arbre
            F[k][i+1, j] = -1  # La case en dessous brûle
    elif i == F[k].shape[0]-1:  # On est sur la ligne du bas
        if F[k-1][i-1, j] == 1:  # Si la case au dessus est un arbre
            F[k][i-1, j] = -1  # La case au dessus brûle
    else:
        if F[k-1][i-1, j] == 1:  # Si la case au dessus est un arbre
            F[k][i-1, j] = -1  # La case au dessus brûle
        if F[k-1][i+1, j] == 1:  # Si la case au dessous est un arbre
            F[k][i+1, j] = -1  # La case en dessous brûle
    if j == 0:  # On est sur la colonne de gauche
        if F[k-1][i, j+1] == 1:  # Si la case à droite est un arbre
            F[k][i, j+1] = -1  # La case à droite brûle
    elif j == F[k].shape[1]-1:  # On est sur la colonne de droite
        if F[k-1][i, j-1] == 1:  # Si la case à gauche est un arbre
            F[k][i, j-1] = -1  # La case à gauche brûle
    else:  # On est sur aucune des colonnes latérales
        if F[k-1][i, j-1] == 1:  # Si la case à gauche est un arbre
            F[k][i, j-1] = -1  # La case à gauche brûle
        if F[k-1][i, j+1] == 1:  # Si la case à droite est un arbre
            F[k][i, j+1] = -1  # La case à droite brûle


def feuDeForet(F):
    k = 2
    while -1 in F[k-1]:
        F.append(np.copy(F[k-1]))  # On copie la forêt du tour précédent
        for i in range(0, F[k].shape[0]):
            for j in range(0, F[k].shape[1]):
                if F[k-1][i, j] == -1:  # Si la case est en feu au rang k
                    if F[k-1][i, j] == 0:
                        ''' Si cette case ne portait pas d'arbre au rang k-1
                        alors on propage le feu et la case s'éteint '''
                        propager(F, k, i, j)
                        F[k][i, j] = 0
                    elif F[k-2][i, j] == -1:
                        '''Si la case était en feu au tour précédent :
                        propage et mort de l'arbre '''
                        propager(F, k, i, j)
                        F[k][i, j] = -2
                    else:
                        ''' La case a été mise en feu, elle propage le feu '''
                        propager(F, k, i, j)
        print(F[k], "Rang : {}".format(k))
        k = k+1


def feuDeForetBordure(F):
    k = 2
    while -1 in F[k-1]:
        F.append(np.copy(F[k-1]))  # On copie la forêt du tour précédent
        for i in range(0, F[k].shape[0]):
            for j in range(0, F[k].shape[1]):
                if F[k-1][i, j] == -1:  # Si la case est en feu au rang k
                    if F[k-1][i, j] == 0:
                        ''' Si cette case ne portait pas d'arbre au rang k-1
                        alors on propage le feu et la case s'éteint '''
                        propager(F, k, i, j)
                        F[k][i, j] = 0
                    elif F[k-2][i, j] == -1:
                        ''' Si la case était en feu au tour précédent :
                        propage et mort de l'arbre '''
                        propager(F, k, i, j)
                        F[k][i, j] = -2
                    else:
                        ''' La case a été mise en feu, elle propage le feu '''
                        propager(F, k, i, j)
        print(F[k], "Rang : {}".format(k))
        k = k+1


def wildfire(n, p, x=-1, y=-1):
    F = [genForet(n, p)]  # Génération de la forêt selon les paramètres voulus
    print(F[0], "Instant initial")
    F.append(enflammer(F[0], x, y))  # La forêt est enflammée puis stockée
    print(F[1], "Rang : 1 (Départ de feu)")
    feuDeForet(F)
    return F


def wildfireBordure(n, p, x=-1, y=-1):
    ''' Génération de la forêt selon les paramètres voulus '''
    F = [genForetBordure(n, p)]
    print(F[0], "Instant initial")
    ''' La forêt est enflammée puis stockée '''
    F.append(enflammerBordure(F[0], x, y))
    print(F[1], "Rang : 1 (Départ de feu)")
    feuDeForetBordure(F)
    return F


#  Affichage


def affichage(F):
    ''' Utilise la librairie tkinter pour l'affichage de la forêt '''
    for k in range(0, len(F)):
        fenetre = tk.Tk()  # Crée la fenêtre que l'on va modifier
        label = tk.Label(fenetre, text="Wildfire")  # Met en place le titre
        label.pack()
        ''' On définit le canevas qui affiche notre forêt '''
        canvas = tk.Canvas(fenetre, width=(F[k].shape[0]+2)*10,
                           height=(F[k].shape[1]+2)*10)
        tracerRectangles(F[k], canvas)
        canvas.pack()
        bouton = tk.Button(fenetre, text="Suivant", command=fenetre.destroy)
        bouton.pack()
        fenetre.mainloop()  # Affiche la fenêtre


def affichage2(F):
    ''' Utilise la librairie tkinter pour l'affichage de la forêt '''
    p = 1  # Initialise le 'pas' entre les rang de la forêt
    fenetre = tk.Tk()  # Crée la fenêtre que l'on va modifier
    label = tk.Label(fenetre, text="Wildfire")  # Met en place le titre
    label.pack()
    canvas = tk.Canvas(fenetre, width=(F[0].shape[0]+2)*10,
                       height=(F[0].shape[1]+2)*10)
    canvas.pack(side=tk.LEFT)
    tracerRectangles(F[0], canvas)  # On trace la forêt initiale
    global k
    k = 0  # Le rang
    # sPas = tk.Scale(fenetre, variable=p, orient=tk.HORIZONTAL, to=10)
    # sPas.pack(side=tk.BOTTOM)
    bSuivant = tk.Button(fenetre, text='Suivant '+str(p)+' tours', command=lambda: rangSuivant(F, p, k, canvas))
    bSuivant.pack()
    bQuit = tk.Button(fenetre, text='Quitter', command=fenetre.quit)
    bQuit.pack(side=tk.BOTTOM)
    fenetre.mainloop()
    fenetre.destroy()


# Fonctions utiles à l'affichage

def pause():
    input("Appuyer sur Entrée pour continuer . . .")


def tracerRectangles(F, canvas):
    ''' Trace les cases '''
    for i in range(0, F.shape[0]):
        for j in range(0, F.shape[1]):
            if F[i, j] == 1:
                canvas.create_rectangle((i+1)*10, (j+1)*10, (i+2)*10, (j+2)*10,
                                        fill='green', width=0)
            elif F[i, j] == -1:
                canvas.create_rectangle((i+1)*10, (j+1)*10, (i+2)*10, (j+2)*10,
                                        fill='red', width=0)
            elif F[i, j] == -2:
                canvas.create_rectangle((i+1)*10, (j+1)*10, (i+2)*10, (j+2)*10,
                                        fill='black', width=0)
            elif F[i, j] == 2:
                canvas.create_rectangle((i+1)*10, (j+1)*10, (i+2)*10, (j+2)*10,
                                        fill='#c0c0c0', width=0)


def rangSuivant(F, p, r, canvas):
    global k
    k = r + p  # On avance le rang du pas
    tracerRectangles(F[k], canvas)
    print(k)
