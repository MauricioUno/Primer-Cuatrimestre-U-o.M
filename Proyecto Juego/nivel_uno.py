import pygame
import sys
from aux_constantes import *
from aux_sonidos import *
from aux_json import *
from class_plataforma import *
from class_texto import *

from enemy_groodle import *
from enemy_ix import *
from enemy_batterflies import *
from jugador import Jugador



def iniciar_nivel_uno(screen, clock):
    
    nivel_uno = importar_lista(r"Proyecto Juego\aux_niveles.json", "niveles")[0]
    pygame.display.set_caption('Nivel Uno: Bosque Verde')

    sonido_nivel_uno.play(-1)

    bosque_verde = Imagen( r"\locations\green forest\all.png", ANCHO_VENTANA, ALTO_VENTANA, 0, 0)
    pasto = Imagen(r"\locations\green forest\Ground.png", ANCHO_VENTANA, ALTO_VENTANA, 0, 0)

    
    medio_segundo = pygame.USEREVENT + 0
    pygame.time.set_timer(medio_segundo,500)


    plataformas = GrupoPlataformas(nivel_uno["plataformas"])
    groodle = SpiritGroodle(800, 270, IZQUIERDA)
    ix = SpiritIx(500, 490, DERECHA, 10, 200, 700)
    batterflies = GrupoBatterflies(3)
    jugador = Jugador(0,400,10)

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == medio_segundo:
                groodle.disparar(jugador.rect)
                batterflies.generar_batterfly()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jugador.saltar(True)

                if event.key == pygame.K_z:
                    jugador.disparar()

                if event.key == pygame.K_q:
                    jugador.recibir_golpe()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    jugador.detener()

                if event.key == pygame.K_SPACE:
                    jugador.saltar(False)

        
        teclas_presionadas = pygame.key.get_pressed()
        if True in teclas_presionadas:

            if teclas_presionadas[pygame.K_LEFT] and not teclas_presionadas[pygame.K_RIGHT] :
                jugador.mover(IZQUIERDA)

            elif teclas_presionadas[pygame.K_RIGHT] and not teclas_presionadas[pygame.K_LEFT] :
                jugador.mover(DERECHA)

            elif teclas_presionadas[pygame.K_RIGHT] and teclas_presionadas[pygame.K_LEFT]:
                jugador.detener()

            if teclas_presionadas[pygame.K_SPACE]:
                jugador.limitar_salto()
                    
                        


        bosque_verde.draw(screen)

        plataformas.actualizar_plataformas(screen)
        groodle.actualizar_groodle(screen, jugador)
        ix.actualizar_ix(screen)
        batterflies.actualizar_batterflies(screen,jugador)
        jugador.actualizar_player(screen, plataformas.lista, ix.rect)

        pasto.draw(screen)
        
        pygame.display.flip()
    
         







