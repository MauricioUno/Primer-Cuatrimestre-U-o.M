from aux_constantes import *
from aux_frames import Auxiliar
import pygame
from class_A import ObjetoAnimado
from class_proyectil import GrupoProyectiles

class SpiritGroodle(ObjetoAnimado):

    def __init__(self, pos_x, pos_y, direccion, screen) -> None:
        self.screen = screen
        self.direccion = direccion
        self.stay = {}
        self.stay[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\groodle\stay.png",9,10, False, 1, True, 100, 130)[:85]
        self.stay[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\groodle\stay.png",9,10, True, 1, True, 100, 130)[:85]

        self.attack = {}
        self.attack[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\groodle\attack.png",9,2, False, 1, True, 100, 130)[:17]
        self.attack[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\groodle\attack.png",9,2, True, 1, True, 100, 130)[:17]
        
        self.animacion_disparo = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\groodle\proyectil.png",10,2)
        super().__init__(self.stay[self.direccion], pos_x, pos_y, self.screen)
        self.rect_hitbox = pygame.Rect(pos_x + 15, pos_y + 30, 70, 70)

        if self.direccion == DERECHA:
            self.rect_vision = pygame.Rect(pos_x - 20 + self.rect.w, pos_y, 400, 100)
            self.velocidad = 15
        else:
            self.rect_vision = pygame.Rect(pos_x - 270 - self.rect.w, pos_y, 400, 100)
            self.velocidad = -15

        self.activo = True
        self.damage = 30
        self.vida = 150
        self.puntos = 500
        self.proyectiles = GrupoProyectiles(self, self.screen)
        self.atacando = False
        self.timer = 0
        self.shoot_allowed = True
        self.timer_disparo = 0


    def disparar(self, jugadores):
        if self.shoot_allowed:
            for jugador in jugadores:
                if self.rect_vision.colliderect(jugador.rect_hitbox) and jugador.activo:
                    self.atacando = True
                    self.shoot_allowed = False
                    self.proyectiles.agregar_disparo(self.rect.x + 15, self.rect.y + 60, self.velocidad, 35, 10, 15, 15, self.animacion_disparo, 25)
                    break
                else:
                    self.atacando = False

    def actualizar_cooldown_disparo(self, delta_ms):
        if not self.shoot_allowed:
            self.timer_disparo += delta_ms
            if self.timer_disparo > 750:
                self.timer_disparo = 0
                self.shoot_allowed = True


    def animaciones(self):
        
        if not self.atacando:
            self.cambiar_animacion(self.stay)
        else:
            self.cambiar_animacion(self.attack)


    def cambiar_animacion(self, animacion):
        if self.animacion != animacion[DERECHA] and self.animacion != animacion[IZQUIERDA]:
            self.frame = 0
        self.animacion = animacion[self.direccion]


    def recibir_golpe(self, proyectil):
        self.vida += -proyectil.damage
        print("Vida Groodle: {0}".format(self.vida))
        if self.vida < 1:
            self.activo = False
            proyectil.master.score += self.puntos
        

    def actualizar(self, jugador, delta_ms):
        if self.activo:
            self.timer += delta_ms
            if self.timer > 30:
                self.timer = 0
                self.disparar([jugador])
                self.actualizar_cooldown_disparo(delta_ms)
                self.animaciones()
                self.updatear_frames()
                self.proyectiles.actualizar_disparos([jugador])
                self.draw()
