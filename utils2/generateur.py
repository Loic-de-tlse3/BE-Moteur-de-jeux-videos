"""Module Generateur qui implémente la classe Générateur, ses attributs et méthodes pour la génération d'objets."""

import pygame
from pygame.locals import *
from utils2.objets import Objet

class Generateur(pygame.sprite.Sprite):
    """Classe représentant le bouton générateur d'objets."""

    # Relation d'association explicite
    _creates = Objet  # Indique que Generateur crée des objets Objet
    # Constantes de classe
    DISTANCE_OBJET = 175  # Distance entre deux objets
    NB_ITEM_MAX = 18  # Nombre d'items maximum du tableau
    NB_ITEM_LIGNE = 6  # Nombre d'items maximum dans une ligne
    IMAGE_TAILLE = 128  # Taille de l'image générée
    TAILLE_CADRE = 163  # Taille du cadre
    X_INITIAL = 96  # Coordonnée initiale x
    Y_INITIAL = 150  # Coordonnée initiale y
    
    # Coordonnées initiales du cadre
    X_INITIAL_CADRE = X_INITIAL - ((TAILLE_CADRE - IMAGE_TAILLE) / 2)
    Y_INITIAL_CADRE = Y_INITIAL - ((TAILLE_CADRE - IMAGE_TAILLE) / 2)

    def __init__(self):
        """Initialise le bouton générateur avec sa position et son apparence."""
        # Initialiser la classe parente Sprite
        super().__init__()
        
        print("Création bouton générateur")
        
        # Position du générateur
        self.pos_x = self.X_INITIAL
        self.pos_y = self.Y_INITIAL

        # Position du prochain objet à générer
        self.next_object_x = self.X_INITIAL + self.DISTANCE_OBJET
        self.next_object_y = self.Y_INITIAL
        
        # Chargement des ressources graphiques
        self.image = 'graphics_files/Bouton.png'
        self.apparence = pygame.image.load(self.image).convert_alpha()
        self.cadre = pygame.image.load('graphics_files/Cadre_null.png').convert_alpha()
        
        # Configuration des rectangles pour la collision et l'affichage
        self.rect = self.apparence.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)
        self.rect.height = self.IMAGE_TAILLE
        self.rect.width = self.IMAGE_TAILLE
        
        self.rectCadre = self.cadre.get_rect()
        self.rectCadre.center = (self.pos_x + (self.IMAGE_TAILLE/2), 
                                self.pos_y + (self.IMAGE_TAILLE/2))

        # Nouvelle liste pour suivre les emplacements libres
        self.emplacements_libres = []
        
        # Tableau représentant les positions de tous les emplacements possibles
        self.grille_positions = []
        self._initialiser_grille_positions()
    
    def _initialiser_grille_positions(self):
        """Initialise un tableau contenant toutes les positions possibles de la grille."""
        for ligne in range(self.NB_ITEM_MAX // self.NB_ITEM_LIGNE):
            for colonne in range(self.NB_ITEM_LIGNE):
                x = self.X_INITIAL + colonne * self.DISTANCE_OBJET
                y = self.Y_INITIAL + ligne * self.DISTANCE_OBJET
                
                if x == self.X_INITIAL and y == self.Y_INITIAL:
                    continue  # On saute la position du générateur
                    
                self.grille_positions.append((x, y))
    
    def marquer_emplacement_libre(self, x, y):
        """
        Marque un emplacement comme libre.
        
        Args:
            x (int): Coordonnée X de l'emplacement
            y (int): Coordonnée Y de l'emplacement
        """
        position = (x, y)
        if position not in self.emplacements_libres and position in self.grille_positions:
            self.emplacements_libres.append(position)
            print(f"Emplacement ({x}, {y}) marqué comme libre")

    def creation_objet(self, liste_objets: list):
        """
        Crée un nouvel objet en privilégiant les emplacements libres.
        
        Args:
            liste_objets (list): Liste contenant tous les objets du jeu
            
        Returns:
            Objet: L'objet créé ou None si la création a échouée
        """
        nb_item = len(liste_objets)
        
        if nb_item < self.NB_ITEM_MAX:
            # Si des emplacements libres existent, on utilise le premier
            if self.emplacements_libres:
                position = self.emplacements_libres.pop(0)
                pos_x, pos_y = position
                print(f"Création d'un nouvel objet à l'emplacement libre ({pos_x}, {pos_y})")
            else:
                # Sinon, on utilise la position suivante normale
                pos_x, pos_y = self.next_object_x, self.next_object_y
                print(f"Création d'un nouvel objet à la position séquentielle ({pos_x}, {pos_y})")
                # Et on met à jour pour le prochain objet
                self._modification_coordonnees(nb_item + 1)
            
            # Création et ajout du nouvel objet
            nouvel_objet = Objet(pos_x, pos_y)
            liste_objets.append(nouvel_objet)
            return nouvel_objet
        else:
            print("Le jeu est plein, impossible de générer un nouvel objet")
            return None

    def _modification_coordonnees(self, nb_item: int) -> None:
        """
        Met à jour les coordonnées pour le prochain objet à générer.
        
        Args:
            nb_item (int): Nombre d'objets actuellement dans le jeu
        """
        # Déplacement horizontal
        self.next_object_x += self.DISTANCE_OBJET
        
        # Si on atteint la fin d'une ligne, on passe à la ligne suivante
        if nb_item % self.NB_ITEM_LIGNE == 0:
            self.next_object_x = self.X_INITIAL
            self.next_object_y += self.DISTANCE_OBJET

    def getPos_x(self) -> int:
        """
        Retourne la position X du générateur.
        
        Returns:
            int: Coordonnée X du générateur
        """
        return self.pos_x

    def getPos_y(self) -> int:
        """
        Retourne la position Y du générateur.
        
        Returns:
            int: Coordonnée Y du générateur
        """
        return self.pos_y
    
    @classmethod
    def get_grid_info(cls):
        """
        Retourne les informations de positionnement pour la grille d'objets.
        
        Returns:
            tuple: (X_INITIAL_CADRE, Y_INITIAL_CADRE, DISTANCE_OBJET, NB_ITEM_LIGNE, NB_ITEM_MAX)
        """
        return (cls.X_INITIAL_CADRE, cls.Y_INITIAL_CADRE, 
                cls.DISTANCE_OBJET, cls.NB_ITEM_LIGNE, cls.NB_ITEM_MAX)
