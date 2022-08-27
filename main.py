import pygame
from Assets.Player.Scripts.Player import Player
from Assets.Monster.Monster import Slime
from Assets.Monster.Monster import Monsters


player = Player(10, 5, 5)
monsters = pygame.sprite.Group()

def main():
    monster = Slime(30, 5, 5, '')
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Untitled")
    background = pygame.image.load("bg.png").convert()
    background = pygame.transform.scale(background, (1280, 720))
    running = True
    framerate = pygame.time.Clock()
    monsters.add(monster)
    while running:
        framerate.tick(30)
        screen.blit(background, (0, 0))
        running = CheckEvents()
        player.update(screen)
        monsters.draw(screen)
        screen.blit(player.image, player.rect)
        pygame.display.update()
        collision()


def CheckEvents():
    quit = True
    # input detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
    return quit

def collision():
    dict=pygame.sprite.groupcollide(monsters,player.group,False,True)

if __name__ == '__main__':
    main()
