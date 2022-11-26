from aux_constantes import *
from gui_form import *
from gui_button import *

class FormPausa(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.boton = Button(master=self, x = w/2-110 , y = y/4, w = 220, h = 50, color_background=None, color_border=None, on_click=self.on_click_boton, on_click_param=None,text="Reanudar",font="Bauhaus 93", font_size= 50, font_color=(240,230,140))
        self.lista_widget = [self.boton]


    def on_click_boton(self, parametro):
        self.set_active(parametro)


    def cambiar_nivel(self, parametro):
        self.boton.on_click_param = parametro

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self, delta_ms): 
        super().draw(delta_ms)
        for aux_boton in self.lista_widget:    
            aux_boton.draw()