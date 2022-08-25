import pygame
import Animation

class Player:
    level = 1
    exp = 0
    god = False
    maxHealth = 0
    inventory = list()
    magic = list()
    facing = True
    transform = None

    def __init__(self, health, attack, phyDef, magDef, intelligence):
        self.health = health
        self.maxHealth = health
        self.attack = attack
        self.phyDef = phyDef
        self.magDef = magDef
        self.intelligence = intelligence
        self.image = pygame.transform.scale(pygame.image.load('Assets\Player\player.png'), (180, 180))
        self.rect = self.image.get_rect()
        print(self.rect.height)
        self.rect.midbottom = (100, 600)
        self.vel_y = 0
        self.jumped = False
        self.still = Animation.importFrames("Assets\Player\BlueWizard\\2BlueWizardIdle\\",180,180,19)



    def Update(self):
        x_move = 0
        y_move = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped is False:
            self.vel_y = -40
            self.jumped = True
        if key[pygame.K_a]:
            x_move -= 8
            if self.facing:
                self.facing = False
        if key[pygame.K_d]:
            x_move += 8
            if not self.facing:
                self.facing = True
        self.vel_y += 5             # falling speed
        if self.vel_y > 10:         # maximum falling speed
            self.vel_y = 10
        y_move += self.vel_y
        self.rect.x += x_move
        self.rect.y += y_move
        if self.rect.bottom > 600:
            self.jumped = False
            self.rect.bottom = 600
        self.still.update(pygame.time.get_ticks())
        self.image=self.still.image
        if not self.facing:
            self.image = pygame.transform.flip(self.image, True, False)

    def Attack(self, monsters):
        # put animation here

        for monster in monsters:
            pass

    def Magic(self):
        # put animation here

        pass

    def Defend(self):
        # put animation here

        pass

    def PhysicsDefend(self, damage):
        self.health -= (damage - self.phyDef)
        Player.Defend(self)

    def MagicDefend(self, damage):
        self.health -= (damage - self.magDef)
        Player.Defend(self)

    def AddInventory(self, equipment):
        self.inventory.append(equipment)

    def Equipt(self, weapon):
        self.attack += weapon.attack
        self.intelligence += weapon.inteligence
        self.magDef += weapon.magDef
        self.phyDef += weapon.phyDef

    def Levelup(self):
        if self.exp == self.level * self.level * 10:
            self.level += 1
            self.maxHealth += 10
            self.health = self.maxHealth

    def GodMode(self):
        self.health = 1000000000
        self.maxHealth = self.health

