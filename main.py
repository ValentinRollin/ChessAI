import pygame

from chess_game.constants import *

pygame.init()

clock = pygame.time.Clock()

win = pygame.display.set_mode((largeur,longueur))

def main():
        run = True
        FPS = 60
        while run:
            clock.tick(FPS)
            win.blit(blanc_fou, (50,50))

            pygame.display.update()

            
# Pour pouvoir fermer la fenetre quand on appuie sur la croix
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()

main()
