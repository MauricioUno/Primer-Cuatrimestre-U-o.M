from constantes import *
from sonidos import *
from objetos import *

def render(tablero: Tablero, pantalla_juego, textos: Texto):
    
    for aux_tarjeta in tablero.lista_tarjetas:
        if(aux_tarjeta.visible):
            pantalla_juego.blit(aux_tarjeta.surface_imagen,aux_tarjeta.rect)
        else:
            pantalla_juego.blit(aux_tarjeta.surface_hide,aux_tarjeta.rect)

    pantalla_juego.blit(textos.tiempo, (0,450))

    if tablero.verificar_juego_terminado():
        tablero.cambiar_musica_ganador()
        pantalla_juego.blit(textos.juego_terminado, (0,500))


    


     