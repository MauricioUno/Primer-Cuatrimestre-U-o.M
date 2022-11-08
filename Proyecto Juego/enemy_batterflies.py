from aux_constantes import *
from aux_frames import Auxiliar
import random
from class_padre import *

class Batterfly(ProyectilAnimado):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, invertido, min_x, max_x, max_y):
        self.fly= Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\inhabitants\batterfly\fly.png",8,5, invertido)
        super().__init__(self.fly, pos_x, pos_y, min_x, max_x, speed_x, 20, 10, 65, 60)

        self.vuelo = speed_y
        self.move_y = self.vuelo
        self.bajando = False
        self.maximo_y = max_y
        self.minimo_y = pos_y


    def controlar_vuelo(self):
        if self.bajando:
            if self.rect.y < self.minimo_y:
                self.move_y = self.vuelo
            else:
                self.bajando = False        
        else:
            if self.rect.y > self.maximo_y:
                self.move_y = -self.vuelo
            else:
                self.bajando = True


    def actualizar_posicion(self):
        self.rect.x += self.move_x
        self.rect_hitbox.x += self.move_x
        self.rect.y += self.move_y
        self.rect_hitbox.y += self.move_y

    def actualizar_batterfly(self, screen, rect_jugador):
        self.updatear_frames()
        self.controlar_vuelo()
        self.actualizar_posicion()
        self.verificar_fin(rect_jugador)
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
            pos_y = random.randrange(0, ALTO_VENTANA - ALTO_VENTANA/3, 20)
            speed_x = random.randrange(6, 11)
            speed_y = random.randrange(6, 11)
            limite_y = pos_y - random.randrange(100,300,10)

            if random.randint(0,1) == 1:
                inversion = True
                speed_x *= -1
                pos_x = random.randrange(ANCHO_VENTANA + 100, ANCHO_VENTANA + ANCHO_VENTANA/4, 20)
            else:
                inversion = False
                pos_x = random.randrange(-ANCHO_VENTANA/4, -100, 20)


            batterfly = Batterfly(pos_x, pos_y, speed_x, speed_y, inversion, -450, ANCHO_VENTANA + 450, limite_y)
            self.lista_batterflies.append(batterfly)


    def actualizar_batterflies(self,screen, rect_jugador):
        for batterfly in self.lista_batterflies:
            batterfly : Batterfly
        
            batterfly.actualizar_batterfly(screen, rect_jugador)
            if not batterfly.activo:
                self.lista_batterflies.remove(batterfly)
            
        
