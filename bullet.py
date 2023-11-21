import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, theta, screen):
        super().__init__()
        self.image = pygame.image.load('assets/tank_bullet3.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.theta = theta
        self.zoom = 1
        self.speed = 4
        self.screen = screen

    def update(self):
        # code here for the bullet trajectory
        self.x += self.speed

        # Update the bullet's rect
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
