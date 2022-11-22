import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_progressbar import ProgressBar
from gui_widget import Widget

from aux_json import *
from class_plataforma import GrupoPlataformas
from enemy_lista import ListaEnemiesNivelUno
from jugador import Jugador

class FormNivelUno(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        nivel_uno = importar_lista(r"Proyecto Juego\aux_niveles.json", "niveles")[0]
        pygame.display.set_caption('Nivel Uno: Bosque Verde')
        self.plataformas = GrupoPlataformas(nivel_uno["plataformas"], master_surface)
        self.enemigos = ListaEnemiesNivelUno(master_surface)
        self.jugador = Jugador(0,400,master_surface)
        self.layer_orb = Widget(master_form=self, x=10, y = 40, w=25, h=25, color_background= None, color_border=None, image_background=r"Proyecto Juego\recursos\caracters\stink\disparo_item.png",text = None,font=None,font_size=None,font_color=None)
        self.layer_ammo = Widget(master_form=self, x=50, y = 40, w=50, h=25, color_background= C_CELEST, color_border=C_BLUE, image_background=None,text=" ",font="Arial",font_size=25,font_color=C_BLUE_2)
        self.layer_score = Widget(master_form=self, x=1090, y = 10, w=100, h=30, color_background=C_YELLOW_2, color_border=C_BROWN, image_background=None, text=" ", font="Arial", font_size=30, font_color=C_BLACK)
        self.pb1 = ProgressBar(master=self,x=10,y=10,w=350,h=20,color_background=M_BRIGHT_CLICK,color_border=C_WHITE, value_max = 100)
        self.lista_widget = [self.pb1, self.layer_orb, self.layer_ammo,self.layer_score]


    def update(self, lista_eventos, delta_ms):
        
        self.pb1.value = self.jugador.vida
        self.layer_ammo.text = "{0}".format(self.jugador.municion)
        self.layer_score.text = "{0}".format(self.jugador.score)
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
            


    def draw(self, lista_eventos, delta_ms, teclas_presionadas):
        super().draw(delta_ms)
        
        self.plataformas.actualizar(delta_ms)
        self.enemigos.actualizar(self.jugador, delta_ms)
        self.jugador.actualizar(self.plataformas.lista, self.enemigos.lista, delta_ms, lista_eventos, teclas_presionadas)
        for aux_widget in self.lista_widget:
            aux_widget.draw()