import pygame
from bullet import Bullet


class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, bullets, screen):
        super().__init__()
        self.image = pygame.image.load('assets/tanks_tankNavy2.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.theta = 45
        self.arrow = pygame.image.load('assets/tank_arrowFull.png')
        self.zoom = 0.4
        self.bullets = bullets
        self.last_fire = 0
        self.screen = screen

    def update(self):

        # check for key presses
        self.check_keys()

    def check_keys(self):
        # check for key presses
        keys = pygame.key.get_pressed()
        # if the left arrow key is pressed
        if keys[pygame.K_LEFT]:
            # rotate the tank left
            self.theta += 1
        # if the right arrow key is pressed
        if keys[pygame.K_RIGHT]:
            # rotate the tank right
            self.theta -= 1
        # if space bar is pressed
        if keys[pygame.K_SPACE] and pygame.time.get_ticks() - self.last_fire > 500:
            # set the last fire time
            self.last_fire = pygame.time.get_ticks()
            # fire a bullet
            print('BOOOOMMM!!!')
            # create a bullet
            bullet = Bullet(self.rect.centerx, self.rect.centery,
                            self.theta, self.screen)
            # add the bullet to the bullets group
            self.bullets.add(bullet)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # Rotate the arrow and scale it
        rot_arrow = pygame.transform.rotozoom(
            self.arrow, self.theta, self.zoom)
        # Get the rectangle of the rotated arrow
        rot_arrow_rect = rot_arrow.get_rect()
        # Set the center of the rotated arrow to the center of the tank
        rot_arrow_rect.center = self.rect.center
        # Draw the rotated arrow
        screen.blit(rot_arrow, rot_arrow_rect)
