import pygame
from aux_constantes import *
from aux_frames import Auxiliar
from class_A import EnemyGuard


class SpiritIx(EnemyGuard):
    def __init__(self, pos_x, pos_y, recorrido, screen):
        self.walk = {}
        self.walk[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\ix\talk.png",7,18, False, 1, True, 130, 100)[:122]
        self.walk[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\ix\talk.png",7,18, True, 1, True, 130, 100)[:122]      
        super().__init__(self.walk[DERECHA], pos_x, pos_y, 7, pos_x - recorrido, pos_x + recorrido, DERECHA, 25, 30, 250, screen)
        self.rect_hitbox = pygame.Rect(pos_x + 20, pos_y + 10, 90, self.rect.h - 20)
        self.timer = 0


    def actualizar_posicion(self):
        super().actualizar_posicion()
        self.rect_hitbox.x += self.move_x


    def actualizar(self, jugador, delta_ms):
        if self.activo:
            self.timer += delta_ms
            if self.timer > 30:
                self.timer = 0
                self.updatear_frames()
                self.controlar_ruta()
                self.animacion = self.walk[self.direccion]
                self.actualizar_posicion()
                self.draw()
