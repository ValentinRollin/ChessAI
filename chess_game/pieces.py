import pygame
from .constants import *

class Piece : 
    def __init__(self, case, image, color, type, ligne, col):
        self.case = case
        self.image = image
        self.color = color
        self.type = type
        self.ligne = ligne
        self.col = col
        self.x = 0
        self.y = 0
        self.availables_moves = []

    def piece_move(self,ligne,col):
        self.ligne = ligne
        self.col = col
        self.calc_pos()

    def calc_pos():
        self.x = self.col*self.case
        self.y = self.ligne*self.case

    def clear_available_moves(self):
        if len(self.available_moves) > 0:
            self.availables_moves = []

class Pawn(Piece) :
    def __init__(self, case, image, color, type, ligne, col):
        super().__init__(case, image, color, type, ligne, col)
        self.first_move = True

    def get_available_moves(self, ligne, col, Board):
        self.clear_available_moves()

        if self.color == White : # tous les mouvements du pion blanc
            if ligne -1>=0:
                if Board[ligne-1][col] == 0:
                    self.availables_moves.append((ligne-1,col))
                if self.first_move :
                    if Board[ligne -1][col] == 0 and Board[ligne-2][col] == 0:
                        self.availables_moves.append((ligne-2,col))
                if col-1 >=0:
                    if Board[ligne-1][col-1] != 0:
                        piece = Board[ligne-1][col-1]
                        if piece.color != self.color:
                            self.availables_moves.append((ligne-1,col-1))
                if col+1 <len(Board[0]): #diagonale a droite de la piece
                    if Board[ligne-1][col+1] != 0 :
                        piece = Board[ligne-1][col-1]

                        if piece.color != self.color:
                            self.availables_moves.append((ligne-1, col+1))
        
        if self.color == Black : # tous les mouvements du pion noir
            if ligne+1 < len(Board) :
                if Board[ligne+1][col] == 0:
                    self.availables_moves.append((ligne+1,col))
                
                if self.first_move:
                    if Board[ligne+1][col] == 0 and Board[ligne+2][col] == 0:
                        self.availables_moves.append((ligne+2,col))
                    
                if col-1 >= 0:
                    if Board[ligne+1][col-1] != 0:
                        piece = Board[ligne+2][col-1]
                        if piece.color != self.color:
                            self.availables_moves.append((ligne+1,col-1))
                if col+1 < len(Board):
                    if Board[ligne+1][col+1] != 0:
                        piece = Board[ligne+1][col+1]
                        if piece.color != self.color:
                            self.availables_moves.append((ligne+1,col+1))
        return self.available_moves
