from tokenize import Whitespace
from numpy import blackman
import pygame
from .board import newBoard
from .constants import *
from copy import deepcopy

class Game :
    def __init__(self, largeur, longueur, lignes, colonnes, case, Win) :
        self.Win = Win
        self.Board = newBoard(largeur, longueur, lignes, colonnes, case, Win)
        self.case = case
        self.selected = None
        self.turn = White
        self.valide_moves = []
        self.Black_pieces_left = 16
        self.White_pieces_left = 16

    def update_window(self):
        self.Board.draw_Board()
        self.Board.draw_pieces()
        self.draw_available_moves()
        pygame.display.update()

    def reset(self) :
        self.Board = newBoard(largeur, longueur, lignes, colonnes,case, Win)
        self.selected = None
        self.Black_pieces_left, self.White_pieces_left = 16,16
        self.valide_moves = []

    def change_turn(self):
        if self.turn == White :
            self.turn = Black
        else :
            self.turn = White 

    def select(self, ligne, col):
        if self.selected :
            move = self._move(ligne, col)

            if not move : 
                self.selected = None
                self.selected(ligne, col)

        piece = self.Board.get_piece(ligne, col)
        if piece != 0 and self.turn == piece.color :
            self.selected = piece

            self.valide_moves = piece.get_available_moves(ligne, col, self.Board.Board)

    def _move(self, ligne, col):
        piece = self.Board.get_piece(ligne, col)

        if self.selected and (ligne, col) in self.valide_moves :
            if piece == 0 or piece.color != self.selected.color:
                if self.simulate_move(self.selected, ligne, col):
                    self.remove(self.selected, ligne, col)
                    self.Board.move(self.Board.Board, piece, ligne, col)
                    self.change_turn()
                    self.valide_moves = []
                    self.selected = None
                    return True
                return False

        return False

    def remove(self, board, piece, ligne, col):
        if piece != 0: 
            board[ligne][col] = 0
            if piece.color == White :
                self.White_pieces_left -= 1
            else :
                self.Black_pieces_left -=1

    def draw_available_moves(self):
        if len(self.valide_moves) > 0 :
            for pos in self.valide_moves :
                ligne, col = pos[0],pos[1]
                pygame.draw.circle(self.Win, Green, (col*self.case + self.case//2), self.case//8)
