import pygame                   # PYGAME package
from pygame.locals import *     # PYGAME constant & functions
from sys import exit            # exit script 
from objets import Objet
from generateur import Generateur

class Game():
    """
    classe principale du jeux
    """

    def __init__(self, size_factor_X=9, size_factor_Y=5.5):
        """
        constructeur de la classe
        size_factor_X et size_factor_Y représentent la taille du plateau de jeux en nombre de tuiles 64*64 pixels
        """
    
        self.size_X, self.size_Y = 128,128                                     
        self.size_factor_X, self.size_factor_Y = size_factor_X, size_factor_Y # taille de la fenêtre en nombre de tuiles

        pygame.init()                                                         # initialisation Pygame
        self.screen = pygame.display.set_mode((self.size_X*self.size_factor_X, self.size_Y*self.size_factor_Y),0,32)
        pygame.display.set_caption("Test 1")                  # titre

        self.listeObjets = []
        self.generateur = Generateur()

    def loop(self):
        """
        boucle de lecture infinie événementielles du jeux
        """
        while True:
            #lecture des événements Pygame 
            for event in pygame.event.get():  
                if event.type == QUIT:  # evènement click sur fermeture de fenêtre
                    self.destroy()      # dans ce cas on appelle le destructeur de la classe 
                elif event.type == KEYUP:
                    if event.key == K_1:
                        print("Bouton 1 frappé")
                        if (self.listeObjets.__len__() < 28):
                            self.generateur.creation_objet(self.listeObjets)
                        else:
                            print("Le tableau est déjà plein")
                    elif event.key == K_2:
                        print("Bouton 2 frappé")
                        print("Il y a ", self.listeObjets.__len__(), " objets dans la liste")
                        print(self.listeObjets)    

            pos_x = 32
            pos_y = 32
            nb_item_ligne = 0

            self.screen.fill((100, 0, 100))
            for objet in self.listeObjets:
                self.screen.blit(objet.apparence, (pos_x, pos_y))
                pos_x += 160
                nb_item_ligne += 1
                if nb_item_ligne == 7:
                    pos_x = 32
                    pos_y += 160
                    nb_item_ligne = 0

            pygame.display.update()                  # rafraîchi l'écran


    def destroy(self):
        """
        destructeur de la classe
        """
        print('Bye!')
        pygame.quit() # ferme la fenêtre principale
        exit()        # termine tous les process en cours
            
if __name__ == '__main__':
    appl=Game()
    try:
        appl.loop()
    except KeyboardInterrupt:  # interruption clavier CTRL-C: appel à la méthode destroy() de appl.
        appl.destroy()