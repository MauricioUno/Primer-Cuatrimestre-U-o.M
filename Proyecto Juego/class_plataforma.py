import pygame
from aux_constantes import *
from class_texto import Imagen


class Plataforma(Imagen):
    def __init__(self, pos_x, pos_y, ancho, alto, path_imagen) -> None:
        super().__init__(path_imagen, ancho, alto, pos_x, pos_y)
        self.rect_piso = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, 5)


    def draw(self,screen):
        screen.blit(self.imagen,self.rect)


class PlataformaTemporal(Plataforma):
    def __init__(self, pos_x, pos_y, ancho, alto, bloque) -> None:
        super().__init__(pos_x, pos_y, ancho, alto, bloque)
        self.existente = True

    def cambiar_estado(self):
        self.existente = not self.existente

    


class GrupoPlataformas:
    def __init__(self,lista_plataformas) -> None:
        self.lista = []
        self.agregar_plataforma(lista_plataformas)

    def agregar_plataforma(self, lista_datos: list[dict]):
        for datos in lista_datos:
            plataforma = Plataforma(datos["pos_x"], datos["pos_y"], datos["ancho"], datos["alto"], r"\tile\grass.png")
            self.lista.append(plataforma)


    def actualizar_plataformas(self, screen):
        for plataforma in self.lista:
            plataforma.draw(screen)



