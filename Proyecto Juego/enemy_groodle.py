from aux_constantes import *
from aux_frames import Auxiliar
import pygame
from class_padre import *

class SpiritGroodle(ObjetoAnimado):

    def __init__(self, pos_x, pos_y, direccion) -> None:
        self.direccion = direccion
        self.stay = {}
        self.stay[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\inhabitants\coco_fantasma\stay.png",9,10, False, 1, True, 100, 130)[:85]
        self.stay[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\inhabitants\coco_fantasma\stay.png",9,10, True, 1, True, 100, 130)[:85]

        self.attack = {}
        self.attack[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\inhabitants\coco_fantasma\attack.png",9,2, False, 1, True, 100, 130)[:17]
        self.attack[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\inhabitants\coco_fantasma\attack.png",9,2, True, 1, True, 100, 130)[:17]
        self.animacion_disparo = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\inhabitants\coco_fantasma\proyectil.png",10,2)
        super().__init__(self.stay[self.direccion], pos_x, pos_y)

        if self.direccion == DERECHA:
            self.rect_vision = pygame.Rect(pos_x - 20 + self.rect.w, pos_y, 400, 100)
            self.velocidad = 15
        else:
            self.rect_vision = pygame.Rect(pos_x - 270 - self.rect.w, pos_y, 400, 100)
            self.velocidad = -15

        self.proyectiles = []
        self.atacando = False

    def disparar(self, rect_jugador):
        if self.rect_vision.colliderect(rect_jugador):
            self.atacando = True
            proyectil = DisparoHorizontal(self.rect.x + 15, self.rect.y + 60, self.velocidad, 35, 10, 15, 15, self.animacion_disparo)
            self.proyectiles.append(proyectil)
        else:
            self.atacando = False


    def animaciones(self):
        
        if not self.atacando:
            if self.animacion != self.stay[DERECHA] and self.animacion != self.stay[IZQUIERDA]:
                self.frame = 0
            self.animacion = self.stay[self.direccion]
        else:
            if self.animacion != self.attack[DERECHA] and self.animacion != self.attack[IZQUIERDA]:
                self.frame = 0
            self.animacion = self.attack[self.direccion]


    def actualizar_proyectiles(self, screen, jugador):
        for proyectil in self.proyectiles:
            proyectil: DisparoHorizontal
            proyectil.actualizar_proyectil(screen, jugador)
            if not proyectil.activo:
                self.proyectiles.remove(proyectil)


    def actualizar_groodle(self, screen, jugador):
        self.animaciones()
        self.updatear_frames()
        self.draw(screen)
        self.actualizar_proyectiles(screen, jugador)
