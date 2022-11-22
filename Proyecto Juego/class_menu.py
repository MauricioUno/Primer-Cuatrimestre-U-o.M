from class_texto import *
from aux_constantes import *

class Menu:
    def __init__(self, textos, textos_interactivos, imagenes, screen) -> None:
        self.textos = []
        self.textos_interactivos = []
        self.imagenes = []
        self.screen = screen
        self.agregar_texto(textos)
        self.agregar_texto_interactivo(textos_interactivos)
        self.agregar_imagen(imagenes)

    def agregar_texto(self, textos):
        for texto in textos:
            escrito = Texto(texto["texto"], texto["tam"], texto["pos_x"], texto["pos_y"])
            self.textos.append(escrito)

    def agregar_texto_interactivo(self, texto_interactivo):
        for texto in texto_interactivo:
            escrito = TextoInteractivo(texto["texto"], texto["tam"], texto["pos_x"], texto["pos_y"])
            self.textos_interactivos.append(escrito)

    def agregar_imagen(self, imagenes):
        for imagen in imagenes:
            aux_imagen = Imagen(imagen["path"], imagen["ancho"], imagen["alto"], imagen["pos_x"], imagen["pos_y"], self.screen)
            self.imagenes.append(aux_imagen)

    def update(self, screen):
        for texto in self.textos:
            texto.draw(screen)
        
        for texto_interc in self.textos_interactivos:
            texto_interc.draw(screen)

        for imagen in self.imagenes:
            imagen.draw()
