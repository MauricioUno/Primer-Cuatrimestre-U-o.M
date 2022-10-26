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
        if self.rect.collidepoint(pos_xy) and not self.visible:
            sonido_voltear.play()
            self.visible = True
            
            
    def __eq__(self, tarjeta):
        return self.path_imagen == tarjeta.path_imagen
    
    def comparar_tarjetas(self, tarjeta):
        if self == tarjeta:
            self.descubierto = True
            tarjeta.descubierto = True
            sonido_clic.play()
        else:
            self.visible=False
            tarjeta.visible=False
            sonido_equivocado.play()


class Tablero:
    
    def __init__(self) -> None:
        self.lista_tarjetas = []
        self.cargar_tarjetas()
        self.mezclar_posicion_tarjetas()
        self.tiempo = 0
        self.musica_ganador = False


    def cargar_tarjetas(self):
        i = 1
        for x in range(0,CANTIDAD_TARJETAS_H*ANCHO_TARJETA,ANCHO_TARJETA):
            for y in range(0,CANTIDAD_TARJETAS_V*ALTO_TARJETA,ALTO_TARJETA):
                if(i > CANTIDAD_TARJETAS_UNICAS):
                    tarjeta = Tarjeta("0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS), x, y)
                else:
                    tarjeta = Tarjeta("0{0}.png".format(i), x, y)
                self.lista_tarjetas.append(tarjeta)
                i = i + 1


    def mezclar_posicion_tarjetas(self):
        lista_rectangulos = list(map(lambda tarjeta : tarjeta.rect, self.lista_tarjetas))
        shuffle(lista_rectangulos)

        for tarjeta, rectangulo in zip(self.lista_tarjetas, lista_rectangulos):
            tarjeta.rect = rectangulo


    def contar_tarjetas_descubiertas(self):
        return reduce(lambda acumulador, tarjeta : acumulador + 1 if tarjeta.descubierto else acumulador, self.lista_tarjetas, 0)


    def contar_tarjetas_visibles_no_descubiertas(self): 
        return reduce(lambda acumulador, tarjeta : acumulador + 1 if tarjeta.visible and not tarjeta.descubierto else acumulador, self.lista_tarjetas, 0)


    def comparar_par_visible_no_descubierto(self):
        '''
        Solo se llama a este metodo cuando la cantidad de tarjetas visibles no descubiertas en la lista es igual a 2
        '''
        lista_tarjetas = list(filter(lambda tarjeta : tarjeta.visible and not tarjeta.descubierto, self.lista_tarjetas))
        lista_tarjetas[0].comparar_tarjetas(lista_tarjetas[1])


    def colision(self, pos_xy):
        if (self.contar_tarjetas_visibles_no_descubiertas() < 2):
            for tarjeta in self.lista_tarjetas:
                tarjeta.verificar_colision(pos_xy)
                if (self.contar_tarjetas_visibles_no_descubiertas() == 2):
                    self.tiempo = pygame.time.get_ticks()
                    

    def update(self):
        tiempo_actual = pygame.time.get_ticks()
        if self.tiempo > 0 and tiempo_actual - self.tiempo > 500:
            self.comparar_par_visible_no_descubierto()
            self.tiempo = 0
                    
    def verificar_juego_terminado(self):
        return self.contar_tarjetas_descubiertas() == len(self.lista_tarjetas)


    def cambiar_musica_ganador(self):
        if not self.musica_ganador:
            sonido_fondo.stop()
            sonido_ganador.play(-1)
            self.musica_ganador = True



class Texto:

    def __init__(self) -> None:
        self.font = pygame.font.SysFont("Arial Narrow", ALTO_TEXTO)
        self.tiempo = self.font.render("Tiempo: {0:02d}:{1:02d}".format(0, 0), True, (255, 0, 0))
        self.juego_terminado = self.font.render("Juego terminado!", True, (255, 0, 0))

    
    def actualizar_tiempo(self, minutos, segundos):
        self.tiempo = self.font.render("Tiempo: {0:02d}:{1:02d}".format(minutos, segundos), True, (255, 0, 0))