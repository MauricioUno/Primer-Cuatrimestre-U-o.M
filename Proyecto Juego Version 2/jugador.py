from aux_constantes import *
from aux_frames import Auxiliar
from class_padre import GrupoDisparosX
import pygame
from gui_progressbar import ProgressBar
from gui_widget import Widget

class Jugador:
    def __init__(self, pos_x, pos_y, screen) -> None:
        self.screen = screen
        self.direccion = DERECHA
        self.stay = {}
        self.stay[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\idle_plus.png",26,2)[:51]
        self.stay[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\idle_plus.png",26,2,True)[:51]
        
        self.walk = {}
        self.walk[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\walk.png",15,1)[:12]
        self.walk[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\walk.png",15,1,True)[:12]

        self.jump = {}
        self.jump[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1)[:23]
        self.jump[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1, True)[:23]

        self.fall = {}
        self.fall[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1)[22:28]
        self.fall[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + "\caracters\stink\jump.png", 33, 1, True)[22:28]
        
        
        self.animacion = self.stay[self.direccion]
        self.frame = 0
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect(x = pos_x, y = pos_y)
        self.rect_pies = pygame.Rect(self.rect.x + self.rect.w/3, self.rect.y + self.rect.h -10, self.rect.w/3, 5)
        self.rect_hitbox = pygame.Rect(self.rect.x + 20, self.rect.y + 10, self.rect.w - 30, self.rect.h - 15)
        self.move_x = 0
        self.move_y = 0

        self.speed_walk = {}
        self.speed_walk[DERECHA] = 10
        self.speed_walk[IZQUIERDA] = -10

        self.sobre_plataforma = True
        self.caminando = False
        self.saltando = False
        self.cayendo = False

        self.speed_jump = 10
        self.gravedad = 10
        self.inicio_salto = self.rect_pies.y


        self.speed_shoot = {}
        self.speed_shoot[DERECHA] = 20
        self.speed_shoot[IZQUIERDA] = -20
        self.orb = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\caracters\stink\disparo_animacion.png",16,2)[:31]
        self.municion = 30
        self.proyectiles = GrupoDisparosX(self, self.screen)
        self.timer_disparo = 0
        self.shoot_allowed = True


        self.invulnerable = False
        self.golpeado = False
        self.hitted = {}
        self.hitted[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\caracters\stink\surprise.png",21,1)[:13]
        self.hitted[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS + r"\caracters\stink\surprise.png",21,1, True)[:13]
        self.timer_invulnerable = 0
        self.timer = 0

        self.vida = 100
        self.vivo = True
        self.death = {}
        self.death[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS +  r"\caracters\stink\angry.png",20,1,False, repeat_frame=2)[8:26]
        self.death[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(PATH_RECURSOS +  r"\caracters\stink\angry.png",20,1,True,repeat_frame=2)[8:26]
        self.activo = True
        self.score = 0


    def mover(self,direccion):
        if not self.golpeado:
            self.direccion = direccion
            self.caminando = True
            self.move_x = self.speed_walk[self.direccion]
            
            
    def detener(self):
        if not self.golpeado:
            self.caminando = False
            self.move_x = 0


    def saltar(self, saltar):
        if not self.golpeado:
            if saltar:
                if self.sobre_plataforma:
                    self.saltando = True
                    self.move_x = 0
                    self.move_y = -self.speed_jump
                    self.inicio_salto = self.rect_pies.y
            else:
                self.saltando = False


    def limitar_salto(self):
        if self.rect_pies.y < self.inicio_salto - 150:
            self.saltando = False


    def verificar_plataforma(self, plataformas):
        if not self.saltando and not self.golpeado:
            self.sobre_plataforma = False
            for plataforma in plataformas:
                if self.rect_pies.colliderect(plataforma.rect_piso):

                    if self.caminando:
                        self.move_x = self.speed_walk[self.direccion] + plataforma.move_x
                    else:
                        self.move_x = plataforma.move_x
                    self.sobre_plataforma = True
                    break
            


    def aplicar_gravedad(self):
        if not self.golpeado and not self.saltando:
            if not self.sobre_plataforma:
                self.move_y = self.gravedad
                self.cayendo = True
            else:
                self.move_y = 0
                self.cayendo = False


    def disparar(self):
        if self.municion > 0 and not self.golpeado and self.shoot_allowed:
            self.shoot_allowed = False  
            self.proyectiles.agregar_disparo(self.rect.centerx, self.rect.centery, self.speed_shoot[self.direccion], 0, 0, 30, 30, self.orb, 10)
            self.municion -= 1

    def cooldown_disparo(self, delta_ms):
        if not self.shoot_allowed:
            self.timer_disparo += delta_ms
            if self.timer_disparo > 200:
                self.timer_disparo = 0
                self.shoot_allowed = True


    def recibir_golpe(self, atacante):
        if not self.invulnerable:
            self.modificar_vida(atacante)
            self.golpeado = True
            self.invulnerable = True
            self.saltando = False
            
            self.move_x = -self.speed_walk[self.direccion] / 2
            self.move_y = -2
            
            
    def modificar_vida(self,atacante):
        self.vida += -atacante.damage
        if self.vida < 1:
            self.vivo = False


    def cooldown_invulnerabilidad(self, delta_ms):
        if self.invulnerable:
            self.timer_invulnerable += delta_ms
            if self.timer_invulnerable > 1000:
                self.timer_invulnerable = 0
                self.invulnerable = False


    def verificar_colision_enemigos(self,enemigos):
        for enemigo in enemigos:
            if self.rect_hitbox.colliderect(enemigo.rect_hitbox):
                self.recibir_golpe(enemigo)



    def animaciones(self):
        if self.vivo:
            if not self.golpeado:
                if self.saltando:
                    self.cambiar_animacion(self.jump)
                else:
                    if self.cayendo:
                        self.cambiar_animacion(self.fall)
                    else:
                        if self.caminando:
                            self.cambiar_animacion(self.walk)
                        else:
                            self.cambiar_animacion(self.stay)
            else:
                self.cambiar_animacion(self.hitted)
        else:
            self.cambiar_animacion(self.death)


    def cambiar_animacion(self, animacion):
        if self.animacion != animacion[DERECHA] and self.animacion != animacion[IZQUIERDA]:
            self.frame = 0
        self.animacion = animacion[self.direccion]

         
    def actualizar_posicion(self):
    
        self.rect.x += self.move_x
        self.rect.y += self.move_y
        self.rect_pies.x += self.move_x
        self.rect_pies.y += self.move_y
        self.rect_hitbox.x += self.move_x
        self.rect_hitbox.y += self.move_y


    def updatear_frames(self):
        if(self.frame < len(self.animacion) - 1):
            self.frame += 1 
        else:
            self.frame = 0

            if not self.vivo:
                self.activo = False

            if self.golpeado:
                self.golpeado = False
                self.detener()
            
            if self.cayendo:
                self.frame = len(self.animacion) - 1

    
    def draw(self):
        self.imagen = self.animacion[self.frame]
        self.screen.blit(self.imagen,self.rect)
    

    def controles(self, lista_eventos, teclas_presionadas):
        
        for event in lista_eventos:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.saltar(True)

                if event.key == pygame.K_z:
                    self.disparar()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.detener()

                if event.key == pygame.K_SPACE:
                    self.saltar(False)


        if True in teclas_presionadas:

            if teclas_presionadas[pygame.K_LEFT] and not teclas_presionadas[pygame.K_RIGHT] :
                self.mover(IZQUIERDA)

            elif teclas_presionadas[pygame.K_RIGHT] and not teclas_presionadas[pygame.K_LEFT] :
                self.mover(DERECHA)

            elif teclas_presionadas[pygame.K_RIGHT] and teclas_presionadas[pygame.K_LEFT]:
                self.detener()

            if teclas_presionadas[pygame.K_SPACE]:
                self.limitar_salto()

    

    def actualizar(self, plataformas, objetivos, delta_ms, lista_eventos, teclas_presionadas):
        if self.activo:
            self.timer += delta_ms
            print(delta_ms)
            if self.timer > 30:
                self.timer = 0
                self.controles(lista_eventos, teclas_presionadas)
                self.verificar_plataforma(plataformas)
                self.aplicar_gravedad()
                self.actualizar_posicion()
                self.animaciones()
                self.updatear_frames()
                self.proyectiles.actualizar_disparos(objetivos)
                self.verificar_colision_enemigos(objetivos)
                self.cooldown_invulnerabilidad(delta_ms)
                self.cooldown_disparo(delta_ms)
                self.draw()

        


