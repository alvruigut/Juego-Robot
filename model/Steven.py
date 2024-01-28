import pygame
import time
from pygame.locals import K_t, K_p,K_m,K_d,K_b
from model.Inventario import *
from model.Tnt import *
import sys
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
        self.perla=0
        self.tnt=0
        self.manzanas=0
        self.manzanas_doradas=0
        self.inventario=Inventario(0,0,{})
   

    def move(self, dx, dy,ventana_horizontal,ventana_vertical,muros,lava,agua):
        x = self.body.x
        y = self.body.y
        if 0 <= self.body.x + dx < ventana_horizontal - self.body.width:
            self.body.x += dx
        if 0 <= self.body.y + dy< ventana_vertical - self.body.height:
            self.body.y += dy
        for componente in muros:
            if self.collision_muro(componente.body):
                self.body.x = x
                self.body.y = y
        for componente in lava:
            if self.collision_lava(componente.body):
                self.body.x = x
                self.body.y = y
                self.vida -= 1
                time.sleep(0.2)
        for componente in agua:
            if self.collision_agua(componente.body):
                self.body.x = x
                self.body.y = y
                self.vida -= 1
                time.sleep(0.2)

    
    def collision_muro(self, muro):
        return self.body.colliderect(muro) 

    def collision_lava(self,lava):
        return self.body.colliderect(lava)

  
    def collision_agua(self,agua):
        if self.enderman==False:
            return self.body.colliderect(agua)
        else:
            return False        
        

    def convertir_enderman(self,perla,perlas):
        tecla = pygame.key.get_pressed()
        if  tecla[K_t] and self.body.colliderect(perla.body) and self.enderman==False:
            self.perla=1
            self.enderman=True
            self.vida+=5
            self.inventario.objetos['Perla']=self.perla
            foto_enderman=pygame.image.load("assest/enderman_front.png")
            enderman=pygame.transform.scale(foto_enderman, (self.gorditura_steven,self.altura_steven))
            self.image=enderman
            perlas.remove(perla)
            time.sleep(0.4)

    def cambiar_enderman(self):
        tecla = pygame.key.get_pressed()
        if tecla[K_p] and self.perla==1 and self.enderman==True:
            self.enderman=False
            foto_steven=pygame.image.load("assest/steve_front.png")
            steve=pygame.transform.scale(foto_steven, (self.gorditura_steven,self.altura_steven))
            self.image=steve
            time.sleep(0.4)
        elif tecla[K_p] and self.perla==1 and self.enderman==False:
            self.enderman=True
            foto_enderman=pygame.image.load("assest/enderman_front.png")
            enderman=pygame.transform.scale(foto_enderman, (self.gorditura_steven,self.altura_steven))
            self.image=enderman
            time.sleep(0.4)

    def comer_manzana_dorada(self,manzana,manzanas):
        tecla = pygame.key.get_pressed()
        if tecla[K_t] and self.body.colliderect(manzana.body):
            if self.enderman==False and self.vida<10: 
                self.vida = 10
                manzanas.remove(manzana)
            elif self.enderman==True and self.vida<15:
                self.vida = 15
                manzanas.remove(manzana)
            else:
                self.manzanas_doradas += 1
                self.inventario.objetos['Manzanas Doradas']=self.manzanas_doradas
                manzanas.remove(manzana)
    
    def comer_manzana_dorada_inventario(self):
        tecla = pygame.key.get_pressed()
        if tecla[K_d] and self.vida<10 and self.enderman==False and self.manzanas_doradas>0:
            self.manzanas_doradas -= 1
            self.vida = 10
            self.inventario.objetos['Manzanas Doradas']=self.manzanas_doradas
            time.sleep(0.3)
            if self.manzanas_doradas==0:
                self.inventario.objetos.pop('Manzanas Doradas')
        elif tecla[K_d] and self.vida<15 and self.enderman==True and self.manzanas_doradas>0:
            self.manzanas_doradas -= 1
            self.vida = 15
            self.inventario.objetos['Manzanas Doradas']=self.manzanas_doradas
            time.sleep(0.3)
            if self.manzanas_doradas==0:
                self.inventario.objetos.pop('Manzanas Doradas')

    def comer_manzana(self,manzana,manzanas):
        tecla = pygame.key.get_pressed()
        if tecla[K_t] and self.body.colliderect(manzana.body):
            if self.vida<10 and self.enderman==False:
                manzanas.remove(manzana)
                self.vida += 1
            elif self.vida<15 and self.enderman==True:
                manzanas.remove(manzana)
                self.vida += 1
            else:
                manzanas.remove(manzana)
                self.manzanas += 1
                self.inventario.objetos['Manzanas']= self.manzanas               
    def comer_manzana_inventario(self):
        tecla = pygame.key.get_pressed()
        if tecla[K_m] and self.vida<10 and self.enderman==False and self.manzanas>0:
            self.manzanas -= 1
            self.vida += 1
            self.inventario.objetos['Manzanas']= self.manzanas               
            time.sleep(0.3)
            if self.manzanas==0:
                self.inventario.objetos.pop('Manzanas')
        elif tecla[K_m] and self.vida<15 and self.enderman==True and self.manzanas>0:
            self.manzanas -= 1
            self.inventario.objetos['Manzanas']= self.manzanas               
            self.vida += 1
            time.sleep(0.3)
            if self.manzanas==0:
                self.inventario.objetos.pop('Manzanas')
        




    def coger_tnt(self,tnt,tnts):
        tecla = pygame.key.get_pressed()
        if tecla[K_t] and self.body.colliderect(tnt.body):
            self.tnt += 1
            tnts.remove(tnt)
            self.inventario.objetos['TNT']=self.tnt
            time.sleep(0.3)




    def poner_tnt(self,tnts,muros,n):
        tecla = pygame.key.get_pressed()
        if tecla[K_b] and self.tnt>0:
            self.tnt -= 1
            self.inventario.objetos['TNT']=self.tnt
            tnt=Tnt(self.body.x,self.body.y)
            tnts.append(tnt)
            muros_explotados=[]
            tnts_activados=[]
            for tnt_otro in tnts:
                if tnt_otro != tnt:
                    dx = abs(tnt.body.x - tnt_otro.body.x)
                    dy = abs(tnt.body.y - tnt_otro.body.y)
                    if dx < tnt.body.width*n and dy < tnt.body.height*n:
                        tnts_activados.append(tnt_otro)
            if tnts_activados==[]:            
                for muro in muros:
                    dx = abs(tnt.body.x - muro.body.x)
                    dy = abs(tnt.body.y - muro.body.y)
                    if dx < tnt.body.width*n and dy < tnt.body.height*n:
                        muros_explotados.append(muro)
                        self.inventario.objetos['TNT']=self.tnt
                        if tnt in tnts:
                            tnts.remove(tnt)
                    else:
                        self.inventario.objetos['TNT']=self.tnt
                        if tnt in tnts:
                            tnts.remove(tnt)
            else:
                for tnt_activo in tnts_activados:
                    for muro in muros:
                        dx = abs(tnt_activo.body.x - muro.body.x)
                        dy = abs(tnt_activo.body.y - muro.body.y)
                        if dx < tnt_activo.body.width*n and dy < tnt_activo.body.height*n:
                            muros_explotados.append(muro)
                            if tnt_activo in tnts:
                                tnts.remove(tnt_activo)
                            if tnt in tnts:
                                tnts.remove(tnt)
                        else:
                            self.inventario.objetos['TNT']=self.tnt
                            if tnt in tnts:
                                tnts.remove(tnt)
                            if tnt_activo in tnts:
                                tnts.remove(tnt_activo)            
            for muro in muros_explotados:
                muros.remove(muro)
            if self.tnt==0:
                self.inventario.objetos.pop('TNT')
                

    def coger_diamante(self,diamante,diamantes):
        tecla = pygame.key.get_pressed()
        if tecla[K_t] and self.body.colliderect(diamante.body):
            self.diamantes += 1
            self.inventario.objetos['Diamante']=self.diamantes
            diamantes.remove(diamante)  
            time.sleep(0.3)

    