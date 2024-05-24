#pygame 가이드 :pygame.display.set_mode()
                # pygame.image.load('images/ship.bmp').convert()
                # pygame.font.SysFont(None, 64).render()
                # pygame.Rect(0,0,10,50)/.get_rect()
                #events=pygame.event.get()   

import pygame
import sys



pygame.init()
screen_surface=pygame.display.set_mode(size=(800,400))
ship_img_surf=pygame.image.load('images/ship.bmp').convert()


font=pygame.font.SysFont(None, 64)
font_surface=font.render(
    str(524),
    True, 
    'black'
    )

while True :
    for event in pygame.event.get():
        #32 SPACE   13 ENTER  1073741904 왼쪽화살표
        print(event)
        if event.type == 256:
            print('QUIT')
            sys.exit()
        elif event.type == 768:
              print('KEYDOWN')
        elif event.type == 769:         
               print('KEYUP')
               if event.key==32 :
                sys.exit()
    screen_surface.fill('white')
    screen_surface.blit(ship_img_surf, ship_img_surf.get_rect())
    screen_surface.blit( font_surface,  font_surface.get_rect())

    pygame.display.flip()