import pygame
from aux_constantes import *
from class_A import Imagen


class Plataforma(Imagen):
    def __init__(self, pos_x, pos_y, ancho, alto, tipo, terreno, screen) -> None:
        super().__init__("/tile/{0}.png".format(tipo), ancho, alto, pos_x, pos_y, screen)
        self.rect_piso = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, 10)
        self.terreno = terreno
        self.move_x = 0
        self.move_y = 0
        self.timer = 0
        

    def actualizar_plataforma(self, delta_ms):
        self.timer += delta_ms
        if self.timer > 30:
            self.timer = 0
            self.draw()




class PlataformaMovil(Plataforma):
    def __init__(self, pos_x, pos_y, ancho, alto, tipo, speed_x, speed_y, ruta, terreno, screen) -> None:
        super().__init__(pos_x, pos_y, ancho, alto, tipo, terreno, screen)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.move_x = self.speed_x
        self.move_y = self.speed_y
        self.minimo_x = self.rect.x
        self.minimo_y = self.rect.y
        self.maximo_x = self.minimo_x + ruta
        self.maximo_y = self.minimo_y - ruta
        self.avanzando = True
        self.subiendo = True


    def controlar_movimiento_x(self):
        if self.avanzando:
            if self.rect.x < self.maximo_x:
                self.move_x = self.speed_x
                self.direccion = DERECHA
            else:
                self.avanzando = False        
        else:
            if self.rect.x > self.minimo_x:
                self.move_x = -self.speed_x
                self.direccion = IZQUIERDA
            else:
                self.avanzando = True


    def controlar_movimiento_y(self):
        if self.subiendo:
            if self.rect.y > self.maximo_y:
                self.move_y = -self.speed_y
            else:
                self.subiendo = False        
        else:
            if self.rect.y < self.minimo_y:
                self.move_y = self.speed_y
            else:
                self.subiendo = True


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
            self.controlar_movimiento_y()
            self.actualizar_posicion()
            self.draw()





class ListaPlataformas:
    def __init__(self,lista_plataformas, screen, name) -> None:
        self.lista = []
        self.screen = screen
        self.name = name

        if "terreno" in lista_plataformas.keys():
            self.agregar_plataforma(lista_plataformas["terreno"])


        if "moviles" in lista_plataformas.keys():
            self.agregar_plataforma_movil(lista_plataformas["moviles"])

    def agregar_plataforma(self, lista_plataformas):
        for dato in lista_plataformas:
            pos_y = dato["pos"][1]
            ancho = dato["dim"][0]
            alto = dato["dim"][1]
            for y in range(dato["qty"][1]):
                pos_x = dato["pos"][0]
                for x in range(dato["qty"][0]):
                    tile = "{0}/{1}".format(self.name, dato["tipo"])
                    plataforma = Plataforma(pos_x, pos_y, ancho, alto, tile, dato["colision"], self.screen)
                    self.lista.append(plataforma)
                    pos_x += ancho
                pos_y += alto


    def agregar_plataforma_movil(self, lista_plataformas):
        for dato in lista_plataformas:
            tile = "{0}/{1}".format(self.name, dato["tipo"])
            plataforma = PlataformaMovil(dato["pos"][0], dato["pos"][1], dato["dim"][0], dato["dim"][1], tile, dato["move"][0], dato["move"][1], dato["route"],0, self.screen)
            self.lista.append(plataforma)

    def actualizar(self, delta_ms):
        for plataforma in self.lista:
            plataforma.actualizar_plataforma(delta_ms)



