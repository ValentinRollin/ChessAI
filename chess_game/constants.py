import pygame
import os

largeur, longueur = 760,70
ligne, colonne = 8,8
carree = largeur // longueur


marron = (87,16,16)
blanc = (255,255,255)

Path = "chess_game/chess_images"

#black peieces

noir_cav = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bKN.png")),(carree, carree))
noir_fou = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bB.png")),(carree, carree))
noir_roi = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bK.png")),(carree, carree))
noir_pion = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bP.png")),(carree, carree))
noir_reine = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bQ.png")),(carree, carree))
noir_tour = pygame.transform.scale(pygame.image.load(os.path.join(Path,"bR.png")),(carree, carree))

#white pieces 

blanc_cav = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wKN.png")),(carree, carree))
blanc_fou = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wB.png")),(carree, carree))
blanc_roi = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wK.png")),(carree, carree))
banc_pion = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wp.png")),(carree, carree))
blanc_reine = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wQ.png")),(carree, carree))
blanc_tour = pygame.transform.scale(pygame.image.load(os.path.join(Path,"wR.png")),(carree, carree))
