import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from aux_constantes import *
from gui_widget import Widget

class FormMenuMain(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)

        self.title = Widget(master_form = self, x = 500, y = 50, w = 500, h = 150, color_background=None, color_border= None, image_background= None, text="GLITCH", font= "Bauhaus 93", font_size=150, font_color=COLOR_TEXTO_MENU)
        self.boton3 = Button(master=self, x = 610, y = 300, w = 280, h = 100, color_background=None, color_border=None, on_click=self.on_click_boton1, on_click_param="form_menu_niveles",text="START",font="Bauhaus 93", font_size= 100, font_color=COLOR_TEXTO_MENU)
        self.boton4 = Button(master=self, x = 505, y = 410, w = 470, h = 100, color_background=None, color_border=None, on_click=print, on_click_param="opciones",text="OPCIONES",font="Bauhaus 93", font_size= 100, font_color=COLOR_TEXTO_MENU)
        self.boton5 = Button(master=self, x = 610, y = 520, w = 280, h = 100, color_background=None, color_border=None, on_click=print, on_click_param="salir",text="SALIR",font="Bauhaus 93", font_size= 100, font_color=COLOR_TEXTO_MENU)
        self.lista_widget = [self.boton3, self.boton4, self.boton5, self.title]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self, delta_ms): 
        super().draw(delta_ms)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()