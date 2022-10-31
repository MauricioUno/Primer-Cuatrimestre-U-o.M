import pygame
import sys
from constantes import *
from player import Player
from enemigo import *

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.init()
clock = pygame.time.Clock()

imagen_fondo = pygame.image.load(r"Programas Pygame\CLASE_19_inicio_juego\images\locations\forest\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(ANCHO_VENTANA/2,480,8)
murcielagos = GrupoBatterflies(5)
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_1.control("STAY")

            if event.key == pygame.K_SPACE:
                player_1.salto(False)


    teclas_presionadas = pygame.key.get_pressed()
    if True in teclas_presionadas:
        if teclas_presionadas[pygame.K_LEFT] and not teclas_presionadas[pygame.K_RIGHT] :
            player_1.control("WALK_L")

        elif teclas_presionadas[pygame.K_RIGHT] and not teclas_presionadas[pygame.K_LEFT] :
            player_1.control("WALK_R")

        elif teclas_presionadas[pygame.K_RIGHT] and teclas_presionadas[pygame.K_LEFT]:
            player_1.control("STAY")

        if teclas_presionadas[pygame.K_SPACE] and not player_1.saltando:
            player_1.salto(True)
        else:
            if pygame.time.get_ticks() - player_1.tiempo_saltando > 700 and player_1.tiempo_saltando > 0:
                player_1.salto(False)
                player_1.tiempo_saltando = 0



    

    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    player_1.update()
    player_1.draw(screen)
    murcielagos.updatear_murcielagos(screen, player_1.rect)
    
    pygame.display.flip()
    
    



    






