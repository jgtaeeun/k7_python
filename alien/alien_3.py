#총알과 외계인 부딪힐 때 



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




bullet_rect = None
bullets = []
left_pressed=False
right_pressed=False
alien_x_direction = 1 # False: -1, 1: right
alien_x_direction_changed = False
clock = pygame.time.Clock()

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #. 총알의 개수를 5개 이하로 하시오
                if len(bullets) < 5:
                    bullet_rect = pygame.rect.Rect(0, 0, 5, 50)
                    bullet_rect.midbottom = ship_rect.midtop
                    bullets.append(bullet_rect)
            elif event.key == pygame.K_RIGHT :
               right_pressed=True
            elif event.key == pygame.K_LEFT :
                left_pressed=True
            elif event.key == pygame.K_UP :
                ship_rect.y=ship_rect.y - 10
            elif event.key == pygame.K_DOWN :
                ship_rect.y=ship_rect.y + 10

        elif event.type == pygame.KEYUP:    
            if event.key == pygame.K_RIGHT :
                right_pressed=False
            elif event.key == pygame.K_LEFT :
                left_pressed=False


    if right_pressed :
              screen_rect=screen_surf.get_rect()
              if ship_rect.x < screen_rect.width - ship_rect.width:     
                ship_rect.x=ship_rect.x + 10
                 
    if left_pressed :
              if  ship_rect.x >0 :
                ship_rect.x=ship_rect.x - 10
              

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

    if bullets:
        screen_rect = screen_surf.get_rect()
       
        for bullet in bullets:
            if bullet.y < 0:
                bullets.remove(bullet)
       
        for bullet in bullets:
            bullet.y = bullet.y - 10

    for alien in aliens:
        for bullet in bullets:
            if pygame.rect.Rect.colliderect(alien, bullet):
                aliens.remove(alien)
                bullets.remove(bullet)

    screen_surf.fill('white')  # Fill the display with a solid color
    screen_surf.blit(ship_img, ship_rect)

    # 외계인 한 줄 만들기
    if aliens:
         for alien in aliens:
            screen_surf.blit(alien_img, alien) 

    #총알의 개수를 5개 이하로 반복 출력     
    if bullets:
      for bullet in bullets:
        pygame.draw.rect(screen_surf, 'red', bullet)

    
        
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
