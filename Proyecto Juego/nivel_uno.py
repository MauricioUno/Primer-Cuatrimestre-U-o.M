import pygame
import sys
from aux_constantes import *
from aux_sonidos import *
from aux_json import *
from class_plataforma import GrupoPlataformas
from class_texto import Imagen

from enemy_lista import ListaEnemiesNivelUno
from jugador import Jugador




def iniciar_nivel_uno(screen, clock):
    
    nivel_uno = importar_lista(r"Proyecto Juego\aux_niveles.json", "niveles")[0]
    pygame.display.set_caption('Nivel Uno: Bosque Verde')

    sonido_nivel_uno.play(-1)

    bosque_verde = Imagen( r"\locations\green forest\all.png", ANCHO_VENTANA, ALTO_VENTANA, 0, 0, screen)
    pasto = Imagen(r"\locations\green forest\Ground.png", ANCHO_VENTANA, ALTO_VENTANA, 0, 0, screen)

    plataformas = GrupoPlataformas(nivel_uno["plataformas"], screen)
    enemigos = ListaEnemiesNivelUno(screen)
    jugador = Jugador(0,400,screen)
    
    while True:

        delta_ms = clock.tick(FPS)
        lista_eventos = pygame.event.get()
        teclas_presionadas = pygame.key.get_pressed()
        
        for event in lista_eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        bosque_verde.draw()
        plataformas.actualizar(delta_ms)
        enemigos.actualizar(jugador, delta_ms)
        jugador.actualizar(plataformas.lista, enemigos.lista, delta_ms, lista_eventos, teclas_presionadas)
        pasto.draw()
        
        pygame.display.flip()
    
         







