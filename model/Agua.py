import pygame


class Agua(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        foto_agua=pygame.image.load("assest/agua.jpg")
        self.gorditura_agua=90
        self.altura_agua=260
        agua=pygame.transform.scale(foto_agua, (self.gorditura_agua,self.altura_agua))
        self.image=agua
        self.body = agua.get_rect()
        self.body.x = x
        self.body.y = y

