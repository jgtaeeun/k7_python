import pygame                                

pygame.init() 
#set_mode return type surface이다. pygame.image.load()의 return타입도 surface이다. 
#surface는 네모난 창이므로 get_rect()를 이용해 위치 조정할 수 있다.

screen_surf = pygame.display.set_mode((1280,720))  #표시할 창 또는 화면 초기화. 이 '디스플레이 표면'은 화면을 나타냅니다. 
ship_img = pygame.image.load('images/ship.bmp')
alien_img = pygame.image.load('images/alien.bmp')

# bullet_rect=pygame.rect.Rect(0,0,5,50) #방법 1: 좌상단 x,y 우하단 xy 방법2)좌상단 x,y 그리고 가로길이w, 세로길이h
# #방법 2로 한 bullet_rect


# ship_rect = pygame.rect.Rect(0,0,100,100)
ship_rect = ship_img.get_rect()
ship_rect.midbottom=screen_surf.get_rect().midbottom    #ship_img을 screen_surf 화면 바닥 중앙에 위치
alien_rect = pygame.rect.Rect(200,200,200,200)
# bullet_rect.midbottom=ship_rect.midtop     #bullet_rect을 .midbottom된 ship_rect 위쪽의 중앙에 위치
clock = pygame.time.Clock()
bullet_rect=None
bullets=[]
left_pressed=False
right_pressed=False
up_pressed=False
down_pressed=False

while True:
    # Process player inputs.
    for event in pygame.event.get():                #event는 키보드나 마우스입력
        if event.type == pygame.QUIT:
            pygame.quit()                           #창닫기 클릭 시 종료
            raise SystemExit                         #SystemExit로 강제로 실행창 종료 
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                  bullet_rect=pygame.rect.Rect(0,0,5,50) #방법 1: 좌상단 x,y 우하단 xy 방법2)좌상단 x,y 그리고 가로길이w, 세로길이h
                                                        #방법 2로 한 bullet_rect
                  bullet_rect.midbottom=ship_rect.midtop     #bullet_rect을 .midbottom된 ship_rect 위쪽의 중앙에 위치                                     
                  bullets.append(bullet_rect)           #스페이스 눌릴 때마다 bullet_rect을 만든다.그리고 bullets 리스트에 저장한다.                
#             # if event.key == pygame.K_RIGHT :
#             #     ship_rect.x=ship_rect.x + 10
#             #     alien_rect.x=alien_rect.x+20
#             # elif event.key == pygame.K_LEFT :
#             #     ship_rect.x=ship_rect.x - 10
#             #     alien_rect.x=alien_rect.x-20
#             # elif event.key == pygame.K_UP :
#             #     ship_rect.y=ship_rect.y - 10
#             #     alien_rect.y=alien_rect.y-20
#             # elif event.key == pygame.K_DOWN :
#             #     ship_rect.y=ship_rect.y + 10
#             #     alien_rect.y=alien_rect.y+20
            elif event.key == pygame.K_RIGHT :
                right_pressed=True
            elif event.key == pygame.K_LEFT :
                left_pressed=True
            elif event.key == pygame.K_UP :
                 up_pressed=True
            elif event.key == pygame.K_DOWN :
                 down_pressed=True

        elif event.type==pygame.KEYUP:
            if event.key == pygame.K_RIGHT :
                 right_pressed=False
            elif event.key == pygame.K_LEFT:
                 left_pressed=False
            elif event.key == pygame.K_UP :
                 up_pressed=False
            elif event.key == pygame.K_DOWN :
                 down_pressed=False

    if right_pressed :
             ship_rect.x=ship_rect.x + 1
             alien_rect.x=alien_rect.x+2
    if left_pressed :
             ship_rect.x=ship_rect.x - 1
             alien_rect.x=alien_rect.x-2
    if up_pressed :
             ship_rect.y=ship_rect.y - 1
             alien_rect.y=alien_rect.y-2
    if down_pressed :
             ship_rect.y=ship_rect.y + 1
             alien_rect.y=alien_rect.y +2

#     # Do logical updates here.
#     # ...
    # bullet_rect.y=bullet_rect.y-1
    if bullets:
        for bullet in bullets:#bullets[bullet_rect,bullet_rect,bullet_rect, ....]
         bullet.y=bullet.y-10  #속도감 올리기 위해 -1=>-10      


# Fill the display with a solid color  화면에 지정한 색상을 채우기
#     # screen.fill((0,0,255))
    screen_surf.fill('white')  # Fill the display with a solid color

    
#     # Render the graphics here.      화면 그리기
#     # ...

    screen_surf.blit(ship_img, ship_rect)
    screen_surf.blit(alien_img, alien_rect)
    if bullets:
        for bullet in bullets: #bullets[bullet_rect,bullet_rect,bullet_rect, ....]
            pygame.draw.rect(screen_surf,'red',bullet)
    
    
  

    pygame.display.flip()  # Refresh on-screen display           #뒤집기
    clock.tick(60)         # wait until next frame (at 60 FPS)    #60프레임(초당 60번 반복)
