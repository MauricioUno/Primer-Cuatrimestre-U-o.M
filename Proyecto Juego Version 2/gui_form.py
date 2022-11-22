import pygame

class Form():
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_background, imagen_background, color_border,active):
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border

        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect(x = x, y = y)
        self.active = active
        self.image_background = imagen_background
        
    
    def set_active(self,name):
        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True


    def render(self):
        if(self.color_background != None):
            self.surface.fill(self.color_background)

        if self.color_border != None:
            pygame.draw.rect(self.surface, self.color_border, self.surface.get_rect(), 2)
             
        if(self.image_background != None):
            image_background = pygame.image.load(self.image_background).convert_alpha()
            image_background = pygame.transform.scale(image_background, (self.w, self.h)).convert_alpha()
            self.surface.blit(image_background, (0,0))


    def draw(self, delta_ms):
        self.master_surface.blit(self.surface,self.slave_rect)
        self.render()
        


