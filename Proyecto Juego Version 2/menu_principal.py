import pygame
from pygame.locals import *
import sys
from aux_constantes import *
from gui_form_menu_nivel import FormMenuNiveles
from gui_form_menu_main import FormMenuMain
from gui_form_nivel_uno import FormNivelUno

pygame.init()

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
clock = pygame.time.Clock()

form_menu_A = FormMenuNiveles(name="form_menu_A",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background =PATH_RECURSOS + r"\imagenes\Fondos\Space.jpg", color_border= None,active=False)
form_menu_B = FormMenuMain(name="form_menu_B",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background =PATH_RECURSOS + r"\imagenes\Fondos\Escalando.jpg", color_border= None,active=True)
form_nivel_uno = FormNivelUno(name="form_nivel_uno", master_surface= screen, x=0, y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background =PATH_RECURSOS + r"\locations\green forest\all.png", color_border= None,active=False)


while True:
    delta_ms = clock.tick(FPS)
    lista_eventos = pygame.event.get()
    teclas_presionadas = pygame.key.get_pressed()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if(form_menu_A.active):
        form_menu_A.update(lista_eventos)
        form_menu_A.draw(delta_ms)

    elif(form_menu_B.active):
        form_menu_B.update(lista_eventos)
        form_menu_B.draw(delta_ms)

    elif(form_nivel_uno.active):
            form_nivel_uno.update(lista_eventos, delta_ms)
            form_nivel_uno.draw(lista_eventos, delta_ms, teclas_presionadas)

    pygame.display.flip()




    


  



