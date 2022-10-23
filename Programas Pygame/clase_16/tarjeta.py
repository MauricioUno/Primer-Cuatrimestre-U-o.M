import pygame
from constantes import *
from functools import reduce
from sonidos import *

def init(nombre_imagen,nombre_imagen_hide,x,y):
    
    nueva_tarjeta = {}
    nueva_tarjeta["visible"] = False
    nueva_tarjeta["descubierto"] = False
    nueva_tarjeta["path_imagen"] = PATH_RECURSOS + "\\" + nombre_imagen
    nueva_tarjeta["surface"] = pygame.transform.scale(pygame.image.load(nueva_tarjeta["path_imagen"]), (ANCHO_TARJETA,ALTO_TARJETA))
    nueva_tarjeta["surface_hide"] = pygame.transform.scale(pygame.image.load(PATH_RECURSOS+nombre_imagen_hide), (ANCHO_TARJETA,ALTO_TARJETA))
    nueva_tarjeta["rect"] = nueva_tarjeta["surface"].get_rect()
    nueva_tarjeta["rect"].x = x
    nueva_tarjeta["rect"].y = y
    return nueva_tarjeta


def cantidad_tarjetas_descubiertas(lista_tarjetas):
    cantidad = reduce(lambda acumulador, elemento : acumulador + 1 if elemento["descubierto"] else acumulador, lista_tarjetas, 0)
    return cantidad
     

def cantidad_tarjetas_visibles_no_descubiertas(lista_tarjetas):
    cantidad = reduce(lambda acumulador, tarjeta : acumulador + 1 if tarjeta["visible"] and not tarjeta["descubierto"] else acumulador, lista_tarjetas, 0)
    return cantidad

def match(lista_tarjetas):
    tarjetas = list(filter(lambda tarjeta : tarjeta["visible"] and not tarjeta["descubierto"], lista_tarjetas))
    if len(tarjetas) == 2:
        if(tarjetas[0]["path_imagen"] == tarjetas[1]["path_imagen"]):
            tarjetas[0]["descubierto"] = True
            tarjetas[1]["descubierto"] = True
            sonido_clic.play()
            return True
        else:
            sonido_equivocado.play()

    return False
