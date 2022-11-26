import pygame
from pygame.locals import *
import sys
from aux_constantes import *
from gui_form_menu_nivel import FormMenuNiveles
from gui_form_menu_main import FormMenuMain
from gui_form_nivel import FormNivel
from gui_form_pausa import FormPausa
pygame.init()

flags = DOUBLEBUF 
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
clock = pygame.time.Clock()

form_main_menu = FormMenuMain(name="form_menu_main",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background =PATH_RECURSOS + r"\background\Escalando.jpg", color_border= None,active=True)
form_levels_menu = FormMenuNiveles(name="form_menu_niveles",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background= None, imagen_background =PATH_RECURSOS + r"\background\Space.jpg", color_border= None,active=False)
form_pausa = FormPausa(name= "form_pausa", master_surface=screen, x = 550, y=180, w=400, h=300, color_background=C_CELEST, color_border=C_WHITE, imagen_background= None, active=False)
form_nivel_uno = FormNivel(name="nivel_uno", master_surface= screen, x=0, y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA)
#form_nivel_dos = FormNivel(name="nivel_dos", master_surface=screen, x=0, y=0, w=ANCHO_VENTANA,h=ALTO_VENTANA)
while True:

    delta_ms = clock.tick(FPS)
    lista_eventos = pygame.event.get()
    teclas_presionadas = pygame.key.get_pressed()
    for event in lista_eventos:
        if event.type == pygame.QUIT:       
            pygame.quit()
            sys.exit() 

    if(form_main_menu.active):
        form_main_menu.update(lista_eventos)
        form_main_menu.draw(delta_ms)
        
    elif(form_levels_menu.active):
        form_levels_menu.update(lista_eventos)
        form_levels_menu.draw(delta_ms)

    elif(form_nivel_uno.active):
        form_nivel_uno.update(lista_eventos, delta_ms)
        form_nivel_uno.draw(lista_eventos, delta_ms, teclas_presionadas)

    # elif(form_nivel_dos.active):
    #      form_nivel_dos.update(lista_eventos, delta_ms)
    #      form_nivel_dos.draw(lista_eventos, delta_ms, teclas_presionadas)
            
    elif(form_pausa.active):
        form_pausa.update(lista_eventos)
        form_pausa.draw(delta_ms)
        
    pygame.display.flip()




    


  



