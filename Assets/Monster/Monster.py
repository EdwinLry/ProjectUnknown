import pygame
import cmath

class Monsters(pygame.sprite.Sprite):
    def __init__(self, health, attack, defend,filepath):
        pygame.sprite.Sprite.__init__(self)
        self.health = health
        self.attack = attack
        self.defend = defend
        self.health = health
        self.maxHealth = health
        self.attack = attack
        self.defend = defend
        self.image = pygame.transform.scale(pygame.image.load('Assets\Player\player.png'), (480, 180))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (100, 600)



    def defend(self,damage):
        self.health-=damage

class Slime(Monsters):
    def update(self):
        pass