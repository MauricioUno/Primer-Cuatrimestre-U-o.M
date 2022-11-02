from constantes import *
from auxiliar import Auxiliar
import random
import pygame

class Batterfly:
    def __init__(self, x, y, speed_x, speed_y, invertido, maximo_x, maximo_y) -> None:

        self.invertido = invertido
        self.fly= Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + r"\inhabitants\batterfly\fly.png",8,5, self.invertido)
        self.frame = 0
        self.move_x = speed_x
        self.move_y = speed_y
        self.animacion = self.fly

        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_pos = pygame.Rect(x+20,y+10, 75, 70)
        
        self.vivo = True
        self.bajando = False
        self.maximo_x = maximo_x
        self.maximo_y = maximo_y
        self.minimo_y = y


    def controlar_vuelo(self):
        if self.bajando:
            if self.rect.y < self.minimo_y:
                self.move_y = abs(self.move_y)
            else:
                self.bajando = False        
        else:
            if self.rect.y > self.maximo_y:
                self.move_y = -abs(self.move_y)
            else:
                self.bajando = True



    def verificar_muerte(self, rect_jugador):
        if self.rect_pos.colliderect(rect_jugador) or self.verificar_limite_x():
            self.vivo = False


    def verificar_limite_x(self):
        limite_alcanzado = False

        if not self.invertido:
            if self.rect.x > self.maximo_x:
                limite_alcanzado = True        
        else:
            if self.rect.x < self.maximo_x:
                limite_alcanzado = True

        return limite_alcanzado


    def actualizar_posicion(self):
        self.rect.x += self.move_x
        self.rect_pos.x += self.move_x
        self.rect.y += self.move_y
        self.rect_pos.y += self.move_y


    def update(self):
        if(self.frame < len(self.animacion) - 1):
            self.frame += 1 
        else: 
            self.frame = 0


    def draw(self,screen):
        #pygame.draw.rect(screen,(0,0,0),self.rect_pos)
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen,self.rect)


    def actualizar_batterfly(self, screen, rect_jugador):
        self.update()
        self.controlar_vuelo()
        self.actualizar_posicion()
        self.verificar_muerte(rect_jugador)
        self.draw(screen)



class GrupoBatterflies:
    def __init__(self, cantidad) -> None:
        self.lista_batterflies = []
        self.cantidad = cantidad
    
    def generar_batterfly(self):
        if len(self.lista_batterflies) < self.cantidad:
            self.agregar_batterflies(self.cantidad - len(self.lista_batterflies))


    def agregar_batterflies(self, cantidad):
        for i in range(cantidad):
            valores = valores_batterfly()
            batterfly = Batterfly(valores["pos_x"], valores["pos_y"], valores["velocidad_x"], valores["velocidad_y"], valores["inversion"], valores["limite_x"], valores["limite_y"])
            self.lista_batterflies.append(batterfly)

    def actualizar_batterflies(self,screen, rect_jugador):
        for batterfly in self.lista_batterflies:
            batterfly.actualizar_batterfly(screen, rect_jugador)
            if not batterfly.vivo:
                self.lista_batterflies.remove(batterfly)
            
        
        
def valores_batterfly():
    datos_batterfly = {}

    datos_batterfly["pos_y"] = random.randrange(0, ALTO_VENTANA - ALTO_VENTANA/3, 20)
    datos_batterfly["velocidad_x"] = random.randrange(5, 10)
    datos_batterfly["velocidad_y"] = random.randrange(5, 10)
    datos_batterfly["limite_y"] = datos_batterfly["pos_y"] - random.randrange(100,300,10)

    if random.randint(0,1) == 1:
        datos_batterfly["inversion"] = True
        datos_batterfly["velocidad_x"] *= -1
        datos_batterfly["pos_x"] = random.randrange(ANCHO_VENTANA + 100, ANCHO_VENTANA + ANCHO_VENTANA/2, 20)
        datos_batterfly["limite_x"] = -100
    else:
        datos_batterfly["inversion"] = False
        datos_batterfly["pos_x"] = random.randrange(-ANCHO_VENTANA/2, -100, 20)
        datos_batterfly["limite_x"] = ANCHO_VENTANA + 100

    return datos_batterfly

