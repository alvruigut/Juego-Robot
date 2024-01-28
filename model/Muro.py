import pygame


class Muro(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        foto_muro=pygame.image.load("assest/muro.jpg")
        self.gorditura_muro=50
        self.altura_muro=50
        muro=pygame.transform.scale(foto_muro, (self.gorditura_muro,self.altura_muro))
        self.image=muro
        self.body = muro.get_rect()
        self.body.x = x
        self.body.y = y

