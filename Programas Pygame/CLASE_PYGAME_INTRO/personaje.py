import pygame


def crear(x,y,ancho,alto):
    imagen_personaje = pygame.image.load("Programas Pygame\CLASE_PYGAME_INTRO\spriteHomero.png")
    imagen_personaje = pygame.transform.scale(imagen_personaje, (ancho,alto))
    rect_personaje = pygame.Rect(x, y, ancho, alto)
    rect_boca= pygame.Rect((x+ancho/2)-10, y+90, 40, 20)
    dict_personaje = {
                    "surface": imagen_personaje, 
                    "rect_pos": rect_personaje, 
                    "rect": rect_boca, 
                    "score": 0
                    }

    return dict_personaje


def update(personaje,incremento_x):
    nueva_x = personaje["rect"].x + incremento_x
    verificar_limite_pantalla(nueva_x, personaje, incremento_x)

def verificar_limite_pantalla(nueva_x,personaje, incremento_x):
    if(nueva_x > 0 and nueva_x < 770):
        personaje["rect_pos"].x = personaje["rect_pos"].x + incremento_x
        personaje["rect"].x = personaje["rect"].x + incremento_x

def actualizar_pantalla(personaje,ventana_ppal):
    ventana_ppal.blit(personaje["surface"],personaje["rect_pos"])
    



