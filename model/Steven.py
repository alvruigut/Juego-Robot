import pygame
import time
from pygame.locals import K_t, K_p

class Steve(pygame.sprite.Sprite):

    def __init__(self, x,y):
        super().__init__()
        foto_steven=pygame.image.load("assest/steve_front.png")
        self.gorditura_steven=40
        self.altura_steven=70

        steve_initial=pygame.transform.scale(foto_steven, (self.gorditura_steven,self.altura_steven))
        self.image=steve_initial
        self.body = steve_initial.get_rect()
        
        self.vida=10
        self.diamantes=0
        self.velocidad=2
        self.body.x = x
        self.body.y = y
        self.enderman=False
        self.tnt=0
        self.estado_x = x
        self.estado_y = y

    def move(self, dx, dy,ventana_horizontal,ventana_vertical, agua):
        x = self.body.x
        y = self.body.y
        if 0 <= self.body.x + dx < ventana_horizontal - self.body.width:
            self.body.x += dx
        if 0 <= self.body.y + dy< ventana_vertical - self.body.height:
            self.body.y += dy
        if self.collision_agua(agua):
            self.body.x = x
            self.body.y = y
        if not 0 <= self.body.x < ventana_horizontal - self.body.width or not 0 <= self.body.y < ventana_vertical - self.body.height:
            self.vida -= 1
            time.sleep(0.3)

    def collision_lava(self,lava):
        if self.body.colliderect(lava):
            self.vida -= 1
            time.sleep(0.3)
    
    def collision_agua(self,agua):
        if self.enderman==False:
            return self.body.colliderect(agua)
        else:
            return False        
        
    def convertir_enderman(self,perla):
        
        tecla = pygame.key.get_pressed()
        if  tecla[K_t] and self.body.colliderect(perla) and self.enderman==False:
            self.enderman=True
            self.vida+=5
            foto_enderman=pygame.image.load("assest/enderman_front.png")
            enderman=pygame.transform.scale(foto_enderman, (self.gorditura_steven,self.altura_steven))
            self.image=enderman
            time.sleep(0.4)
        elif tecla[K_t] and self.body.colliderect(perla) and self.enderman==True:
            self.enderman=False
            foto_steven=pygame.image.load("assest/steve_front.png")
            steve=pygame.transform.scale(foto_steven, (self.gorditura_steven,self.altura_steven))
            self.image=steve
            time.sleep(0.4)
            
    def comer_manzana_dorada(self,manzana):
        tecla = pygame.key.get_pressed()
        if tecla[K_t] and self.body.colliderect(manzana):
            self.vida = 10

    def comer_manzana(self,manzana):
        tecla = pygame.key.get_pressed()
        if tecla[K_t] and self.body.colliderect(manzana):
            if self.vida<10:
                self.vida += 1
                time.sleep(0.3)

    def coger_tnt(self,tnt):
        tecla = pygame.key.get_pressed()
        if tecla[K_t] and self.body.colliderect(tnt):
            self.tnt += 1
            time.sleep(0.3)

    def coger_diamante(self,diamante):
        tecla = pygame.key.get_pressed()
        if tecla[K_t] and self.body.colliderect(diamante):
            self.diamantes += 1
            time.sleep(0.3)
