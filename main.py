import pygame

from chess_game.constants import *

pygame.init()

clock = pygame.time.Clock()

win = pygame.display.set_mode((largeur,longueur))

def get_position(x,y):
    row = y//case
    col = x//case

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

                if event.type == pygame.KEYDOWN :
                    if event.type == pygame.K_SPACE and game_over: 
                        pass

                if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    if pygame.mouse.get_pressed()[0]: # 0 pour clique gauche
                        location = pygame.mouse.get_pos() #recp les coordonnées du clique
                        ligne,col = get_position(location[0], location[1]) #x=0 y=1


main()
