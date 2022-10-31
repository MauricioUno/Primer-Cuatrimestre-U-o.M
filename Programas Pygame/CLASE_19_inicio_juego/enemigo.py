from constantes import *
from auxiliar import Auxiliar
import random
import pygame

class Batterfly:
    def __init__(self, x, y, speed_x, speed_y, invertido, maximo_x, maximo_y) -> None:

        self.fly= Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"\inhabitants\batterfly\fly.png",8,5, invertido)
        self.frame = 0
        self.move_x = speed_x
        self.move_y = speed_y
        self.animation = self.fly

        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_pos = pygame.Rect(x+20,y+10, 75, 70)
        self.down = False

        self.maximo_x = maximo_x
        self.maximo_y = y - maximo_y
        self.minimo_y = y



    def update(self):
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0

        self.rect.x += self.move_x
        self.rect_pos.x += self.move_x
        self.controlar_vuelo()
    
    def controlar_vuelo(self):
        if self.rect.y < self.minimo_y and self.down == True:
            self.rect.y += self.move_y
            self.rect_pos.y += self.move_y
        
        else:
            self.down = False
            if self.rect.y > self.maximo_y:
                self.rect.y -= self.move_y
                self.rect_pos.y -= self.move_y
            else:
                self.down = True

    def draw(self,screen):
        #pygame.draw.rect(screen,(0,0,0),self.rect_pos)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)


class GrupoBatterflies:
    def __init__(self, cantidad) -> None:
        self.lista_murcielagos = []
        self.agregar_murcielagos(cantidad)
        self.cantidad = cantidad
        
    def agregar_murcielagos(self, cantidad):
        for i in range(cantidad):
            invertido = random.randrange(0,2)
            y = random.randrange(200, 480, 20)
            movimiento_x = random.randrange(5, 10)
            movimiento_y = random.randrange(5, 10)
            maximo_y = random.randrange(100,200,10)
            if invertido == 1:
                invertido = False
                x = random.randrange(-ANCHO_VENTANA/2, 0, 20)
                limite_x = ANCHO_VENTANA + 100
            else:
                invertido = True
                movimiento_x *= -1
                x = random.randrange(ANCHO_VENTANA, ANCHO_VENTANA + ANCHO_VENTANA/2, 20)
                limite_x = -100
            
            batterfly = Batterfly(x, y , movimiento_x, movimiento_y, invertido, limite_x, maximo_y)
            self.lista_murcielagos.append(batterfly)

    def updatear_murcielagos(self,screen, rect_player):

        if len(self.lista_murcielagos) < self.cantidad:
            self.agregar_murcielagos(1)

        for murcielago in self.lista_murcielagos:
            murcielago.update()
            murcielago.draw(screen)
            
            if murcielago.rect_pos.colliderect(rect_player):
                self.lista_murcielagos.remove(murcielago)

            if murcielago.move_x > 0:
                if murcielago.rect.x > murcielago.maximo_x:
                    self.lista_murcielagos.remove(murcielago)

            elif murcielago.rect.x < murcielago.maximo_x:
                self.lista_murcielagos.remove(murcielago)
            




