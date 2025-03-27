import pygame
from pygame.locals import *
from objets import *

class Generateur():

    def __init__(self):
        print("création bouton générateur")

    def creation_objet(self, listeObjets):
        listeObjets.append(Objet())
