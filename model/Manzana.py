import pygame

class Manzana(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        foto_manzana=pygame.image.load("assest/manzana.png")
        self.gorditura_manzana=70
        self.altura_manzana=50
        manzana=pygame.transform.scale(foto_manzana, (self.gorditura_manzana,self.altura_manzana))
        self.image=manzana
        self.body = manzana.get_rect()
        self.body.x = x
        self.body.y = y

class ManzanaDorada(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        foto_manzana=pygame.image.load("assest/manzana_oro.png")
        self.gorditura_manzana=40
        self.altura_manzana=40
        manzana=pygame.transform.scale(foto_manzana, (self.gorditura_manzana,self.altura_manzana))
        self.image=manzana
        self.body = manzana.get_rect()
        self.body.x = x
        self.body.y = y