import pygame
from functools import reduce
from random import shuffle
from constantes import *
from sonidos import *

class Tarjeta:
    surface_hide = pygame.transform.scale(pygame.image.load(PATH_RECURSOS + r"\00.png"), (ANCHO_TARJETA,ALTO_TARJETA))
    def __init__(self,nombre_imagen, x, y) -> None:
        self.visible = False
        self.descubierto = False
        self.path_imagen = PATH_RECURSOS + "\\" + nombre_imagen
        self.surface_imagen = pygame.transform.scale(pygame.image.load(self.path_imagen), (ANCHO_TARJETA,ALTO_TARJETA))
        self.rect = pygame.Rect((x,y),(ANCHO_TARJETA, ALTO_TARJETA))

    
    def verificar_colision(self, pos_xy):
        return self.rect.collidepoint(pos_xy) and not self.visible



class Tablero:
    def __init__(self) -> None:
        self.lista_tarjetas = []
        self.tiempo = 0
        self.musica_ganador = False


    def agregar_elemento(self, elemento: Tarjeta):
        self.lista_tarjetas.append(elemento)

    def cambiar_tiempo(self, tiempo):
        self.tiempo = tiempo

    def contar_tarjetas_descubiertas(self):
        return reduce(lambda acumulador, tarjeta : acumulador + 1 if tarjeta.descubierto else acumulador, self.lista_tarjetas, 0)

    def contar_tarjetas_visibles_no_descubiertas(self): 
        return reduce(lambda acumulador, tarjeta : acumulador + 1 if tarjeta.visible and not tarjeta.descubierto else acumulador, self.lista_tarjetas, 0)

    def comprobar_par_descubierto(self):
        tarjetas = list(filter(lambda tarjeta : tarjeta.visible and not tarjeta.descubierto, self.lista_tarjetas))
        if len(tarjetas) == 2:
            if tarjetas[0].path_imagen == tarjetas[1].path_imagen:
                tarjetas[0].descubierto = True
                tarjetas[1].descubierto = True
                sonido_clic.play()
            else:
                sonido_equivocado.play()


    def verificar_juego_terminado(self):
        return self.contar_tarjetas_descubiertas() == len(self.lista_tarjetas)

    def verificar_musica_ganador(self):
        if not self.musica_ganador:
            sonido_fondo.stop()
            sonido_ganador.play(-1)
            self.musica_ganador = True

    def mezclar_posicion_tarjetas(self):
        lista_rectangulos = list(map(lambda tarjeta : tarjeta.rect, self.lista_tarjetas))
        shuffle(lista_rectangulos)

        for tarjeta, rectangulo in zip(self.lista_tarjetas, lista_rectangulos):
            tarjeta.rect = rectangulo


class Texto:

    def __init__(self) -> None:
        self.font = pygame.font.SysFont("Arial Narrow", ALTO_TEXTO)
        self.tiempo = ""
        self.juego_terminado = self.font.render("Juego terminado!", True, (255, 0, 0))

    
    def actualizar_tiempo(self, minutos, segundos):
        self.tiempo = self.font.render("Tiempo: {0:02d}:{1:02d}".format(minutos, segundos), True, (255, 0, 0))