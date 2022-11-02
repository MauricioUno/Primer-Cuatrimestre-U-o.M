from constantes import *
from auxiliar import Auxiliar
import pygame

class Proyectil:
    def __init__(self, x, y, velocidad):
        self.proyectil = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"\inhabitants\coco_fantasma\proyectil.png",10,2)
        self.animacion = self.proyectil
        self.frame = 0

        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_pos = pygame.Rect(x+35,y+10, 20, 20)

        self.move_x = -velocidad
        self.move_y = 0
        self.activo = True
    

    def verificar_fin(self, rect_jugador):
        if self.rect_pos.colliderect(rect_jugador) or self.verificar_limite_x():
            self.activo = False


    def verificar_limite_x(self):
        limite_alcanzado = False
        if self.rect.x < -40:
            limite_alcanzado = True
            
        return limite_alcanzado


    def actualizar_posicion(self):
        self.rect.x += self.move_x
        self.rect_pos.x += self.move_x
        self.rect.y += self.move_y
        self.rect_pos.y += self.move_y


    def update(self):
        if(self.frame < len(self.animacion) - 1):
            self.frame += 1 
        else: 
            self.frame = 0


    def draw(self,screen):
        #pygame.draw.rect(screen,(0,0,0),self.rect_pos)
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen,self.rect)

    def actualizar_proyectil(self, screen, rect_jugador):
        self.update()
        self.actualizar_posicion()
        self.verificar_fin(rect_jugador)
        self.draw(screen)
        


class CocoFantasma:

    def __init__(self, x, y):
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"\inhabitants\coco_fantasma\stay.png",10,4)[:3]
        self.attack_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"\inhabitants\coco_fantasma\attack.png",9,2)[:17]
        self.frame = 0
        self.animacion = self.stay_l
        self.animacion_anterior = self.stay_l
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_pos = pygame.Rect(x+17,y+20, 85, 100)
        self.rect_vision = pygame.Rect(x-350,y-20, 380, 120)
        self.proyectiles = []
        self.atacando = False

    def disparar(self, rect_jugador):
        if self.rect_vision.colliderect(rect_jugador):
            self.atacando = True
            proyectil = Proyectil(self.rect.x + 25, self.rect.y + 35, 10)
            self.proyectiles.append(proyectil)
        else:
            self.atacando = False


    def animaciones(self):
        
        if not self.atacando:
            self.animacion = self.stay_l
        else:
            self.animacion = self.attack_l

        if self.animacion != self.animacion_anterior:
            self.animacion_anterior = self.animacion
            self.frame = 0


    def update(self):
        if(self.frame < len(self.animacion) - 1):
            self.frame += 1 
        else: 
            self.frame = 0


    def draw(self,screen):
        #pygame.draw.rect(screen,(0,0,0),self.rect_vision)
        #pygame.draw.rect(screen,(0,0,0),self.rect_pos)
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen,self.rect)
    

    def actualizar_proyectiles(self, screen, rect_jugador):
        for proyectil in self.proyectiles:
            proyectil.actualizar_proyectil(screen, rect_jugador)
            if not proyectil.activo:
                self.proyectiles.remove(proyectil)


    def actualizar_coco_fantasma(self, screen, rect_jugador):
        self.animaciones()
        self.update()
        self.draw(screen)
        self.actualizar_proyectiles(screen, rect_jugador)
