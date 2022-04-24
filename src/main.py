WIDTH = 1920
HEIGHT = 1080
player_x = 600  
player = 350

def draw():
    screen.blit(images.backdrop, (0, 0))
    screen.blit(images.mars, (900, 150))
    screen.blit(images.ship, (450, 200))
