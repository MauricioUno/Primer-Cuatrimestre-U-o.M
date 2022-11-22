import pygame
import sys
from pygame.locals import *
from class_menu import *
from class_texto import *
from nivel_uno import iniciar_nivel_uno
from aux_constantes import *
from aux_sonidos import *
from aux_data_menus import *

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), DOUBLEBUF, 16)
imagen_menu = Imagen(r"\imagenes\Fondos\space.jpg", ANCHO_VENTANA, ALTO_VENTANA, 0, 0, pantalla)
time_clock = pygame.time.Clock()
sonido_fondo.play(-1)

def menu_principal(screen, fondo, clock):
    pygame.display.set_caption('Glitch is Dead, Long Live Glitch!')
    
    menu_main = Menu(textos_main, textos_int_main, [], screen)
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_main.textos_interactivos[0].rect_hitbox.collidepoint(event.pos):
                    menu_start(screen, fondo, clock)
                elif  menu_main.textos_interactivos[1].rect_hitbox.collidepoint(event.pos):
                    print("menu opciones")
                elif  menu_main.textos_interactivos[2].rect_hitbox.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                

        fondo.draw()
        menu_main.update(screen)
        
        pygame.display.flip()



def menu_start(screen, fondo, clock):

    menu_start = Menu(textos_start, textos_int_start, imagenes_start, screen)
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_start.textos_interactivos[0].rect_hitbox.collidepoint(event.pos):
                    menu_principal(screen, fondo, clock)

                elif menu_start.imagenes[0].rect.collidepoint(event.pos):
                    sonido_fondo.stop()
                    iniciar_nivel_uno(screen, clock)

                elif menu_start.imagenes[1].rect.collidepoint(event.pos):
                    pass 

                elif menu_start.imagenes[2].rect.collidepoint(event.pos):
                    pass 
                

        fondo.draw()
        menu_start.update(screen)
        pygame.display.flip()




menu_principal(pantalla, imagen_menu, time_clock)