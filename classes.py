# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:22:54 2019

@author: LordOf20th
"""

class Arbre:
    """ Classe définissant un arbre, caractérisé par :
    - Son état : Sain ou En feu (par défaut à sa création l'arbre est considéré Sain)
    - Sa position en x et y """
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.brule=False
    def enflammer(self):
        """ Méthode pour enflammer l'arbre"""
        
        if not self.brule:
            self.brule = True