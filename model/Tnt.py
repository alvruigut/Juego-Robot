import pygame

class Tnt(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        foto_tnt=pygame.image.load("assest/tnt.png")
        self.gorditura_tnt=40
        self.altura_tnt=40
        tnt=pygame.transform.scale(foto_tnt, (self.gorditura_tnt,self.altura_tnt))
        self.image=tnt
        self.body = tnt.get_rect()
        self.body.x = x
        self.body.y = y

