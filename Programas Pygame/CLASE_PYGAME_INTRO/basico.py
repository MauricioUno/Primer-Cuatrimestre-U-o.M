import pygame
import colores
import dona
import personaje
import score

ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("PYGAME HOMERO COME DONAS")

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

player = personaje.crear(ANCHO_VENTANA/2,ALTO_VENTANA-200,200,200)
lista_donas = dona.crear_lista_donas(20)

flag_run = True
while flag_run:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_run = False

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                dona.update(lista_donas, player)

    lista_teclas = pygame.key.get_pressed()
    if True in lista_teclas:
        if lista_teclas[pygame.K_LEFT] :
            personaje.update(player,-5)
        if lista_teclas[pygame.K_RIGHT] :
            personaje.update(player,5)

    score.aumentar_velocidad_donas(player,lista_donas)
    ventana_ppal.fill(colores.NEGRO)
    personaje.actualizar_pantalla(player,ventana_ppal)
    dona.actualizar_pantalla(lista_donas,ventana_ppal)
    score.actualizar_pantalla(player, ventana_ppal)

    pygame.display.flip()
pygame.quit()