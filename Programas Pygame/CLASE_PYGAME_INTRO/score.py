import pygame
import random
def actualizar_pantalla(personaje, ventana_ppal):
    font = pygame.font.SysFont("Arial Narrow", 50)
    text = font.render("SCORE: {0}".format(personaje["score"]), True, (255, 0, 0))
    ventana_ppal.blit(text,(0,0))


def aumentar_velocidad_donas(personaje, donas):
    if personaje["score"] > 5000:
        for dona in donas:
            dona["speed"] = random.randrange (10,30,1)
            