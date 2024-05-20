import pygame
from myfunc import init, create_ship, create_bullet, create_aliens,\
    handle_event, update_object, render_object

pygame.init()


screen_surf = init()
ship_rect = create_ship(screen_surf)  
aliens = create_aliens()

clock = pygame.time.Clock()

while True:
    
    # Process player inputs.
    handle_event(ship_rect)
    update_object(screen_surf, ship_rect, aliens)
    render_object(screen_surf, ship_rect, aliens)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
    
    # if len(aliens) == 0:
    #     print('Game Over!')
    #     is_running = False
        
    #game_over_msg.render('Game Over!', True, (0, 0, 0))

