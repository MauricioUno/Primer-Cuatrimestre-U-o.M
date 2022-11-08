from aux_constantes import *
from aux_frames import Auxiliar
from class_padre import *


class SpiritIx(ObjetoAnimado):
    def __init__(self, pos_x, pos_y, direccion, velocidad, min_x, max_x):
        self.direccion = direccion
        self.walk = {}
        self.walk[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\inhabitants\fongus\talk.png",7,18, False, 1, True, 130, 100)[:122]
        self.walk[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\inhabitants\fongus\talk.png",7,18, True, 1, True, 130, 100)[:122]

        self.velocidad = velocidad
        self.move_x = self.velocidad
        self.retrocediendo = False
        self.maximo_x = max_x
        self.minimo_x = min_x        
        super().__init__(self.walk[self.direccion], pos_x, pos_y)


    def controlar_ruta(self):
        if self.retrocediendo:
            if self.rect.x > self.minimo_x:
                self.move_x = -self.velocidad
                self.animacion = self.walk[IZQUIERDA]
            else:
                self.retrocediendo = False        
        else:
            if self.rect.x < self.maximo_x:
                self.move_x = self.velocidad
                self.animacion = self.walk[DERECHA]
            else:
                self.retrocediendo = True


    def actualizar_posicion(self):
        self.rect.x += self.move_x



    def actualizar_ix(self, screen):
        self.updatear_frames()
        self.controlar_ruta()
        self.actualizar_posicion()
        self.draw(screen)
