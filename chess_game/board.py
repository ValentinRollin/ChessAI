import pygame
from .pieces import *
from .constants import *

class newBoard:
    def __init__(self, largeur, longueur, lignes, colonnes, case, win ):
        self.largeur = largeur
        self.longueur = longueur
        self.case = case
        self.win = win
        self.ligne = lignes
        self.colonne = colonnes
        self.Board = []
        self.create_Board()

    def create_Board(self):
        for li in range(self.ligne):
            self.Board.append([0 for i in range(self.colonnes)])

            for col in range(self.colonnes):
                pass