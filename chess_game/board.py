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
        self.colonnes = colonnes
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

                #ligne pieces noir
                if ligne == 0 : 
                    # cas de la tour
                    if col == 0 or col == 7: 
                        self.Board[ligne][col] == Rook(self.case, noir_tour, Black, "Rook", ligne, col)

                    #cas du cavalier
                    if col == 1 or col == 6 :
                        self.Board[ligne][col] == Knight(self.case, noir_cav, Black, "Knight",ligne, col)

                    #cas du fou
                    if col == 2 or col == 5 :
                        self.Board[ligne][col] == Bishop(self.case, noir_fou, Black, "Bishop", ligne, col)

                    #cas de la reine
                    if col == 3 :
                        self.Board[ligne][col] == Queen(self.case, noir_reine, Black, "Queen", ligne, col)

                    #cas du roi
                    if col == 4 :
                        self.Board[ligne][col] == King(self.case, noir_roi, Black, "King", ligne, col)
                
                #ligne pieces blanches
                if ligne == 7 :
                    # cas de la tour
                    if col == 0 or col == 7: 
                        self.Board[ligne][col] == Rook(self.case, blanc_tour, White, "Rook", ligne, col)

                    #cas du cavalier
                    if col == 1 or col == 6 :
                        self.Board[ligne][col] == Knight(self.case, blanc_cav, White, "Knight",ligne, col)

                    #cas du fou
                    if col == 2 or col == 5 :
                        self.Board[ligne][col] == Bishop(self.case, blanc_fou, White, "Bishop", ligne, col)

                    #cas de la reine
                    if col == 3 :
                        self.Board[ligne][col] == Queen(self.case, blanc_reine, White, "Queen", ligne, col)

                    #cas du roi
                    if col == 4 :
                        self.Board[ligne][col] == King(self.case, blanc_roi, White, "King", ligne, col)                
                        

    def get_piece(self, ligne, col) :
        return self.Board[ligne][col]

    def move(self,piece,ligne, col):
        self.Board[piece.ligne][piece.col], self.Board[ligne][col] = self.Board[ligne, col], self.Board[piece.ligne][piece.col]

        piece.piece_move(ligne, col)

        if piece.type == "Pawn":
            if piece.first_move : 
                piece.first_move = False

    def draw_Board(self):
        self.win.fill(marron)

        for ligne in range (self.lignes) :
            for col in range(ligne%2, colonnes, 2):
                pygame.draw.react(self.win, blanc, (case*(ligne), case*(col), case, case))

    def draw_piece(self, piece, Win):
        Win.blit(piece.image, (piece.x, piece.y))

    def draw_pieces(self):
        for ligne in range(self.lignes):
            for col in range(self.colonnes):
                if self.Board[ligne][col] != 0:
                    self.draw_piece(self.Board[ligne][col],self.win)

                    





















