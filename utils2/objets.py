"""Module objets qui implémente la classe Objet, ses attributs et ses méthodes."""
import pygame
from pygame.locals import *
from enum import Enum
from random import randint

# Définition de la classe Type initialisant les types d'armes (Distance, Corps à Corps)
class Type(Enum):
    """Classe des Types d'objets soit une arme de type corps à corps ou de type distance."""
    
    DISTANT = 1
    CAC = 2

class Objet(pygame.sprite.Sprite):
    """Classe des objets (armes) dans le jeu."""

    # Constantes de classe
    IMAGE_TAILLE = 128
    
    def __init__(self, pos_x: int, pos_y: int) -> None:
        """
        Initialise un objet avec une position et des attributs aléatoires.
        
        Args:
            pos_x (int): Position horizontale de l'objet
            pos_y (int): Position verticale de l'objet
        """
        # Initialiser la classe parente Sprite
        super().__init__()
        
        # Position de l'objet
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        # Attributs de l'objet
        self.niveau = 1
        self.type = Type(randint(1, 2))
        
        # Chargement des ressources graphiques
        self._initialiser_ressources()
        self._maj_apparence()
        
        # Configuration des rectangles pour la collision
        self.rect = self.apparence.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.rect.height = self.IMAGE_TAILLE
        self.rect.width = self.IMAGE_TAILLE
        self.rectCadre = self.cadre.get_rect()
        self.rectCadre.center = (self.pos_x + (self.IMAGE_TAILLE/2), self.pos_y + (self.IMAGE_TAILLE/2))

    def _initialiser_ressources(self):
        """Initialise les chemins vers les ressources graphiques selon le type de l'objet."""
        # Chemins des images de cadre (communs à tous les types)
        self.cadre1 = 'graphics_files/Cadre_nv1.png'
        self.cadre2 = 'graphics_files/Cadre_nv2.png'
        self.cadre3 = 'graphics_files/Cadre_nv3.png'
        
        # Chemins des images selon le type d'arme
        if self.type == Type.DISTANT:
            self.image1 = 'graphics_files/gun.png'
            self.image2 = 'graphics_files/rifle.png'
            self.image3 = 'graphics_files/space-gun.png'
        else:  # Type.CAC
            self.image1 = 'graphics_files/knife.png'
            self.image2 = 'graphics_files/sword.png'
            self.image3 = 'graphics_files/spears.png'

    def _maj_apparence(self):
        """Met à jour l'apparence de l'objet selon son niveau."""
        # Sélection de l'image selon le niveau
        if self.niveau == 1:
            self.apparence = pygame.image.load(self.image1).convert_alpha()
            self.cadre = pygame.image.load(self.cadre1).convert_alpha()
        elif self.niveau == 2:
            self.apparence = pygame.image.load(self.image2).convert_alpha()
            self.cadre = pygame.image.load(self.cadre2).convert_alpha()
        else:  # niveau 3
            self.apparence = pygame.image.load(self.image3).convert_alpha()
            self.cadre = pygame.image.load(self.cadre3).convert_alpha()

        # Mettre à jour la position des rectangles
        self.rect = self.apparence.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)
        self.rectCadre = self.cadre.get_rect()
        self.rectCadre.center = (self.pos_x + (self.IMAGE_TAILLE/2), self.pos_y + (self.IMAGE_TAILLE/2))
    
    def getType(self) -> Type:
        """
        Retourne le type de l'arme.
        
        Returns:
            Type: Type de l'arme (DISTANT ou CAC)
        """
        return self.type

    def getNiveau(self) -> int:
        """
        Retourne le niveau de l'arme.
        
        Returns:
            int: Niveau de l'arme (1-3)
        """
        return self.niveau
    
    def getPos_x(self) -> int:
        """
        Retourne la position X de l'objet.
        
        Returns:
            int: Coordonnée X de l'objet
        """
        return self.pos_x

    def getPos_y(self) -> int:
        """
        Retourne la position Y de l'objet.
        
        Returns:
            int: Coordonnée Y de l'objet
        """
        return self.pos_y
    
    def destruction(self, liste_objets: list) -> None:
        """
        Détruit l'objet en le supprimant de la liste des objets.
        
        Args:
            liste_objets (list): Liste contenant tous les objets du jeu
        """
        if self in liste_objets:
            liste_objets.remove(self)
            # On pourrait ajouter un effet de destruction ici (animation, son, etc.)
            print(f"Objet de type {self.type.name} de niveau {self.niveau} détruit")

    def fusionner(self, autre_objet, liste_objets: list) -> bool:
        """
        Fusionne cet objet avec un autre objet compatible.
        
        Args:
            autre_objet (Objet): L'objet avec lequel fusionner
            liste_objets (list): Liste contenant tous les objets du jeu
            
        Returns:
            bool: True si la fusion a réussi, False sinon
        """
        # Vérification de la compatibilité pour la fusion
        if (self.type != autre_objet.getType()) or (self.niveau == 3) or (autre_objet.getNiveau() == 3):
            print(f"Fusion refusée: types incompatibles ou niveau max atteint")
            return False
        
        if self.niveau != autre_objet.getNiveau():
            print(f"Fusion refusée: niveaux différents")
            return False
            
         # Fusion acceptée - c'est autre_objet qui monte de niveau
        print(f"Fusion acceptée: {autre_objet.type.name} niveau {autre_objet.niveau} -> {autre_objet.niveau + 1}")
        autre_objet.niveau += 1
        autre_objet._maj_apparence()  # Mettre à jour l'apparence de l'objet amélioré
    
        # Détruire l'objet courant (celui qu'on a déplacé)
        self.destruction(liste_objets)
        return True
