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

    def check_game(self):
        if self.checkmate(self.Board):
            if self.turn == White:
                print("Black wins")
                return True
            else: 
                print("White wins")
                return True
    
    def enemies_moves (self, piece, Board):
        ennemies_moves = []
        for r in range(len(Board)) :
            for c in range(len(Board[r])):
                if Board[r][c] != 0 :
                    if Board[r][c].color != piece.color :
                        moves = Board[r][c].get_available_moves(r,c,Board)
                        for move in moves :
                            ennemies_moves.append(move)
        return ennemies_moves

    def get_King_pos(self, Board):
        for r in range(len(Board)):
            for c in range(len(Board)):
                if Board[r][c] != 0:
                    if Board[r][c].type == "King" and Board[r][c].color == self.turn:
                        return (r,c)
        

    def simulate_moves(self, piece, ligne, col):
        piece_ligne, piece_col = piece.ligne, piece.col
        save_piece = self.Board.Board[ligne][col]

        if self.Board.Board[ligne][col] != 0:
            self.Board.Board[ligne][col] = 0

        self.Board.Board[piece.ligne][piece.col], self.Board.Board[ligne][col] = self.Board.Board[ligne][col], self.Board.Board[piece.ligne][piece.col]

        king_pos = self.get_King_pos(self.Board.Board)
        if king_pos in self.enemies_moves(piece, self.Board.Board):
            piece.ligne, piece.col = piece_ligne, piece_col 
            self.Board[piece_ligne][piece_col] = piece
            self.Board.Board[ligne][col] = save_piece 
            return False
        
        piece.ligne, piece.col = piece_ligne, piece_col
        self.Board.Board[piece_ligne][piece_col] = piece
        self.Board.Board[ligne][col] = save_piece
        return True

    def possible_moves(self, Board):
        possible_moves = []
        for r in range(len(Board)):
            for c in range (len(Board[r])):
                if Board[r][c] != 0:
                    if Board[r][c].color == self.turn and Board[r][c].type != "King":
                        moves = Board[r][c].get_availables_moves(r,c,Board)

                        for move in moves :
                            possible_moves.append(move)

        return possible_moves

    def checkmate(self,Board):
        king_pos = self.get_King_pos(Board.Board)
        get_king = Board.get_piece(king_pos[0], king_pos[1])

        king_available_moves = set(get_king.availables_moves(king_pos[0],king_pos[1],Board.Board))
        enemies_moves_set = set(self.enemies_moves(get_king, Board.Board))
        king_moves = king_available_moves - enemies_moves_set
        set1 = king_available_moves.intersection(enemies_moves_set)
        possible_moves_to_def = set1.intersection(self.possible_moves(Board.Board))

        if len(king_moves)==0 and len(king_available_moves) != 0 and possible_moves_to_def == 0:
            return True

        return False