import pygame
from aux_constantes import *

pygame.mixer.init()
sonido_fondo = pygame.mixer.Sound(PATH_RECURSOS + r"\imagenes\Auxiliar\musica_menu.wav")
sonido_fondo.set_volume(0.1)

sonido_nivel_uno = pygame.mixer.Sound(PATH_RECURSOS + r"\imagenes\Auxiliar\musica_nivel_uno.wav")
sonido_nivel_uno.set_volume(0.1)