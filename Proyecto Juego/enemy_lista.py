from enemy_groodle import SpiritGroodle
from enemy_ix import SpiritIx
from enemy_batterflies import GrupoBatterflies
from aux_constantes import *


class ListaEnemiesNivelUno:
    def __init__(self, screen) -> None:
        self.master_screen = screen
        self.groodle = SpiritGroodle(790, 330, IZQUIERDA, self.master_screen)
        self.ix = SpiritIx(500, 610, DERECHA, 10, 200, 700, self.master_screen)
        self.batterflies = GrupoBatterflies(3, self.master_screen)


    def actualizar(self, jugador, delta_ms):
        self.lista = []

        self.groodle.actualizar(jugador, delta_ms)
        if self.groodle.activo:
            self.lista.append(self.groodle)
            
        self.ix.actualizar(jugador, delta_ms)
        if self.ix.activo:
            self.lista.append(self.ix)
            
        self.batterflies.actualizar(jugador, delta_ms)
        for batterfly in self.batterflies.lista_batterflies:
            self.lista.append(batterfly)

        