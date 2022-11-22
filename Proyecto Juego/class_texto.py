import pygame
from aux_constantes import *

class Texto:
    def __init__(self, texto, tamaño_letra, ubicacion_x, ubicacion_y) -> None:
        self.fuente = pygame.font.Font(PATH_RECURSOS + r"\imagenes\Auxiliar\JingleBalonsGTDemo.ttf", tamaño_letra)
        self.texto = self.fuente.render(texto, True, COLOR_TEXTO_MENU)
        self.rect = self.texto.get_rect(center = (ubicacion_x, ubicacion_y))
        

    def draw(self, screen):
        screen.blit(self.texto, self.rect)


class TextoInteractivo(Texto):
    def __init__(self, texto, tamaño_letra, ubicacion_x, ubicacion_y) -> None:
        super().__init__(texto, tamaño_letra, ubicacion_x, ubicacion_y)
        self.rect_hitbox = pygame.Rect(self.rect.centerx -self.rect.width/2, self.rect.centery - tamaño_letra/2, self.rect.width, tamaño_letra)



class Imagen:
    def __init__(self, path_imagen, ancho, alto, pos_x, pos_y, screen) -> None:
        self.imagen = pygame.image.load(PATH_RECURSOS + path_imagen).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto)).convert_alpha()
        self.rect = self.imagen.get_rect(x = pos_x, y = pos_y)
        self.screen = screen

    
    def draw(self):
        self.screen.blit(self.imagen, self.rect)