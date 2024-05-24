import pygame


class Alien:
    def __init__(self,screen_surface):
        self.alien_img = pygame.image.load('images/alien.bmp').convert()
        self.screen_surface=screen_surface
        self.alien_rect = self.alien_img.get_rect()

    def render(self):
        self.screen_surface.blit(self.alien_img, self.alien_rect)

    def move(self, x, y):
        self.alien_rect.x = x
        self.alien_rect.y = y

# alien=Alien()
# alien.render()
# alien.move()
