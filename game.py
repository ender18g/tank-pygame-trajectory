import pygame
from tank import Tank

# Set the width and height of the game window
WIDTH = 1024 * 2
HEIGHT = 1024

# create clock
clock = pygame.time.Clock()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# make background
bg_tile = pygame.image.load('assets/backgroundColorDesert.png')
background = pygame.Surface(screen.get_size())
for i in range(0, WIDTH, bg_tile.get_width()):
    for j in range(0, HEIGHT, bg_tile.get_height()):
        background.blit(bg_tile, (i, j))

# make bullet group
bullets = pygame.sprite.Group()

# Create a tank at center of the screen
my_tank = Tank(WIDTH//2, HEIGHT - 100, bullets, screen)

# Set the running flag to True
running = True

# Main game loop
while running:
    # Check for events
    for event in pygame.event.get():
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

    # Update the display
    pygame.display.flip()
pygame.quit()
