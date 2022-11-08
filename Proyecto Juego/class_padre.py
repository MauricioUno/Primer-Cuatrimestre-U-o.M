from aux_constantes import *
import pygame

class ObjetoAnimado:
    def __init__(self, animacion, pos_x, pos_y):
        self.animacion = animacion
        self.frame = 0
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect(x = pos_x, y = pos_y)


    def updatear_frames(self):
        if(self.frame < len(self.animacion) - 1):
            self.frame += 1 
        else: 
            self.frame = 0


    def draw(self,screen):
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen,self.rect)




class ProyectilAnimado(ObjetoAnimado):
    def __init__(self, animacion, pos_x, pos_y, minimo, maximo, velocidad, aux_x, aux_y, ancho, alto):
        self.proyectil = animacion
        self.min_x = minimo
        self.max_x = maximo
        self.move_x = velocidad
        self.activo = True
        super().__init__(self.proyectil, pos_x, pos_y)
        self.rect_hitbox = pygame.Rect(pos_x + aux_x, pos_y +aux_y , ancho, alto)


    def verificar_fin(self, objetivo):
        if self.verificar_colision(objetivo) or self.verificar_limite_x():
            self.activo = False

    
    def verificar_colision(self,objetivo):        
        return self.rect_hitbox.colliderect(objetivo)


    def verificar_limite_x(self):
        return not (self.min_x < self.rect_hitbox.x and self.rect_hitbox.x < self.max_x) 




class DisparoHorizontal(ProyectilAnimado):

    def __init__(self, pos_x, pos_y, velocidad, aux_x, aux_y, ancho, alto, animacion) -> None:
        self.proyectil = animacion
        super().__init__(self.proyectil, pos_x, pos_y, -100, ANCHO_VENTANA + 100, velocidad, aux_x, aux_y, ancho, alto)


    def actualizar_posicion(self):
        self.rect.x += self.move_x
        self.rect_hitbox.x += self.move_x

    def actualizar_proyectil(self, screen, objetivo):
        self.updatear_frames()
        self.actualizar_posicion()
        self.verificar_fin(objetivo)
        self.draw(screen)

