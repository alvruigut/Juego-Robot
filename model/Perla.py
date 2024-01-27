import pygame

class Perla(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        foto_perla=pygame.image.load("assest/enderman.png")
        self.gorditura_perla=50
        self.altura_perla=50
        perla=pygame.transform.scale(foto_perla, (self.gorditura_perla,self.altura_perla))
        self.image=perla
        self.body = perla.get_rect()
        self.body.x = x
        self.body.y = y

