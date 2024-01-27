import pygame
from pygame.locals import QUIT, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_y,K_n,K_q,K_i
import random
from model.Steven import *
from model.Lava import *
from model.Manzana import *
from model.Diamante import *
from model.Agua import *
from model.Perla import *
from model.Tnt import *
from util.Mensaje import *
from model.Inventario import *
#Volumen
foto_volumen = pygame.image.load("assest/volumen.png")
volumen=pygame.transform.scale(foto_volumen, (50,50))
#0 posicion inicial,1 back,2 left,3 right
sprite_steven=[pygame.image.load("assest/steve_front.png"),pygame.image.load("assest/steve_back.png"),pygame.image.load("assest/steve_left.png"),pygame.image.load("assest/steve_right.png")]
sprite_enderman=[pygame.image.load("assest/enderman_front.png"),pygame.image.load("assest/enderman_back.png"),pygame.image.load("assest/enderman_x.png")]
#Ventana
tam_x_ventana = 1900
tam_y_ventana = 980
ventana = pygame.display.set_mode((tam_x_ventana, tam_y_ventana))
foto_fondo = pygame.image.load("assest/fondo.jpg")
fondo=pygame.transform.scale(foto_fondo, (tam_x_ventana,tam_y_ventana))
#Steven
steven=Steve(0,0)
posicion_x_steven = random.randint(600, tam_x_ventana-steven.body.width)
posicion_y_steven= random.randint(0, tam_y_ventana-steven.body.height)
steven.body.x = posicion_x_steven
steven.body.y = posicion_y_steven
#Agua
agua=Agua(540,327)
#Lava
lavas=[]
lava=Lava(0,0)
for x in range(6):
    for y in range(2):
        lava=Lava(x*lava.body.width,y*(lava.body.height+steven.body.height+10)+tam_y_ventana/3) 
        lavas.append(lava)  

#ManzanaOro
manzanas_oro=[]
manzana_oro=ManzanaDorada(0,tam_y_ventana/2-lava.body.height/2-5)
manzanas_oro.append(manzana_oro)
#Manzana
manzanas=[]
manzana=Manzana(0,900)
manzana2=Manzana(0,700)
manzanas.append(manzana)
manzanas.append(manzana2)

#Diamantes
diamantes=[]
diamante=Diamante(700,700)
diamantes.append(diamante)
#Perla
perlas=[]
perla=Perla(0,60)
perlas.append(perla)
#TNT
tnts=[]
tnt=Tnt(900,30)
tnts.append(tnt)




pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("assest/minecraft.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

game_running=True
muted = False
while game_running:


    fuente = pygame.font.Font(None, 36)  
    vida_texto = fuente.render(f'Vida: {steven.vida}', True, (0, 0, 0))
    diamantes_texto = fuente.render(f'Diamantes: {steven.diamantes}', True, (0, 0, 0))
    inventario_texto = fuente.render(f'Inventario: {steven.inventario.objetos}', True, (0, 0, 0))

    ventana.blit(fondo, (0, 0))
    ventana.blit(volumen, (tam_x_ventana-50, 0))

    for manzana_oro in manzanas_oro:
        steven.comer_manzana_dorada(manzana_oro,manzanas_oro)
        ventana.blit(manzana_oro.image, manzana_oro.body)
    for manzana in manzanas:
        steven.comer_manzana(manzana,manzanas)
        ventana.blit(manzana.image, manzana.body)
        

    ventana.blit(vida_texto, (10, 10))
    ventana.blit(inventario_texto, (900, 10))
    for tnt in tnts:
        ventana.blit(tnt.image, tnt.body)
        steven.coger_tnt(tnt,tnts)

    for diamante in diamantes:
        ventana.blit(diamante.image, diamante.body)
        steven.coger_diamante(diamante,diamantes)
    for perla in perlas:
        ventana.blit(perla.image, perla.body)
        steven.convertir_enderman(perla,perlas)
    steven.cambiar_enderman()

    for lava in lavas:
        ventana.blit(lava.image, lava.body)
        steven.collision_lava(lava.body)
    ventana.blit(agua.image, agua.body)
    ventana.blit(steven.image, steven.body)

    buttom_pressed = pygame.key.get_pressed()
    if buttom_pressed[K_LEFT]:
        if steven.enderman==False:
            steven.move(-steven.velocidad,0,tam_x_ventana,tam_y_ventana,agua.body)  # mover a la izquierda
            steven.image=pygame.transform.scale(sprite_steven[2], (steven.gorditura_steven-14, steven.altura_steven-3))
        else:
            steven.move(-steven.velocidad,0,tam_x_ventana,tam_y_ventana,agua.body)  # mover a la izquierda
            steven.image=pygame.transform.scale(sprite_enderman[2], (steven.gorditura_steven-14, steven.altura_steven-3))
    if buttom_pressed[K_RIGHT]:
        if steven.enderman==False:
            steven.move(steven.velocidad, 0,tam_x_ventana,tam_y_ventana, agua.body)  # mover a la derecha
            steven.image=pygame.transform.scale(sprite_steven[3], (steven.gorditura_steven-10, steven.altura_steven-5))
        else:            
            steven.move(steven.velocidad, 0,tam_x_ventana,tam_y_ventana, agua.body)  # mover a la derecha
            steven.image=pygame.transform.scale(sprite_enderman[2], (steven.gorditura_steven-10, steven.altura_steven-5))

    if buttom_pressed[K_UP]:
        if steven.enderman==False:
            steven.move(0, -steven.velocidad,tam_x_ventana,tam_y_ventana,agua.body)  # mover hacia arriba
            steven.image=pygame.transform.scale(sprite_steven[1], (steven.gorditura_steven, steven.altura_steven))
        else:
            steven.move(0, -steven.velocidad,tam_x_ventana,tam_y_ventana,agua.body)  # mover hacia arriba
            steven.image=pygame.transform.scale(sprite_enderman[1], (steven.gorditura_steven, steven.altura_steven))
    if buttom_pressed[K_DOWN]:
        if steven.enderman==False:
            steven.move(0, steven.velocidad,tam_x_ventana,tam_y_ventana,agua.body)  # mover hacia abajo
            steven.image=pygame.transform.scale(sprite_steven[0], (steven.gorditura_steven, steven.altura_steven))
        else:
            steven.move(0, steven.velocidad,tam_x_ventana,tam_y_ventana,agua.body)  # mover hacia abajo
            steven.image=pygame.transform.scale(sprite_enderman[0], (steven.gorditura_steven, steven.altura_steven))



  
    

                
   

            
   

    for event in pygame.event.get():
        if event.type == QUIT :
            game_running = False
        

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                mouse_x, mouse_y = event.pos
                if tam_x_ventana - 50 <= mouse_x <= tam_x_ventana and 0 <= mouse_y <= 50:
                    muted = not muted
                    if muted:
                        pygame.mixer.music.set_volume(0)
                        foto_volumen = pygame.image.load("assest/volumenoff.png")
                        volumen=pygame.transform.scale(foto_volumen, (50,50))
                    else:
                        foto_volumen = pygame.image.load("assest/volumen.png")
                        volumen=pygame.transform.scale(foto_volumen, (50,50))
                        pygame.mixer.music.set_volume(0.5)
    if steven.vida <= 0:
        game_running = False
    pygame.display.flip()

pygame.quit()