# 외계인 여러 줄 만들기
import pygame

pygame.init()

screen_surf = pygame.display.set_mode((1280,720))

alien_img = pygame.image.load('images/alien.bmp')

alien_rect = pygame.rect.Rect(200,200,200,200)



alien_rect = alien_img.get_rect()
alien_x_pos = alien_rect.width
alien_y_pos = alien_rect.height

aliens = []
for _ in range(3):
    for _ in range(10):
        alien = pygame.rect.Rect(alien_x_pos, alien_y_pos,\
                            alien_rect.width,\
                            alien_rect.height)
        alien_x_pos += alien_rect.width * 2
        aliens.append(alien)
    alien_y_pos += alien_rect.height * 2
    alien_x_pos = alien_rect.width    
    
           

clock = pygame.time.Clock()

while True:
#     # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    



    
    
    screen_surf.fill('white') 
              
   
        
    if aliens:
            for alien in aliens:
               screen_surf.blit(alien_img, alien) 

    
    
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
