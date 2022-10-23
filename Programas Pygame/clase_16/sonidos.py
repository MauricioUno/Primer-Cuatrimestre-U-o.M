import pygame

path = r"C:\Users\Mauricio\Documents\Pez UTN\Primer-Cuatrimestre-UnoMauricio\Programas Pygame\clase_16\recursos\\"

pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)

sonido_fondo = pygame.mixer.Sound(path + "fondo.wav")
sonido_fondo.set_volume(0.2)

sonido_clic = pygame.mixer.Sound(path + "clic.wav")
sonido_clic.set_volume(0.2)

sonido_equivocado = pygame.mixer.Sound(path + "equivocado.wav")
sonido_equivocado.set_volume(0.2)

sonido_ganador = pygame.mixer.Sound(path + "ganador.wav")
sonido_ganador.set_volume(0.2)

sonido_voltear = pygame.mixer.Sound(path + "voltear.wav")
sonido_voltear.set_volume(0.2)