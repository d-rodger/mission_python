WIDTH = 1920
HEIGHT = 1080
player_x = 600  
player_y = 350
mars_x = 900
mars_y = 150

def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (mars_x, mars_y))
    screen.blit(images.ship, (1000, 200))
    screen.blit(images.astronaut, (player_x, player_y)) 
    
def game_loop():
    global player_x, player_y
    global mars_x, mars_y
    if keyboard.d:
        player_x+= 10
    elif keyboard.a:
        player_x-=10
    elif keyboard.w:
        player_y-=10
    elif keyboard.s:
        player_y+=10
    elif keyboard.i:
        mars_y-=10
    elif keyboard.j:
        mars_x -=10
    elif keyboard.l:
        mars_x +=10
    elif keyboard.k:
        mars_y +=10
                
clock.schedule_interval(game_loop, 0.03)
