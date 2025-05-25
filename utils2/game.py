"""Module game implémentant la classe Game, ses attributs et méthodes pour le fonctionnement du jeu."""
import pygame
import sys
from utils2.generateur import Generateur
from utils2.objets import Objet, Type

class Game:
    """Classe principale du jeu gérant la boucle de jeu, les événements et l'affichage."""

    # Couleur de fond pour effacer l'écran
    BLACK = (0, 0, 0)
    score = 0

    def __init__(self, screen, background, cadre):
        """
        Initialise le jeu avec ses composants principaux.
        
        Args:
            screen: Surface d'affichage pygame
            background: Image d'arrière-plan
            cadre: Image de cadre vide pour les emplacements
        """
        # Initialisation des attributs principaux
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        # Chargement des ressources graphiques
        self.arriere_plan = background
        self.cadre_null = cadre
        
        # Initialisation des objets du jeu
        self.listeObjets = []
        self.generateur = Generateur()
        self.listeObjets.append(self.generateur)
        
        # Attribut pour le suivi de l'objet sélectionné
        self.objet_selectionne = None
        
        # Récupération des informations de grille du générateur
        self.grid_info = Generateur.get_grid_info()
        
    def handling_events(self):
        """Gère les événements utilisateur (clavier, souris, etc.)."""
        for event in pygame.event.get():
            # Gestion de la fermeture du jeu
            if event.type == pygame.QUIT:
                self.running = False
                
            # Gestion des clics de souris
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic gauche
                    self._gerer_selection(event.pos)
            
            # Gestion du relâchement de la souris
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and self.objet_selectionne:
                    self._gerer_action_objet(event.pos)
    
    def _gerer_selection(self, position):
        """
        Gère la sélection d'un objet.
        
        Args:
            position: Tuple (x, y) de la position du clic
        """
        for objet in self.listeObjets:
            if objet.rect.collidepoint(position):
                if isinstance(objet, Generateur):
                    # Clic sur le générateur: création d'un nouvel objet
                    #print("Clic sur le bouton générateur")
                    self.generateur.creation_objet(self.listeObjets)
                elif isinstance(objet, Objet):
                    # Clic sur un objet: sélection pour déplacement ou fusion
                    #print(f"Sélection de l'objet {objet.getType().name} niveau {objet.getNiveau()}")
                    self.objet_selectionne = objet
                break
    
    def _gerer_action_objet(self, position):
        """
        Gère l'action à effectuer avec l'objet sélectionné (fusion ou déplacement).
        
        Args:
            position: Tuple (x, y) de la position du relâchement
        """
        # Vérifier si on relâche l'objet sur un autre objet -> fusion
        for objet in self.listeObjets:
            if (objet != self.objet_selectionne and 
                isinstance(objet, Objet) and 
                objet.rect.collidepoint(position)):
                # Tentative de fusion
                if self.objet_selectionne.fusionner(objet, self.listeObjets):
                    # Marquer l'emplacement de l'objet détruit comme libre
                    self.generateur.marquer_emplacement_libre(self.objet_selectionne.getPos_x(), self.objet_selectionne.getPos_y())
                
                if(objet.getNiveau()==2):
                    self.score+=50
                elif(objet.getNiveau()==3):
                    self.score+=100
                
                self.objet_selectionne = None
                return
                
        
        # Si on est ici, c'est qu'on n'a pas fusionné -> déselection
        self.objet_selectionne = None

    def update(self):
        """Met à jour l'état du jeu (logique de jeu)."""
        # Implémentation future: mise à jour des animations, timers, etc.
        pass

    def interrupt(self):
        """Efface l'écran en préparation au rendu de la frame suivante."""
        self.screen.fill(self.BLACK)

    def display(self):
        """Affiche tous les éléments du jeu à l'écran."""
        # Effacement de l'écran
        self.interrupt()
        
        # Affichage de l'arrière-plan
        self.screen.blit(self.arriere_plan, (0, 0))
        
        # Affichage des cadres vides
        self._afficher_cadres_null()
        
        # Affichage de tous les objets
        for objet in self.listeObjets:
            self.screen.blit(objet.apparence, objet.rect)
            self.screen.blit(objet.cadre, objet.rectCadre)
            
            # Marquage visuel de l'objet sélectionné
            if objet == self.objet_selectionne:
                pygame.draw.rect(self.screen, (255, 0, 0), objet.rect, 2)
        
        # Mise à jour de l'affichage
        self.show_score()
        pygame.display.flip()

    def _afficher_cadres_null(self):
        """Affiche les cadres vides pour les emplacements des objets."""
        # Extraction des informations de la grille
        x_init, y_init, distance, nb_ligne, nb_max = self.grid_info
        
        # Affichage des cadres vides pour chaque emplacement possible
        x, y = x_init, y_init
        for i in range(nb_max):
            self.screen.blit(self.cadre_null, (x, y))
            
            x += distance
            # Passage à la ligne suivante si nécessaire
            if (i + 1) % nb_ligne == 0:
                x = x_init
                y += distance
    def show_score(self):
        """Affiche le score en haut à droite de notre écran de jeu"""
        score_obj = pygame.font.SysFont('comicsans',50,True)
        score_txt = score_obj.render("Score : " + str(self.score), 1, (0,0,0))
        self.screen.blit(score_txt, (990,20))

    def run(self):
        """Démarre et gère la boucle principale du jeu."""
        while self.running:
            # Gestion des événements
            self.handling_events()
            
            # Mise à jour de la logique du jeu
            self.update()
            
            # Affichage du jeu
            self.display()
            
            #Pour afficher le score à chaque d'horloge dans la console
            #print("Score = ", self.score)

            # Régulation de la vitesse du jeu
            self.clock.tick(self.fps)
        
        print("Score Final = ", self.score)
        # Si on sort de la boucle, on nettoie avant de quitter
        print("Fin du jeu")
