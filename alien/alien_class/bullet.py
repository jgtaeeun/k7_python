import pygame


class Bullet :
    def __init__(self,screen_surface):
          self.bullet_rect = pygame.rect.Rect(0, 0, 50, 10)
     
          self.screen_surface=screen_surface

    def render(self):
          pygame.draw.rect(self.screen_surface, 'red', self.bullet_rect)

    def move_front_ship(self, ship_rect):
            self.bullet_rect.midbottom = ship_rect.midtop

# bullet=Bullet()    
# bullet.render() 
# bullet.move_front_ship()