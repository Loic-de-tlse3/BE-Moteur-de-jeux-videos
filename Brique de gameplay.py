import pygame
from objets import *
from generateur import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.listeObjets = []
        self.generateur = Generateur()
        self.listeObjets.append(self.generateur)

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for objet in self.listeObjets:
                        if objet.rect.collidepoint(event.pos) and isinstance(objet, Generateur):
                            print("création objet")
                            self.generateur.creation_objet(self.listeObjets)

    def update(self):
        pass
        #if self.arme.colliderect(self.arme1.rect):
        #    if self.arme.image == self.arme1.image:
        #        if self.arme.image == pygame.image.load(Melee1):
        #            self.arme.image = pygame.image.load(Melee2)
        #        else:
        #            self.arme.image = pygame.image.load(Distance2)


    def display(self):
        self.screen.blit(arriere_plan, (0, 0))
        self.ajout_cadre_null()
        for objet in self.listeObjets:
            self.screen.blit(objet.apparence, objet.rect)
            self.screen.blit(objet.cadre, objet.rectCadre)
        pygame.display.flip()

    def ajout_cadre_null(self):
        x = X_INITIAL_CADRE
        y = Y_INITIAL_CADRE
        for i in range(NB_ITEM_MAX):
            self.screen.blit(cadre_null, (x, y))
            x += DISTANCE_OBJET
            if (i+1) % NB_ITEM_LIGNE == 0:
                x = X_INITIAL_CADRE
                y = y + DISTANCE_OBJET

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)


pygame.init()
screen =  pygame.display.set_mode((1224, 750)) #Initialisation de la taille de la fenêtre (X px * Y px)
arriere_plan = pygame.image.load('../Projet BE images/Cadre.png').convert()
cadre_null = pygame.image.load('../Projet BE images/Cadre null.png').convert_alpha()
game = Game(screen)
game.run()

pygame.quit()