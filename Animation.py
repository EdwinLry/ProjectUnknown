import pygame


class MySprite(pygame.sprite.Sprite):
    def __init__(self,frames,animations):
        pygame.sprite.Sprite.__init__(self)
        self.first_frame = 0
        self.last_frame = frames
        self.last_time = 0
        self.frame=0
        self.animations=animations
        self.image=None


    def update(self, current_time, rate = 70): # current_time 更新频率 为30
        # update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame >= self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time
            self.image=self.animations[self.frame]



def importFrames(filepath,width,height,frames):
    group=list()
    for i in range(0,frames):
        image = pygame.transform.scale(pygame.image.load(filepath+str(i)+'.png'), (width, height))
        group.append(image)
    return MySprite(frames,group)