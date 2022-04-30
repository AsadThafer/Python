import pygame
from game import Game

pygame.init()
pygame.display.set_caption('Crossy RPG Game - By Asad Asad')

game = Game()    #call class
game.run_game_loop()  #call function


pygame.quit() #quit pygame
quit()