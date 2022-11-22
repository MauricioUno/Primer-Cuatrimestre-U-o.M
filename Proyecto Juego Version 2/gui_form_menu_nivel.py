import pygame
from pygame.locals import *
from aux_constantes import *
from gui_form import Form
from gui_button import Button


class FormMenuNiveles(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active)

        self.boton1 = Button(master=self,x=20,y=20,w=500,h=180,color_background=None,color_border=None,image_background=PATH_RECURSOS + r"\locations\green forest\all.png",on_click=self.on_click_boton,on_click_param="form_nivel_uno",text="Green Forest",font="Bauhaus 93",font_size=25,font_color=C_BROWN)
        self.boton2 = Button(master=self,x=20,y=220,w=500,h=180,color_background=None,color_border=None,image_background=PATH_RECURSOS + r"\locations\desert\all.png",on_click=print,on_click_param="Nivel Dos",text="Desert",font="Bauhaus 93",font_size=25,font_color=C_YELLOW_2)
        self.boton3 = Button(master=self,x=20,y=420,w=500,h=180,color_background=None,color_border=None,image_background=PATH_RECURSOS + r"\locations\red forest\all.png",on_click=print,on_click_param="Nivel Tres",text="Red Forest",font="Bauhaus 93",font_size=25,font_color=C_BLACK)
        self.boton4 = Button(master=self,x=20, y=670, w=120,h =50,color_background=None,color_border=None,image_background=None, on_click=self.on_click_boton, on_click_param="form_menu_B",text="atras",font="Bauhaus 93", font_size= 50, font_color=COLOR_TEXTO_MENU) 
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4]

    def on_click_boton(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self, delta_ms): 
        super().draw(delta_ms)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()