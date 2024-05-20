#외계인 한 줄 함대를 자동으로 좌우로 움직이기  


import pygame

pygame.init()

screen_surf = pygame.display.set_mode((1280,720))


ship_img = pygame.image.load('images/ship.bmp')
alien_img = pygame.image.load('images/alien.bmp')

ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom

alien_rect = pygame.rect.Rect(200,200,200,200)

# 외계인 한 줄 만들기
aliens = []
alien_rect = alien_img.get_rect()
alien_x_pos = alien_rect.width
alien_y_pos = alien_rect.height

for _ in range(10):
    alien = pygame.rect.Rect(alien_x_pos, alien_y_pos,\
                            alien_rect.width,\
                            alien_rect.height)
    alien_x_pos += alien_rect.width * 2
    aliens.append(alien)

clock = pygame.time.Clock()
left_pressed=False
right_pressed=False
alien_x_direction = 1 # False: -1, 1: right
alien_x_direction_changed = False


while True:
    #  if alien_rect.x < screen_rect.width-   ship_rect.width:
    if aliens:
        screen_rect = screen_surf.get_rect()
        for alien in aliens:
            if screen_rect.width - alien.width < alien.x:
                alien_x_direction = -1
                alien_x_direction_changed = True
                break
            elif alien.x < screen_rect.x:
                alien_x_direction = 1
                alien_x_direction_changed = True
                break

        for alien in aliens:
            #print(alien.y, alien_y_pos)
            alien.x += alien_x_direction * 2
            if alien_x_direction_changed:
                alien.y += alien_img.get_rect().height

    alien_x_direction_changed = False




    screen_surf.fill('white')  # Fill the display with a solid color
    screen_surf.blit(ship_img, ship_rect)

    # 외계인 한 줄 만들기
    if aliens:
         for alien in aliens:
            screen_surf.blit(alien_img, alien) 

 
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)