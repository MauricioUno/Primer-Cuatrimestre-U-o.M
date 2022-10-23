import pygame
import math
import random
import tarjeta
from constantes import *
from sonidos import *

def init():
    
    d_tablero = {}
    lista_tarjetas = []
    i = 1
    for x in range(0,CANTIDAD_TARJETAS_H*ANCHO_TARJETA,ANCHO_TARJETA):
        for y in range(0,CANTIDAD_TARJETAS_V*ALTO_TARJETA,ALTO_TARJETA):
            if(i > CANTIDAD_TARJETAS_UNICAS):
                tarjeta_test = tarjeta.init("0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS),r"\00.png",x,y)
            else:
                tarjeta_test = tarjeta.init("0{0}.png".format(i),r"\00.png",x,y)
            lista_tarjetas.append(tarjeta_test)
            i = i + 1
            

    d_tablero["l_tarjetas"] = lista_tarjetas
    d_tablero["tiempo_ultimo_destape"] = 0

    return d_tablero

def colicion(d_tablero,pos_xy):
    cant_tarjetas = tarjeta.cantidad_tarjetas_visibles_no_descubiertas(d_tablero["l_tarjetas"])
    if (cant_tarjetas < 2):
        for aux_tarjeta in d_tablero["l_tarjetas"]:
            if aux_tarjeta["rect"].collidepoint(pos_xy) and not aux_tarjeta["visible"]:
                sonido_voltear.play()
                aux_tarjeta["visible"] = True
                d_tablero["tiempo_ultimo_destape"] = pygame.time.get_ticks()

def update(d_tablero):
    
    tiempo_actual = pygame.time.get_ticks()
    if d_tablero["tiempo_ultimo_destape"] > 0:
        cant_tarjetas = tarjeta.cantidad_tarjetas_visibles_no_descubiertas(d_tablero["l_tarjetas"])
        if tiempo_actual - d_tablero["tiempo_ultimo_destape"] > 1000 and cant_tarjetas == 2:
            d_tablero["tiempo_ultimo_destape"] = 0
            for aux_tarjeta in d_tablero["l_tarjetas"]:
                if not aux_tarjeta["descubierto"]:
                    aux_tarjeta["visible"]=False

        if tarjeta.match(d_tablero["l_tarjetas"]):
            d_tablero["tiempo_ultimo_destape"] = 0
    

def render(d_tablero,pantalla_juego, segundos, minutos):
    
    for aux_tarjeta in d_tablero["l_tarjetas"]:
        if(aux_tarjeta["visible"]):
            pantalla_juego.blit(aux_tarjeta["surface"],aux_tarjeta["rect"])
        else:
            pantalla_juego.blit(aux_tarjeta["surface_hide"],aux_tarjeta["rect"])


    font = pygame.font.SysFont("Arial Narrow", ALTO_TEXTO)
    text = font.render("Tiempo: {0:02d}:{1:02d}".format(minutos, segundos), True, (255, 0, 0))
    pantalla_juego.blit(text, (0,450))

    if verificar_juego_terminado(d_tablero["l_tarjetas"]):
        ganador = font.render("Terminado!", True, (255, 0, 0))
        pantalla_juego.blit(ganador, (0,500))


def verificar_juego_terminado(lista_tarjetas):
    cant_tarjetas_descubiertas = tarjeta.cantidad_tarjetas_descubiertas(lista_tarjetas)
    if cant_tarjetas_descubiertas == len(lista_tarjetas):
        juego_terminado = True
        sonido_fondo.stop()
        sonido_ganador.play(-1)
    else:
        juego_terminado = False

    return juego_terminado


def mezclar_posicion_tarjetas(lista_tarjetas):
    
    lista_posiciones = list(map(lambda tarjeta : tarjeta["rect"], lista_tarjetas))
    random.shuffle(lista_posiciones)

    for indice,tarjeta in enumerate(lista_tarjetas):
        tarjeta["rect"] = lista_posiciones[indice]
    


     