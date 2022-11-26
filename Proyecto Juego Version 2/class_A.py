from aux_constantes import *
import pygame

class ObjetoAnimado:
    def __init__(self, animacion, pos_x, pos_y, screen):
        self.screen = screen
        self.animacion = animacion
        self.frame = 0
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect(x = pos_x, y = pos_y)


    def updatear_frames(self):
        if(self.frame < len(self.animacion) - 1):
            self.frame += 1 
        else: 
            self.frame = 0


    def draw(self):
        self.imagen = self.animacion[self.frame]
        self.screen.blit(self.imagen,self.rect)



class Imagen:
    def __init__(self, path_imagen, ancho, alto, pos_x, pos_y, screen) -> None:
        self.imagen = pygame.image.load(PATH_RECURSOS + path_imagen).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto)).convert_alpha()
        self.rect = self.imagen.get_rect(x = pos_x, y = pos_y)
        self.screen = screen

    
    def draw(self):
        self.screen.blit(self.imagen, self.rect)



class EnemyGuard(ObjetoAnimado):
    def __init__(self, animacion, pos_x, pos_y, velocidad, min_x, max_x, direccion, damage, vida, puntos, screen):
        super().__init__(animacion, pos_x, pos_y, screen)
        self.velocidad = velocidad
        self.move_x = self.velocidad
        self.maximo_x = max_x
        self.minimo_x = min_x
        self.activo = True
        self.avanzando = True
        self.direccion = direccion
        self.damage = damage
        self.vida = vida
        self.puntos = puntos


    def recibir_golpe(self,proyectil):
        self.vida += -proyectil.damage
        if self.vida < 1:
            self.activo = False
            proyectil.master.score += self.puntos


    def controlar_ruta(self):
        if self.avanzando:
            if self.rect.x > self.minimo_x:
                self.move_x = -self.velocidad
                self.direccion = IZQUIERDA
            else:
                self.avanzando = False        
        else:
            if self.rect.x < self.maximo_x:
                self.move_x = self.velocidad
                self.direccion = DERECHA
            else:
                self.avanzando = True

   
    def actualizar_posicion(self):
        self.rect.x += self.move_x


