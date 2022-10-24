import pygame
from constantes import *

def obtener_diccionario_textos(minutos, segundos):
    font = pygame.font.SysFont("Arial Narrow", ALTO_TEXTO)
    diccionario_textos = {}
    
    diccionario_textos["time"] = font.render("Tiempo: {0:02d}:{1:02d}".format(minutos, segundos), True, (255, 0, 0))
    diccionario_textos["juego_terminado"] = font.render("Juego terminado!", True, (255, 0, 0))

    return diccionario_textos

def actualizar_reloj(diccionario_textos, minutos, segundos):
    font = pygame.font.SysFont("Arial Narrow", ALTO_TEXTO)
    diccionario_textos["time"] = font.render("Tiempo: {0:02d}:{1:02d}".format(minutos, segundos), True, (255, 0, 0))