import pygame


class Ship:
    def __init__(self,screen_surface):
        self.ship_img_surf=pygame.image.load('images/ship.bmp').convert()
        self.screen_surface=screen_surface

        self.ship_rect = self.ship_img_surf.get_rect()
        

    def render(self):
        
        # self.screen_surface.blit(self.ship_img_surf, self.ship_img_surf.get_rect())
        self.screen_surface.blit(self.ship_img_surf,self.ship_rect)
    def midbottom(self):
        self.ship_rect.midbottom = self.screen_surface.get_rect().midbottom
# ship=Ship(screen_surface)
# ship.render()