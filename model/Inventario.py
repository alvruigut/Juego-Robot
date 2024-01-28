import pygame

class Inventario(pygame.sprite.Sprite):
    def __init__(self,x,y,objetos):
        super().__init__()
        foto_inventario=pygame.image.load("assest/mochila.png")
        self.gorditura_inventario=80
        self.altura_inventario=50
        inventario=pygame.transform.scale(foto_inventario, (self.gorditura_inventario,self.altura_inventario))
        self.image=inventario
        self.objetos=objetos
        self.body = inventario.get_rect()
        self.body.x = x
        self.body.y = y



  
