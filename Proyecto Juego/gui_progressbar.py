import pygame
from pygame.locals import *
from gui_widget import Widget
from aux_constantes import *


class ProgressBar(Widget):
    def __init__(self,master,x=0,y=0,w=200,h=50,color_background=C_GREEN,color_border=C_RED,image_background=None, value_max = 1):
        super().__init__(master,x,y,w,h,color_background,color_border,image_background,None,None,None,None)
        
        self.barra_vida = pygame.Rect(0,0,w,h)
        self.value_min = 0
        self.value_max = value_max
        self.value = self.value_max
        self.render()
        
    def render(self):
        super().render()
        self.barra_vida.w = self.value * self.w / self.value_max
        self.slave_surface.fill(C_GREEN_2, self.barra_vida)
        if self.color_border:
            pygame.draw.rect(self.slave_surface, self.color_border, self.slave_surface.get_rect(), 2)
        

    def update(self, lista_eventos):
        self.render()
    

