import pygame
from constantes import *
import tablero
from sonidos import *
import textos

pygame.init() #Se inicializa pygame
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA+100))
pygame.display.set_caption('The Simpsons Memotest')

segundo = pygame.USEREVENT + 0
pygame.time.set_timer(segundo,1000)

tiempo_de_inicio = pygame.USEREVENT + 1
pygame.time.set_timer(tiempo_de_inicio,3000)

tablero_juego = tablero.init()
tablero.mezclar_posicion_tarjetas(tablero_juego['l_tarjetas'])


imagen_fondo = pygame.image.load(PATH_RECURSOS + "\imagen_fondo.jpg")

sonido_fondo.play(-1)

segundos = 0
minutos = 0
textos_juego = textos.obtener_diccionario_textos(minutos,segundos)
running = True
juego_iniciado = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        
        if juego_iniciado:
            if event.type == pygame.MOUSEBUTTONDOWN :
                tablero.colicion(tablero_juego,event.pos)
            
            if not tablero.verificar_juego_terminado(tablero_juego["l_tarjetas"]):
                if event.type == segundo:
                    segundos += 1
                    if segundos == 60:
                        minutos += 1
                        segundos = 0
        
        else:
            if event.type == tiempo_de_inicio:
                juego_iniciado = True

            for tarjeta in tablero_juego['l_tarjetas']:
                tarjeta["visible"] = not juego_iniciado   
        
    tablero.update(tablero_juego)
    pantalla_juego.blit(imagen_fondo,(0,0))
    textos.actualizar_reloj(textos_juego, minutos, segundos)
    tablero.render(tablero_juego, pantalla_juego, textos_juego)

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()