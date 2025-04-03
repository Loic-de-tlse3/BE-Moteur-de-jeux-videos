import pygame
from pygame.locals import *
from sys import exit
from enum import Enum
from random import randint

IMAGE_TAILLE = 105

class Type(Enum):
    DISTANT = 1
    CAC = 2

class Objet(pygame.sprite.Sprite):
    """
    Classe des objets dans le jeu
    """
    
    def __init__(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.niveau = 1
        self.type = Type(randint(1, 2))
        self.majApparence()
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.apparence.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.rect.height = IMAGE_TAILLE
        self.rect.width = IMAGE_TAILLE

    def majApparence(self):
        if self.type == Type.DISTANT:
            #TODO
            print("Mise à jour du sprite pour une arme distante")
            self.image1 = '../Projet BE images/gun.png'
            self.image2 = '../Projet BE images/rifle.png'
            self.image3 = '../Projet BE images/space-gun.png'
        else:
            #TODO
            print("Mise à jour du sprite pour une arme càc")
            self.image1 = '../Projet BE images/knife.png'
            self.image2 = '../Projet BE images/sword.png'
            self.image3 = '../Projet BE images/spears.png'
        self.apparence = pygame.image.load(self.image1).convert_alpha()

    def getType(self):
        return self.type

    def getNiveau(self):
        return self.niveau
    
    def getPos_x(self):
        return self.pos_x

    def getPos_y(self):
        return self.pos_y
    
    def destruction(self, listeObjets: list) -> None:
        """
        Détruit l'objet en le supprimant de la liste des objets.
        """
        #TODO
        print("destruction du sprite")

        if self in listeObjets:
            listeObjets.remove(self)

    def fusionner(self, objet, liste_objet: list) -> None:
        if (self.type != objet.getType()) or (self.niveau == 3) or (objet.getNiveau() == 3):
            #TODO
            print("refuser la fusion")
        else:
            #TODO
            print("Accepter la fusion")
            self.niveau += 1
            objet.destruction(objet, liste_objet)
            if self.niveau == 2:
                self.apparence = pygame.image.load(self.image2).convert()
            else:
                self.apparence = pygame.image.load(self.image3).convert()