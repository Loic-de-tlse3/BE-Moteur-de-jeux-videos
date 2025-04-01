import pygame
from arme import Arme
import random

bouton = "Projet BE images/Bouton.png"
Melee1 = "Projet BE images/knife.png"
Melee2 = "Projet BE images/sword.png"
Melee3 = "Projet BE images/spears.png"
Distance1 = "Projet BE images/gun.png"
Distance2 = "Projet BE images/rifle.png"
Distance3 = "Projet BE images/space-gun.png"

ListeArmes = [Melee1, Melee2, Melee3, Distance1, Distance2, Distance3]
ListeArmesBasique = [Melee1, Distance1]

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.arme = Arme(150,200,random.choice(ListeArmesBasique))
        self.arme1 = Arme(150*3,200,random.choice(ListeArmesBasique))

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.arme.move()

    def update(self):
        pass
        #if self.arme.colliderect(self.arme1.rect):
        #    if self.arme.image == self.arme1.image:
        #        if self.arme.image == pygame.image.load(Melee1):
        #            self.arme.image = pygame.image.load(Melee2)
        #        else:
        #            self.arme.image = pygame.image.load(Distance2)


    def display(self):
        screen.blit(arriere_plan,(0,0))
        self.arme.draw(self.screen)
        self.arme1.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)


pygame.init()
screen =  pygame.display.set_mode((1224, 750)) #Initialisation de la taille de la fenêtre (X px * Y px)
arriere_plan = pygame.image.load("Cadre.png").convert()
game = Game(screen)
game.run()

pygame.quit()