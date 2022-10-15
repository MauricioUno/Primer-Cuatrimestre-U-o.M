import pygame.locals
import pygame

pygame.init()

running = True

window = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("COCO!")

imagen_espacio = pygame.image.load("Programas Pygame\Espacio.jpg")
window.blit(imagen_espacio, (0,0))
i = 0
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    teclas_presionadas = pygame.key.get_pressed()
    if True in teclas_presionadas:
        if teclas_presionadas[pygame.K_DOWN]:
            pygame.draw.rect(window,(0,100,0),(i,0,50,100))
            i += 1

    pygame.display.flip()


pygame.quit()
