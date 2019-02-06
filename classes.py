# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 22:22:54 2019

@author: LordOf20th
"""

class Arbre:
    """ Classe définissant un arbre, caractérisé par :
    - Son état : Sain ou En feu (par défaut à sa création l'arbre est considéré Sain)
    - Sa position en x et y """
    def __init__(self):
        self._etat=0
    def _get_etat(self):
        """ Méthode pour lire l'état de l'arbre"""
        return self._etat
    def _set_etat(self, nouvel_etat):
        """ Mutateur de l'attribut état """
        if nouvel_etat == 0 or nouvel_etat == 1 or nouvel_etat == -1:
            self._etat=nouvel_etat
        else: 
            raise ValueError("Valeur d'état invalide, seules 0, 1 et -1 sont valides")
    etat=property(_get_etat, _set_etat)
    def __repr__(self):
        if self._etat == 0 :
            return "Sain"
        elif self._etat == 1:
            return "En feu"
        elif self._etat == -1:
            return "Mort"
            