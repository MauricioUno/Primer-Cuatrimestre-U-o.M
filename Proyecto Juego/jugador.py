from aux_constantes import *
from aux_frames import Auxiliar
from class_padre import DisparoHorizontal
import pygame

class Jugador:
    def __init__(self,x,y,speed_walk) -> None:

        self.stay = {}
        self.stay[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\idle_plus.png",26,2)[:51]
        self.stay[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\idle_plus.png",26,2,True)[:51]
        
        self.walk = {}
        self.walk[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\walk.png",15,1)[:12]
        self.walk[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\walk.png",15,1,True)[:12]

        self.jump = {}
        self.jump[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1)[:23]
        self.jump[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1, True)[:23]

        self.fall = {}
        self.fall[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1)[22:28]
        self.fall[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1, True)[22:28]
        
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk

        self.direccion = DERECHA
        self.animacion = self.stay[DERECHA]

        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_pies = pygame.Rect(self.rect.x + self.rect.w/4, self.rect.y + self.rect.h -10, self.rect.w/2, 5)

        self.sobre_plataforma = True
        self.caminando = False
        self.saltando = False
        self.cayendo = False
        self.speed_jump = 10
        self.gravedad = 10
        self.inicio_salto = y

        self.orb = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\caracters\stink\disparo_animacion.png",16,2)[:31]
        self.disparando = False
        self.municion = 15
        self.proyectiles = []

        self.vida = 100
        self.golpeado = False
        self.hitted = {}
        self.hitted[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\caracters\stink\surprise.png",21,1)[:13]
        self.hitted[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\caracters\stink\surprise.png",21,1, True)[:13]

    def mover(self,direccion):
        if not self.golpeado:
            self.direccion = direccion
            self.caminando = True
            if self.direccion == DERECHA:
                self.move_x = self.speed_walk
                
            elif self.direccion == IZQUIERDA:
                self.move_x = -self.speed_walk
            

    def detener(self):
        if not self.golpeado:
            self.caminando = False
            self.move_x = 0


    def saltar(self, saltar):
        if not self.golpeado:
            if saltar:
                if self.sobre_plataforma:
                    self.saltando = True
                    self.inicio_salto = self.rect.y
            else:
                if self.saltando:
                    self.terminar_salto()


    def limitar_salto(self):
        if self.saltando and self.rect.y < self.inicio_salto - 140:
            self.terminar_salto()


    def terminar_salto(self):
        self.saltando = False
        self.caer(True)


    def controlar_movimiento_y(self):
        if not self.golpeado:
            if self.saltando:
                self.move_y = -self.speed_jump

            else:
                if self.sobre_plataforma:
                    self.caer(False)
                else:
                    self.caer(True)


    def caer(self, cayendo):
        if cayendo:
            self.move_y = self.gravedad
            self.cayendo = True
        else:
            self.move_y = 0
            self.cayendo = False


    def verificar_plataforma(self, plataformas):
        self.sobre_plataforma = False
        for plataforma in plataformas:
            if(self.rect_pies.colliderect(plataforma.rect_piso)):
                self.sobre_plataforma = True
                break   


    
    def disparar(self):
        if self.municion > 0:
            self.disparando = True
            if self.direccion == DERECHA:
                proyectil = DisparoHorizontal(self.rect.x + self.rect.w/2, self.rect.y + self.rect.h/2, 20, 18, 5, 30, 30, self.orb)
            else:
                proyectil = DisparoHorizontal(self.rect.x - self.rect.w/2 + 20, self.rect.y + self.rect.h/2, -20, -12, 5, 30, 30, self.orb)
            
            self.municion -= 1
            self.proyectiles.append(proyectil)
        else:
            self.disparando = False

    
    def cambiar_vida(self, modficacion):
        self.vida += modficacion

    def recibir_golpe(self):
        self.golpeado = True    
        if self.saltando:
            self.terminar_salto()
        
        if self.direccion == DERECHA:
            self.move_x = -6
        else:
            self.move_x = 6
        self.move_y = -2
        


    def animaciones(self):
        if not self.golpeado:
            if self.saltando:
                self.cambiar_animacion(self.jump)
            else:
                if self.cayendo:
                    self.cambiar_animacion(self.fall)
                else:
                    if self.caminando:
                        self.cambiar_animacion(self.walk)
                    else:
                        self.cambiar_animacion(self.stay)
        else:
            self.cambiar_animacion(self.hitted)

    def cambiar_animacion(self, animacion):
        if self.animacion != animacion[DERECHA] and self.animacion != animacion[IZQUIERDA]:
            self.frame = 0
        self.animacion = animacion[self.direccion]

         
    def actualizar_posicion(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.rect_pies.x += self.move_x
        self.rect_pies.y += self.move_y


    def updatear_frames(self):
        if(self.frame < len(self.animacion) - 1):
            self.frame += 1 
        else:
            self.frame = 0
            if self.cayendo:
                self.frame = len(self.animacion) - 1

            if self.golpeado:
                self.golpeado = False
                self.detener()
                self.move_y = 0
            
    

    def draw(self,screen):
        #pygame.draw.rect(screen,(0,0,0),self.rect_pies)
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen,self.rect)

    def actualizar_proyectiles(self, screen, objetivo):
        for proyectil in self.proyectiles:
            proyectil.actualizar_proyectil(screen, objetivo)
            if not proyectil.activo:
                self.proyectiles.remove(proyectil)


    def actualizar_player(self, screen, plataformas, objetivo):
        
        self.verificar_plataforma(plataformas)
        self.controlar_movimiento_y()
        self.actualizar_posicion()
        self.animaciones()
        self.updatear_frames()
        self.actualizar_proyectiles(screen, objetivo)
        self.draw(screen)
        


