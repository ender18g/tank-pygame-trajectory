import pygame
from math import sin, cos, atan2, pi, atan

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, theta, screen):
        super().__init__()
        self.image = pygame.image.load('assets/tank_bullet3.png')
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.theta = theta # theta in deg
        self.zoom = 1
        self.speed = 8
        self.screen = screen

        # init values for trajectory
        self.x_dot = self.speed * cos(self.theta * pi/180)
        self.y_dot = self.speed * sin(self.theta * pi / 180)

        self.x_ddot = 0
        self.y_ddot = 0

        self.drag = 5e-3
        self.gravity = 5e-2

    def update(self):
        # code here for the bullet trajectory
        self.x += self.x_dot
        self.y -= self.y_dot

        # handle the velocity
        self.x_dot += self.x_ddot
        self.y_dot += self.y_ddot

        # handle the acceleration
        self.x_ddot = -self.drag * self.x_dot
        self.y_ddot = -self.drag * self.y_dot - self.gravity


        # Update the bullet's rect
        self.rect.center = (self.x, self.y)

        # check if this bullet should stop (land on dirt)
        if self.y > self.screen.get_height() - 100:
            self.y_dot = 0
            self.x_dot = 0
            self.y_ddot = 0
            self.x_ddot = 0

        # update the theta IF positive y velocity
        if not self.y_dot == 0:
            rads = atan2(self.y_dot, self.x_dot)
            self.theta = rads * 180 / pi

    def draw(self, screen):
        rot_bullet = pygame.transform.rotozoom(self.image, self.theta, 1)
        # get rectangle of rotated bullet
        rot_bullet_rect = rot_bullet.get_rect()
        rot_bullet_rect.center = self.rect.center

        screen.blit(rot_bullet, rot_bullet_rect)
