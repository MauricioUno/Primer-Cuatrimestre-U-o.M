from constantes import *
from auxiliar import Auxiliar
import pygame

class Jugador:
    def __init__(self,x,y,speed_walk) -> None:

        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "\caracters\stink\idle.png",16,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "\caracters\stink\idle.png",16,1,True)
        
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "\caracters\stink\walk.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "\caracters\stink\walk.png",15,1,True)[:12]

        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "\caracters\stink\jump.png", 33, 1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "\caracters\stink\jump.png", 33, 1, True)
        
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk

        self.direccion = "derecha"
        self.animacion = self.stay_r
        self.animacion_anterior = self.stay_r

        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.saltando = False
        self.cayendo = False
        self.speed_jump = 10
        self.inicio_salto = y


    def mover(self,direccion):
        self.direccion = direccion
        if self.direccion == "derecha":
            self.move_x = self.speed_walk
            
        elif self.direccion == "izquierda":
            self.move_x = -self.speed_walk
            

    def detener(self):
        self.move_x = 0


    def saltar(self, saltar):

        if self.rect.y < self.inicio_salto - 150:
            saltar = False

        if saltar: 
            if self.rect.y == 400:
                self.move_y = -self.speed_jump
                self.saltando = True
                self.frame = 0
                self.inicio_salto = self.rect.y
        else:
            self.saltando = False
            self.caer(True)


    def controlar_movimiento_y(self):

        if not self.rect.y < 400 and not self.saltando:
            #self.rect.y = 400
            self.caer(False)


    def caer(self, cayendo):
        if cayendo:
            self.move_y = self.speed_jump
            self.cayendo = True
        else:
            self.move_y = 0
            self.cayendo = False

    def animaciones(self):
        
        if not self.saltando and not self.cayendo:
            if self.move_x == 0:
                if self.direccion == "derecha":
                    self.animacion = self.stay_r
                elif self.direccion == "izquierda":
                    self.animacion = self.stay_l

            else:
                if self.move_x == self.speed_walk:
                    self.animacion = self.walk_r

                elif self.move_x == -self.speed_walk:
                    self.animacion = self.walk_l                

            if self.animacion != self.animacion_anterior:
                self.animacion_anterior = self.animacion
                self.frame = 0

        elif self.saltando or self.cayendo:
            if self.direccion == "derecha":
                self.animacion = self.jump_r
            elif self.direccion == "izquierda":
                self.animacion = self.jump_l


    def actualizar_posicion(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y


    def update(self):
        if(self.frame < len(self.animacion) - 1):
            self.frame += 1 
        else: 
            self.frame = 0
    

    def draw(self,screen):
        #pygame.draw.rect(screen,(0,0,0),self.rect)
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen,self.rect)


    def actualizar_player(self, screen):
        self.animaciones()
        self.update()
        self.actualizar_posicion()
        self.controlar_movimiento_y()
        self.draw(screen)
        


