import pygame
import random

def crear(x,y,ancho,alto):
    imagen_dona = pygame.image.load("Programas Pygame\CLASE_PYGAME_INTRO\spriteDona.png")
    imagen_dona = pygame.transform.scale(imagen_dona,(ancho,alto))
    rect_dona = pygame.Rect(x, y, ancho, alto)
    dict_dona = {
                "surface": imagen_dona, 
                "rect": rect_dona, 
                "speed": random.randrange (10,20,1)
                }
    return dict_dona

def crear_lista_donas(cantidad):
    lista_donas = []
    for i in range(cantidad):
        y = random.randrange (-1000,0,60)
        x = random.randrange (0,740,60)
        lista_donas.append(crear(x,y,60,60))
    return lista_donas


def update(lista_donas, personaje):
    for dona in lista_donas:
        dona["rect"].y = dona["rect"].y + dona["speed"]
        if verificar_colision_o_final(personaje, dona):
            dona["rect"].x = random.randrange (0,740,60)
            dona["rect"].y = random.randrange (-1000,0,60)

def verificar_colision_o_final(personaje, dona):
    reiniciar = False
    if(personaje["rect"].colliderect(dona["rect"])):
        personaje["score"] = personaje["score"] + 100
        reiniciar = True
        
    if(dona["rect"].y > 880):
        reiniciar = True

    return reiniciar

def actualizar_pantalla(lista_donas,ventana_ppal):
    for dona in lista_donas:
        ventana_ppal.blit(dona["surface"],dona["rect"])