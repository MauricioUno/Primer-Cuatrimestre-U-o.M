from constantes import *
import pygame
import sys

from player import Jugador
from batterfly import *
from coco_fantasma import *

pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption('Glitch is Dead, Long Live Glitch!')
imagen_fondo = pygame.image.load(r"Programas Pygame\CLASE_19_inicio_juego\images\locations\forest\all.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))


un_segundo = pygame.USEREVENT + 0
pygame.time.set_timer(un_segundo,1000)

jugador = Jugador(ANCHO_VENTANA/2,400,10)
batterflies = GrupoBatterflies(4)
coco = CocoFantasma(ANCHO_VENTANA-200, 400)

clock = pygame.time.Clock()
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == un_segundo:
            coco.disparar(jugador.rect)
            batterflies.generar_batterfly()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                jugador.detener()

            if event.key == pygame.K_SPACE:
                jugador.saltar(False)

    
    teclas_presionadas = pygame.key.get_pressed()
    if True in teclas_presionadas:
        if teclas_presionadas[pygame.K_LEFT] and not teclas_presionadas[pygame.K_RIGHT] :
            jugador.mover("izquierda")

        elif teclas_presionadas[pygame.K_RIGHT] and not teclas_presionadas[pygame.K_LEFT] :
            jugador.mover("derecha")

        elif teclas_presionadas[pygame.K_RIGHT] and teclas_presionadas[pygame.K_LEFT]:
            jugador.detener()

        if teclas_presionadas[pygame.K_SPACE]:
            jugador.saltar(True)
                  
                    


    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    coco.actualizar_coco_fantasma(screen, jugador.rect)
    batterflies.actualizar_batterflies(screen, jugador.rect)
    jugador.actualizar_player(screen)
    
    pygame.display.flip()
    
    



    






