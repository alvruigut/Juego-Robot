import pygame


class Lava(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        foto_lava=pygame.image.load("assest/lava.png")
        self.gorditura_lava=90
        self.altura_lava=90
        lava=pygame.transform.scale(foto_lava, (self.gorditura_lava,self.altura_lava))
        self.image=lava
        self.body = lava.get_rect()
        self.body.x = x
        self.body.y = y

