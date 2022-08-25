import pygame
from Assets.Player.Scripts.Player import Player

player = Player(10, 5, 5, 6, 1)


def main():
    pygame.init()
    screen=pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Untitled")
    background=pygame.image.load("bg.png").convert()
    background=pygame.transform.scale(background,(1280,720))
    running = True
    framerate=pygame.time.Clock()
    while running:
        framerate.tick(30)
        screen.blit(background,(0,0))
        running = CheckEvents()
        player.Update()
        screen.blit(player.image,player.rect)
        pygame.display.update()


def CheckEvents():
    quit = True
    # input detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
    return quit


if __name__ == '__main__':
    main()
