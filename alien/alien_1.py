#. 총알의 개수를 5개 이하로 하시오

# 외계인 한 줄 만들기

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

    #총알의 개수를 5개 이하로 반복 출력 /총알 속도   
    if bullets:
        screen_rect = screen_surf.get_rect()
       
        for bullet in bullets:
            if bullet.y < 0:
                bullets.remove(bullet)
       
        for bullet in bullets:
            bullet.y = bullet.y - 10


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