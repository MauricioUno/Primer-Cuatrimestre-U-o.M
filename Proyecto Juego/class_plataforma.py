import pygame
from aux_constantes import *
from class_texto import Imagen


class Plataforma(Imagen):
    def __init__(self, pos_x, pos_y, ancho, alto, path_imagen, speed_x, speed_y, screen) -> None:
        super().__init__(path_imagen, ancho, alto, pos_x, pos_y, screen)
        self.rect_piso = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, 5)
        self.existente = True
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.move_x = self.speed_x
        self.move_y = self.speed_y
        self.minimo_x = self.rect.x
        self.minimo_y = self.rect.y
        self.maximo_x = self.minimo_x + 300
        self.maximo_y = self.minimo_y + 200
        self.avanzando = True
        self.timer = 0



    def controlar_movimiento_x(self):
        if self.avanzando:
            if self.rect.x < self.maximo_x:
                self.move_x = self.speed_x
            else:
                self.avanzando = False        
        else:
            if self.rect.x > self.minimo_x:
                self.move_x = -self.speed_x
            else:
                self.avanzando = True


    def actualizar_posicion(self):
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.rect_piso.x += self.move_x
        self.rect_piso.y += self.move_y



    def actualizar_plataforma(self, delta_ms):
        self.timer += delta_ms
        if self.timer > 30:
            self.timer = 0
            self.controlar_movimiento_x()
            self.actualizar_posicion()
            self.draw()



class GrupoPlataformas:
    def __init__(self,lista_plataformas, screen) -> None:
        self.lista = []
        self.screen = screen
        self.agregar_plataforma(lista_plataformas)

    def agregar_plataforma(self, lista_datos: list[dict]):
        for datos in lista_datos:
            plataforma = Plataforma(datos["pos_x"], datos["pos_y"], datos["ancho"], datos["alto"], r"\tile\grass.png", datos["speed_x"], datos["speed_y"], self.screen)
            self.lista.append(plataforma)


    def actualizar(self, delta_ms):
        for plataforma in self.lista:
            plataforma.actualizar_plataforma(delta_ms)



