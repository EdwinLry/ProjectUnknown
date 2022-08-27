import pygame
import Animation
from Assets.Attack import Normal


class Player:
    level = 1
    exp = 0
    god = False
    maxHealth = 0
    inventory = list()
    group=pygame.sprite.Group()
    facing = True
    transform = None

    def __init__(self, health, attack, defend):
        self.health = health
        self.maxHealth = health
        self.attack = attack
        self.defend=defend
        self.image = pygame.transform.scale(pygame.image.load('Assets\Player\player.png'), (180, 180))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (100, 600)
        self.vel_y = 0
        self.jumped = False
        self.still = Animation.importFrames("Assets\Player\BlueWizard\\2BlueWizardIdle\\", 180, 180, 19)
        self.last_time=0

    def update(self,screen):
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
        if key[pygame.K_f]:
            self.Attack(screen)


        self.vel_y += 5  # falling speed
        if self.vel_y > 10:  # maximum falling speed
            self.vel_y = 10
        y_move += self.vel_y
        self.rect.x += x_move
        self.rect.y += y_move
        if self.rect.bottom > 600:
            self.jumped = False
            self.rect.bottom = 600
        self.still.update(pygame.time.get_ticks())
        self.image = self.still.image
        self.group.update()
        self.group.draw(screen)
        if not self.facing:
            self.image = pygame.transform.flip(self.image, True, False)

    def Attack(self, screen):
        current_time=pygame.time.get_ticks()
        if current_time < self.last_time + 100:
            return
        self.last_time=current_time
        if(self.facing):
            bullet=Normal(self.attack,1000,'bullet1.png',50,50,20,1,self.rect.center)
        else:
            bullet = Normal(self.attack, 1000, 'bullet1.png', 50, 50, 20,-1, self.rect.center)
        self.group.add(bullet)



    def Defend(self):
        # put animation here

        pass


    def AddInventory(self, equipment):
        self.inventory.append(equipment)

    def Equipt(self, weapon):
        self.attack += weapon.attack
        self.defend += weapon.defend

    def Levelup(self):
        if self.exp == self.level * self.level * 10:
            self.level += 1
            self.maxHealth += 10
            self.health = self.maxHealth

    def GodMode(self):
        self.health = 1000000000
        self.maxHealth = self.health
