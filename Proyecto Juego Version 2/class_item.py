import pygame
import re
from aux_constantes import *
from class_A import *

class Item(Imagen):
    def __init__(self, tipo, ancho, alto, pos_x, pos_y, reaparicion, cooldown, efecto, screen) -> None:
        super().__init__("/items/{0}.png".format(tipo), ancho, alto, pos_x, pos_y, screen)
        self.activo = True
        self.timer = 0
        self.reaparicion = reaparicion
        self.cooldown = cooldown
        self.efecto = efecto

    def verificar_colision(self, objetivos):
        for objetivo in objetivos:
            if self.rect.colliderect(objetivo.rect_hitbox):
                self.activo = False
                self.aplicar_efecto(objetivo)

    
    def aplicar_efecto(self, objetivo):
        if re.search("recarga", self.efecto, re.IGNORECASE):
            objetivo.municion += 5
        
        elif re.search("score", self.efecto, re.IGNORECASE):
            objetivo.score += 100
        
        elif re.search("curacion", self.efecto, re.IGNORECASE):
            objetivo.vida += 30
        

    def actualizar_cooldown_reaparicion(self, delta_ms):
        if not self.activo:
            self.timer += delta_ms
            if self.timer > self.cooldown:
                self.timer = 0
                self.activo = True
    
    def actualizar(self, delta_ms, objetivos):
        if self.reaparicion:
            self.actualizar_cooldown_reaparicion(delta_ms)
        if self.activo:
            self.timer += delta_ms
            if self.timer > 30:
                self.timer = 0
                self.verificar_colision(objetivos)
                self.draw()



class ListaItems:
    def __init__(self, lista_items, screen) -> None:
        self.lista = []
        self.screen = screen
        if "recarga" in lista_items.keys():
            self.agregar_item(lista_items["recarga"], "recarga")

        
        if "score" in lista_items.keys():
            self.agregar_item(lista_items["score"], "score")


    def agregar_item(self, lista_items, efecto):
        for item in lista_items:
            aux_item = Item(item["item"], item["dimension"][0], item["dimension"][1], item["coordenadas"][0], item["coordenadas"][1], False, 0, efecto, self.screen)
            self.lista.append(aux_item)


    def actualizar(self, delta_ms, objetivos):
        for item in self.lista:
            item.actualizar(delta_ms, objetivos)
            if not item.reaparicion and not item.activo:
                self.lista.remove(item)