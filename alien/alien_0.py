#화면밖으로 나가지 않도록 하기
import pygame                                

pygame.init()

screen_surf = pygame.display.set_mode((1280,720))


ship_img = pygame.image.load('images/ship.bmp')
alien_img = pygame.image.load('images/alien.bmp')

ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom

alien_rect = pygame.rect.Rect(200,200,200,200)

clock = pygame.time.Clock()
left_pressed=False
right_pressed=False

while True:
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            pygame.quit()                         
            raise SystemExit                        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT :
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
              if alien_rect.x < screen_rect.width-   ship_rect.width:
                alien_rect.x=alien_rect.x + 20  
              
 
    if left_pressed :
              if  ship_rect.x >0 :
                ship_rect.x=ship_rect.x - 10
              if   alien_rect.x >0 :
                alien_rect.x= alien_rect.x - 20
        
    



    screen_surf.fill('white')  # Fill the display with a solid color
    screen_surf.blit(ship_img, ship_rect)
    screen_surf.blit(alien_img, alien_rect)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)            
             

   

       