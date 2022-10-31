from constantes import *
from auxiliar import Auxiliar
import pygame

class Player:
    def __init__(self,x,y,speed_walk) -> None:
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "\caracters\stink\idle.png",16,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "\caracters\stink\idle.png",16,1,True)
        
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "\caracters\stink\walk.png",15,1)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(PATH_IMAGE + "\caracters\stink\walk.png",15,1,True)[:12]

        self.jump_r = 1
        self.jump_l = 2        
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk

        self.direccion = "derecha"
        self.animation = self.stay_r
        self.animacion_anterior = self.stay_r

        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.saltando = False
        self.speed_jump = 8
        self.tiempo_saltando = 0


    def control(self,action):

        if(action == "WALK_R"):
            self.move_x = self.speed_walk
            self.animation = self.walk_r
            self.direccion = "derecha"
            
        elif(action == "WALK_L"):
            self.move_x = -self.speed_walk
            self.animation = self.walk_l
            self.direccion = "izquierda"
            
        elif(action == "STAY"):
            if self.direccion == "derecha":
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0


        if self.animation != self.animacion_anterior:
            self.animacion_anterior = self.animation
            self.frame = 0


    def salto(self, saltar):

        if saltar and self.rect.y == 480:
            self.move_y = -self.speed_jump
            self.saltando = True
            self.tiempo_saltando = pygame.time.get_ticks()
        elif not saltar:
            self.saltando = False

        if self.saltando:
            if self.direccion == "derecha":
                pass
            elif self.direccion == "izquierda":
                pass


    def update(self):
        if(self.frame < len(self.animation) - 1):
            self.frame += 1 
        else: 
            self.frame = 0

        self.rect.x += self.move_x
        self.rect.y += self.move_y

        if not self.saltando and self.rect.y < 480:
            self.move_y = self.speed_jump
            
        elif self.rect.y >= 480:
            self.rect.y = 480
            self.move_y = 0
        
    
    def draw(self,screen):
        #pygame.draw.rect(screen,(0,0,0),self.rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        


