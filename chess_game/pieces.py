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
            
    