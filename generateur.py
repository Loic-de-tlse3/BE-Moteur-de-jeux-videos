import pygame
from pygame.locals import *
from objets import *

X_INITIAL = 96
Y_INITIAL = 150
DISTANCE_OBJET = 175
NB_ITEM_MAX = 18
NB_ITEM_LIGNE = 6

class Generateur(pygame.sprite.Sprite):

    def __init__(self):
        print("création bouton générateur")
        self.pos_x = X_INITIAL
        self.pos_y = Y_INITIAL
        self.next_object_x = X_INITIAL + DISTANCE_OBJET
        self.next_object_y = Y_INITIAL
        self.image = '../Projet BE images/Bouton.png'
        self.apparence = pygame.image.load(self.image).convert_alpha()
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.apparence.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)
        self.rect.height = IMAGE_TAILLE
        self.rect.width = IMAGE_TAILLE
        self.cadre = pygame.image.load('../Projet BE images/Cadre null.png').convert_alpha()
        self.rect.width = IMAGE_TAILLE
        self.rectCadre = self.cadre.get_rect()
        self.rectCadre.center = (self.pos_x+(IMAGE_TAILLE/2), self.pos_y+(IMAGE_TAILLE/2))

    def creation_objet(self, listeObjets: list) -> None:
        nb_item = listeObjets.__len__()
        if nb_item < NB_ITEM_MAX:
            print("Insertion d'un nouvel objet")
            listeObjets.append(Objet(self.next_object_x, self.next_object_y))
            nb_item += 1
            self.modification_coordonnees(nb_item)
        else: 
            print("Le jeu est plein on ne peut plus générer")

    def modification_coordonnees(self, nb_item: int) -> None:
        self.next_object_x += DISTANCE_OBJET
        if nb_item % NB_ITEM_LIGNE == 0:
            self.next_object_x = X_INITIAL
            self.next_object_y = self.next_object_y + DISTANCE_OBJET

    def getPos_x(self):
        return self.pos_x

    def getPos_y(self):
        return self.pos_y
