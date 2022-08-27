import pygame

class Attack(pygame.sprite.Sprite):
    def __init__(self,damage,range,filepath,width,height,speed,dir,pos):
        pygame.sprite.Sprite.__init__(self)
        self.damage=damage
        self.range=range
        self.image = pygame.transform.scale(pygame.image.load(filepath), (width, height))
        self.rect=self.image.get_rect()
        self.rect.center=pos
        self.speed=speed
        self.dir=dir

class Normal(Attack):
    def update(self):
        self.rect.x+=(self.speed*self.dir)
        self.range-=self.speed