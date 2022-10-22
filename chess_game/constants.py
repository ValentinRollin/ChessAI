import pygame
import os

largeur, longueur = 760,760
lignes, colonnes = 8,8
case = largeur/12


marron = (87,16,16)
blanc = (255,255,255)

Path = "chess_game/chess_images"

#black peieces

noir_cav = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bKN.png")),(case, case))
noir_fou = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bB.png")),(case, case))
noir_roi = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bK.png")),(case, case))
noir_pion = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bP.png")),(case, case))
noir_reine = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bQ.png")),(case, case))
noir_tour = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bR.png")),(case, case))
#white pieces 

blanc_cav = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wKN.png")),(case, case))
blanc_fou = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wB.png")),(case, case))
blanc_roi = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wK.png")),(case, case))
banc_pion = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wp.png")),(case, case))
blanc_reine = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wQ.png")),(case, case))
blanc_tour = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wR.png")),(case, case))
