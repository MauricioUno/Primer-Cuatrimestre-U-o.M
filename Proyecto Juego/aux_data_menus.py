from aux_constantes import *
from class_texto import *


textos_main = [
    {
        "texto": "GLITCH",
        "tam": int(ALTO_VENTANA * 0.25),
        "pos_x": (ANCHO_VENTANA/2),
        "pos_y": ALTO_VENTANA/2 - int(ALTO_VENTANA * 0.25)
    }
]

textos_int_main = [
    {
        "texto": "START",
        "tam": int(ALTO_VENTANA * 0.25/2),
        "pos_x": (ANCHO_VENTANA/2),
        "pos_y": (ALTO_VENTANA/2)
    },

    {
        "texto": "OPCIONES",
        "tam": int(ALTO_VENTANA * 0.25/2),
        "pos_x": (ANCHO_VENTANA/2),
        "pos_y": (ALTO_VENTANA/2 + int(ALTO_VENTANA * 0.25/2 + ALTO_VENTANA * 0.03))
    },

    {
        "texto": "SALIR",
        "tam": int(ALTO_VENTANA * 0.25/2),
        "pos_x": (ANCHO_VENTANA/2),
        "pos_y": (ALTO_VENTANA/2 + int(ALTO_VENTANA * 0.25 + ALTO_VENTANA * 0.06))
    }
]

############################

textos_start = [
    {
        "texto": "NIVELES",
        "tam": int(ALTO_VENTANA * 0.25/2),
        "pos_x": int(ANCHO_VENTANA * 0.15),
        "pos_y": int(ALTO_VENTANA * 0.25/3)
    }
]

textos_int_start = [

    {
        "texto": "atras",
        "tam": int(ALTO_VENTANA * 0.25/3),
        "pos_x": ANCHO_VENTANA -60,
        "pos_y": ALTO_VENTANA - int(ALTO_VENTANA * 0.25/6)
    }
]

imagenes_start = [
    {
        "path": r"\locations\green forest\all.png",
        "ancho": ANCHO_VENTANA/2,
        "alto": ALTO_VENTANA/4,
        "pos_x": 20,
        "pos_y": int(ALTO_VENTANA * 0.25/1.5),
    },

    {
        "path": r"\locations\desert\all.png",
        "ancho": ANCHO_VENTANA/2,
        "alto": ALTO_VENTANA/4,
        "pos_x": 20,
        "pos_y": int(ALTO_VENTANA * 0.25/1.5) + ALTO_VENTANA/4 + 10,
    },

    {
        "path": r"\locations\red forest\all.png",
        "ancho": ANCHO_VENTANA/2,
        "alto": ALTO_VENTANA/4,
        "pos_x": 20,
        "pos_y": int(ALTO_VENTANA * 0.25/1.5) + ALTO_VENTANA/2 + 20,
    }
]
