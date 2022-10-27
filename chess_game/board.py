import pygame
from .pieces import *
from .constants import *

class newBoard:
    def __init__(self, largeur, longueur, lignes, colonnes, case, win ):
        self.largeur = largeur
        self.longueur = longueur
        self.case = case
        self.win = win
        self.lignes = lignes
        self.colonne = colonnes
        self.Board = []
        self.create_Board()

    def create_Board(self):
        for ligne in range(self.lignes):
            self.Board.append([0 for i in range(self.colonnes)])

            for col in range(self.colonnes):
                #ligne pions noir
                if ligne == 1 :
                    self.Board[ligne][col] = Pawn(self.case,noir_pion, Black, "Pawn", ligne, col)

                #ligne pions blanc
                if ligne == 6 :
                    self.Board[ligne][col] = Pawn(self.case, blanc_pion, White, "Pawn", ligne, col)

            
























