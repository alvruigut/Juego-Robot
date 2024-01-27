import pygame
from pygame.locals import *

# Definir la clase para la ventana emergente
class Mensaje():
    def __init__(self, message,tam_x_ventana,tam_y_ventana):
        self.message = message
        
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render(self.message, 1, (10, 10, 10))
        self.rect = self.text.get_rect(center=(tam_x_ventana/2, tam_y_ventana/2))

    def mostrar_mensaje(self, ventana):
        ventana.blit(self.text, self.rect)
