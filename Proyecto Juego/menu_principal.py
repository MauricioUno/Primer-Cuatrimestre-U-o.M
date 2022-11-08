import pygame
import sys
from class_menu import *
from class_texto import *
from nivel_uno import iniciar_nivel_uno
from aux_constantes import *
from aux_sonidos import *
from aux_data_menus import *

pygame.init()
pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
imagen_menu = Imagen(r"\imagenes\Fondos\escalando.jpg", ANCHO_VENTANA, ALTO_VENTANA, 0, 0)
time_clock = pygame.time.Clock()
sonido_fondo.play(-1)

def menu_principal(screen, fondo, clock):
    pygame.display.set_caption('Glitch is Dead, Long Live Glitch!')
    
    menu_main = Menu(textos_main, textos_int_main, [])
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_main.textos_interactivos[0].rect_hitbox.collidepoint(event.pos):
                    menu_start(screen, fondo, clock)
                elif  menu_main.textos_interactivos[1].rect_hitbox.collidepoint(event.pos):
                    menu_opciones(screen, fondo, clock)
                elif  menu_main.textos_interactivos[2].rect_hitbox.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                

        fondo.draw(screen)
        menu_main.update(screen)
        
        pygame.display.flip()



def menu_start(screen, fondo, clock):

    menu_start = Menu(textos_start, textos_int_start, imagenes_start)
    while True:
        clock.tick(FPS)

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
                

        fondo.draw(screen)
        menu_start.update(screen)
        pygame.display.flip()


def menu_opciones(screen, fondo, clock):
    
    menu_opciones = Menu([], textos_int_opciones, [])

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_opciones.textos_interactivos[0].rect_hitbox.collidepoint(event.pos):
                    menu_score(screen, fondo, clock)

                elif menu_opciones.textos_interactivos[1].rect.collidepoint(event.pos):
                    pass

                elif menu_opciones.textos_interactivos[2].rect.collidepoint(event.pos):
                    pass 

                elif menu_opciones.textos_interactivos[3].rect.collidepoint(event.pos):
                    menu_principal(screen, fondo, clock) 
                

        fondo.draw(screen)
        menu_opciones.update(screen)
        pygame.display.flip()


def menu_score(screen, fondo, clock):
    menu_score = Menu(textos_score, textos_int_score, [])
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_score.textos_interactivos[0].rect_hitbox.collidepoint(event.pos):
                    menu_opciones(screen, fondo, clock)
                

        fondo.draw(screen)
        menu_score.update(screen)
        pygame.display.flip()

menu_principal(pantalla, imagen_menu, time_clock)