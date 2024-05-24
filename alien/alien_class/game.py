#ctrl shifr f :검색창에 함수이름 검색하면 그 함수가 있는 py파일 위치 뜬다.
#pygame 가이드 :pygame.display.set_mode()
                # pygame.image.load('images/ship.bmp').convert()
                # pygame.font.SysFont(None, 64).render()
                # pygame.Rect(0,0,10,50)/.get_rect()
                #events=pygame.event.get()   

import pygame
import sys



pygame.init()
screen_surface=pygame.display.set_mode(size=(800,400))
print(type(screen_surface),screen_surface.get_rect())  #<class 'pygame.surface.Surface'> <rect(0, 0, 800, 400)>

ship_img_surf=pygame.image.load('images/ship.bmp').convert()
print(ship_img_surf.get_rect())  #<rect(0, 0, 60, 48)>

font=pygame.font.SysFont(None, 64)
font_surface=font.render(
    'hello',
    True, 
    'black'
    )
print(font_surface.get_rect())

bullets=[]
bullet_rect=pygame.Rect(0,0,10,50)
bullets.append(bullet_rect)
print(bullet_rect)


#60Fps : 1초에 60번 반복한 키이벤트 저장
events=pygame.event.get()      #저장된 이벤트 값들 List[Event]
print(type(events), events)   
#<class 'list'>
# [<Event(4352-AudioDeviceAdded
#  {'which': 0, 'iscapture': 0})>, <Event(32774-WindowShown {'window': None})>, <Event(32768-ActiveEvent {'gain': 1, 'state': 2})>, <Event(32785-WindowFocusGained {'window': None})>, <Event(770-TextEditing {'text': '', 'start': 0, 'length': 0, 'window': None})>, <Event(32768-ActiveEvent {'gain': 1, 'state': 1})>, <Event(32783-WindowEnter {'window': None})>, <Event(1024-MouseMotion {'pos': (157, 218), 'rel': (0, 0), 'buttons': (0, 0, 0), 'touch': False, 'window': None})>, <Event(32770-VideoExpose {})>, <Event(32776-WindowExposed {'window': None})>]

print(type(events[0])) # <class 'pygame.event.Event'>
print(events[0].type)  #4352
print(type(events[0].type))  #<class 'int'>


#=============================================================================================
# for event in pygame.event.get():           #event는 List[Event]에서 Event요소 1개씩이다.
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             raise SystemExit
#         if event.type == pygame.KEYDOWN:

print(pygame.QUIT) # 256 
print( pygame.KEYDOWN) #768
print( pygame.KEYUP)  #769

while True :
    for event in pygame.event.get():
        if event.type == 256:
            print('QUIT')
            sys.exit()
        elif event.type == 768:
              print(event.key)  #32 SPACE   13 ENTER  1073741904 왼쪽화살표
              print('KEYDOWN')
        elif event.type == 769:         
               print('KEYUP')
               if event.key==32 :
                sys.exit()

    screen_surface.blit(ship_img_surf, ship_img_surf.get_rect())
    screen_surface.blit( font_surface,  font_surface.get_rect())
    screen_surface.fill('white')
    pygame.display.flip()



