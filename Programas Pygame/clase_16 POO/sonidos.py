import pygame
from constantes import *

pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)

sonido_fondo = pygame.mixer.Sound(PATH_RECURSOS + r"\fondo.wav")
sonido_fondo.set_volume(0.1)

sonido_clic = pygame.mixer.Sound(PATH_RECURSOS + "\clic.wav")
sonido_clic.set_volume(0.2)

sonido_equivocado = pygame.mixer.Sound(PATH_RECURSOS + "\equivocado.wav")
sonido_equivocado.set_volume(0.2)

sonido_ganador = pygame.mixer.Sound(PATH_RECURSOS + "\ganador.wav")
sonido_ganador.set_volume(0.1)

sonido_voltear = pygame.mixer.Sound(PATH_RECURSOS + r"\voltear.wav")
sonido_voltear.set_volume(0.5)