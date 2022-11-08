import pygame
from aux_constantes import *

class Texto:
    def __init__(self, texto, tamaño_letra, ubicacion_x, ubicacion_y) -> None:
        self.fuente = pygame.font.Font(PATH_RECURSOS + r"\imagenes\Auxiliar\JingleBalonsGTDemo.ttf", tamaño_letra)
        self.texto = self.fuente.render(texto, True, COLOR_TEXTO_MENU)
        self.rect = self.texto.get_rect()
        self.rect.centerx = ubicacion_x
        self.rect.centery = ubicacion_y

    
    def draw(self, screen):
        screen.blit(self.texto, self.rect)


class TextoInteractivo(Texto):
    def __init__(self, texto, tamaño_letra, ubicacion_x, ubicacion_y) -> None:
        super().__init__(texto, tamaño_letra, ubicacion_x, ubicacion_y)
        self.rect_hitbox = pygame.Rect(ubicacion_x -self.rect.width/2, ubicacion_y - tamaño_letra/2, self.rect.width, tamaño_letra)


class Imagen:
    def __init__(self, path_imagen, ancho, alto, pos_x, pos_y) -> None:
        self.imagen = pygame.image.load(PATH_RECURSOS + path_imagen)
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect = self.imagen.get_rect(x = pos_x, y = pos_y)

    
    def draw(self, screen):
        screen.blit(self.imagen, self.rect)