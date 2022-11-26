from aux_constantes import *
from aux_frames import Auxiliar
import random
from class_proyectil import Proyectil

class Batterfly(Proyectil):
    def __init__(self, pos_x, pos_y, speed_x, speed_y, invertido, min_x, max_x, max_y, screen):
        self.fly= Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\enemies\batterfly\fly.png",8,5, invertido)
        super().__init__(self.fly, pos_x, pos_y, min_x, max_x, speed_x, 20, 10, 65, 60, 15, self, screen)

        self.vuelo = speed_y
        self.move_y = self.vuelo
        self.bajando = False
        self.maximo_y = max_y
        self.minimo_y = pos_y
        self.timer = 0
        self.vida = 1
        self.puntos = 50

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
    
    def recibir_golpe(self, proyectil):
        self.vida += -proyectil.damage
        if self.vida < 1:
            self.activo = False
            proyectil.master.score += self.puntos
        

    def actualizar(self, jugador, delta_ms):
        if self.activo:
            self.timer += delta_ms
            if self.timer > 30:
                self.timer = 0
                self.updatear_frames()
                self.controlar_vuelo()
                self.actualizar_posicion()
                self.verificar_limite_x()
                self.draw()
        



class GrupoBatterflies:
    def __init__(self, cantidad, screen) -> None:
        self.lista = []
        self.screen = screen
        self.cantidad = cantidad
        self.timer = 0
        self.spawn_allowed = True

    
    def generar_batterfly(self):
        if self.spawn_allowed:
            self.spawn_allowed = False
            if len(self.lista) < self.cantidad:
                self.agregar_batterflies(self.cantidad - len(self.lista))


    def actualizar_cooldown_spawn(self, delta_ms):
        if not self.spawn_allowed:
            self.timer += delta_ms
            if self.timer > 500:
                self.timer = 0
                self.spawn_allowed = True


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


            batterfly = Batterfly(pos_x, pos_y, speed_x, speed_y, inversion, -450, ANCHO_VENTANA + 450, limite_y, self.screen)
            self.lista.append(batterfly)


    def actualizar(self, jugador, delta_ms):
    
        for batterfly in self.lista:
            batterfly : Batterfly
            batterfly.actualizar(jugador, delta_ms)
            if not batterfly.activo:
                self.lista.remove(batterfly)
        
        self.generar_batterfly()
        self.actualizar_cooldown_spawn(delta_ms)
