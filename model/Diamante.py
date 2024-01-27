import pygame

class Diamante(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        foto_diamante=pygame.image.load("assest/diamante.png")
        self.gorditura_diamante=80
        self.altura_diamante=120
        diamante=pygame.transform.scale(foto_diamante, (self.gorditura_diamante,self.altura_diamante))
        self.image=diamante
        self.body = diamante.get_rect()
        self.body.x = x
        self.body.y = y

