import pygame
from aux_constantes import *
from aux_frames import Auxiliar
from class_A import EnemyGuard


class Dust(EnemyGuard):
    def __init__(self, pos_x, pos_y, recorrido, screen):
        self.walk = {}
        self.walk[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\dust\walk_right.png",9,1)
        self.walk[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\dust\walk_right.png",9,1, True)
        super().__init__(self.walk[DERECHA], pos_x, pos_y, 10, pos_x - recorrido, pos_x + recorrido, DERECHA, 10, 20, 100, screen)
        self.rect_hitbox = pygame.Rect(pos_x + 20, pos_y + 10, 60, self.rect.h - 20)
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
                pygame.draw.rect(self.screen, C_CELEST, self.rect_hitbox)
                self.draw()