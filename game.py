import pygame
import pygame_menu
from tank import Tank

# init pygame
pygame.init()

# Set the width and height of the game window
WIDTH = 1024 * 2
HEIGHT = 1024

# create clock
clock = pygame.time.Clock()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bullet_speed = [ 1 ]

######################################### make a menu
menu_width = 400
menu_height = 300
# make a menu surface
menu_surface = pygame.surface.Surface((menu_width,menu_height))
def set_velocity(value, velocity_num):
    # Update the velocity that the tank shoots
    bullet_speed[0] = velocity_num
    print("Bullet Speed List",bullet_speed)
    pass

menu = pygame_menu.Menu('Shell Velocity', menu_width, menu_height,
                       theme=pygame_menu.themes.THEME_BLUE)
menu.add.selector('Difficulty :', [('Fast', 20), ('Medium', 12), ('Slow',6) ], onchange=set_velocity)

################################################################



# make background
bg_tile = pygame.image.load('assets/backgroundColorDesert.png')
background = pygame.Surface(screen.get_size())
for i in range(0, WIDTH, bg_tile.get_width()):
    for j in range(0, HEIGHT, bg_tile.get_height()):
        background.blit(bg_tile, (i, j))

# make bullet group
bullets = pygame.sprite.Group()

# Create a tank at center of the screen
my_tank = Tank(WIDTH//2, HEIGHT - 100, bullets,bullet_speed, screen)

# Set the running flag to True
running = True



# Main game loop
while running:
    # Check for events and pass to menu
    events = pygame.event.get()
    for event in events:
        # If the user closes the window, set running to False
        if event.type == pygame.QUIT:
            running = False

    # Set the game's FPS
    clock.tick(60)

    # Draw the background
    screen.blit(background, (0, 0))

    # Update the tank & bullets
    my_tank.update()
    bullets.update()

    # Draw the tank & bullets
    [b.draw(screen) for b in bullets]
    my_tank.draw(screen)

    # blit menu surface
    menu.update(events)
    menu.draw(screen)


    # Update the display
    pygame.display.flip()
pygame.quit()
