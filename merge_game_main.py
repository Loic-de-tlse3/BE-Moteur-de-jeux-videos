"""
Fichier principal du jeu appelant la routine de jeu.
"""

import pygame #import de la librarie Pygame
#from utils.Game import * #import du module Game contenant les principales
                        #fonctions permettant de lancer le jeu
from utils2.game import *

"""Routine de jeu initilisant les principaux attributs tels que : la librairie Pygame
la fenêtre de jeu, les images principales au lancement du jeu et lançant la routine de jeu
et enfin éteint le jeu en arrêtant la librairie Pygame."""

#initialisation de la librairie Pygame
pygame.init()

#Initialisation de la taille de la fenêtre (X px * Y px)
screen =  pygame.display.set_mode((1200, 700))

#Initialisation des principales images à utiliser pour le jeu
arriere_plan = pygame.image.load('./graphics_files/fond_ecran.png').convert()
cadre_null = pygame.image.load('./graphics_files/Cadre_null.png').convert_alpha()

#Initialisation du jeu
game = Game(screen,arriere_plan,cadre_null)

#Lancement de la routine de jeu
game.run()

#Extinction du jeu / Arrêt de la librairie Pygame
pygame.quit()