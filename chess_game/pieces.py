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


class Rook(Piece):

    def __init__(self, case, image, color, type, ligne, col):
        super().__init__(case, image, color, type, ligne, col)

    def get_available_moves(self, ligne, col, Board):
        self.clear_available_moves()

        for i in range(ligne+1,8): #mouvement devant
            if Board[i][col] == 0 :
                self.availables_moves.append((i,col)) 
            else : 
                if Board[i][col].color != self.color :
                    self.availables_moves.append((i,col))
                    break
                else: 
                    break 
                    
        for j in range(ligne-1,-1,-1): #mouvement derriere
            if Board[j][col] == 0:
                self.availables_moves.append((j,col))
            else:
                if Board[j][col].color != self.color:
                    self.availables_moves.append((j,col))
                    break
                else :
                    break

        for i in range(col+1,8): #mouvement droite
            if Board[ligne][i] == 0:
                self.availables_moves.append((ligne,i))
            else:
                if Board[i][col].color != self.color:
                    self.availables_moves.append((ligne,i))
                    break
                else :
                    break
        for j in range(col-1,-1,-1) : #mouvement gauche
            if Board[ligne][j] == 0:
                self.availables_moves.append((ligne,j))
            else:
                if Board[ligne,j].color != self.color:
                    self.availables_moves.append((ligne,j))
                    break
                else:
                    break

        return self.availables_moves