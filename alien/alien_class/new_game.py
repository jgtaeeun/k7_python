# a=5 
# print(type(a), a)  #<class 'int'> 5
# b=int(5)
# print(type(b), b)  #<class 'int'> 5


# class Game :
#     def __init__(self, title) :
#         self.title=title
#      def __str__(self):
#         return self.title


# g=Game('Space Invader!')
# print(type(g), g)  # <class '__main__.Game'> Space Invader!



#ctrl .하면 해결책 제시 (예: import필요한 거 알려줌)
# f12 <=> alt 왼쪽 화살표 
import sys
import pygame

from alien import Alien
from ship import Ship


class Game :
    def __init__(self, title) :
        self.title=title

        pygame.init()
        self.screen_surface=pygame.display.set_mode(size=(800,400))
        # self.ship_img_surf=pygame.image.load('images/ship.bmp').convert()
        self.ship=Ship(self.screen_surface)
        self.ship.midbottom()

       #외계인 1개
        # self.alien=Alien(self.screen_surface)
        # self.alien.move(50, 50)
        #외계인 2개 
        # self.aliens = []
        # alien = Alien(self.screen_surface)
        # alien.move(50, 50)
        # self.aliens.append(alien)

        # alien = Alien(self.screen_surface)
        # alien.move(150, 150)
        # self.aliens.append(alien)
        
        #외계인 함대
        self.aliens = []
        for j in range(0,3,2):
            for i in range(1,13,2):
             alien = Alien(self.screen_surface)
             alien.move(60*i,58*j)
             self.aliens.append(alien)
            


        self.font=pygame.font.SysFont(None, 64)
        self.font_surface=self.font.render(
            str(524),
            True, 
            'black'
        )
        self.clock = pygame.time.Clock()
       
    def __str__(self):
        return self.title
    
    def start(self):
        while True :
            for event in pygame.event.get():
        #32 SPACE   13 ENTER  1073741904 왼쪽화살표

                 if event.type == 256:
                      print('QUIT')
                      sys.exit()
                 elif event.type == 768:
                     print('KEYDOWN')
                     
                 elif event.type == 769:         
                    print('KEYUP')
                    if event.key==32 :
                        sys.exit()




            self.screen_surface.fill('white')

            for alien in self.aliens:
               alien.render()

            # self.screen_surface.blit(self.ship_img_surf, self.ship_img_surf.get_rect())
            self.ship.render()
            self.screen_surface.blit( self.font_surface,  self.font_surface.get_rect())

            pygame.display.flip()
            self.clock.tick(60) 

# g=Game('Space Invader!')
# g.start()