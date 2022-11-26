import pygame
from pygame.locals import *
from aux_constantes import *
from aux_json import *
from gui_form import Form

from class_A import Imagen
from class_plataforma import ListaPlataformas
from class_item import ListaItems

from enemy_lista import ListaEnemigos
from jugador import Jugador
from class_portal import Portal


class FormNivel(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background=None, imagen_background=None, color_border=None, active=False):
        data_nivel = importar_lista("Proyecto Juego Version 2/{0}.json".format(name), name)[0]
        imagen_background = PATH_RECURSOS + data_nivel["background"]
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)
        self.name = name
        self.plataformas = ListaPlataformas(data_nivel["plataformas"], master_surface, name)
        self.items = ListaItems(data_nivel["items"], master_surface)
        self.enemigos = ListaEnemigos(data_nivel["enemigos"], master_surface)
        self.jugador = Jugador(data_nivel["pos_player"][0], data_nivel["pos_player"][1], master_surface, self)
        self.portal = Portal(data_nivel["pos_portal"][0], data_nivel["pos_portal"][1], master_surface)
        
        
        

    def update(self, lista_eventos, delta_ms):
        self.forms_dict["form_pausa"].cambiar_nivel(self.name)
        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.set_active("form_pausa")

                if event.key == pygame.K_x:
                    if self.jugador.is_on_portal:
                        print("nivel_terminado")



    def draw(self, lista_eventos, delta_ms, teclas_presionadas):
        super().draw(delta_ms)
        self.plataformas.actualizar(delta_ms)
        self.items.actualizar(delta_ms, [self.jugador])
        self.enemigos.actualizar(self.jugador, delta_ms)
        self.jugador.actualizar(self.plataformas.lista, self.enemigos.lista, delta_ms, lista_eventos, teclas_presionadas)
        self.portal.actualizar([self.jugador], delta_ms)
        