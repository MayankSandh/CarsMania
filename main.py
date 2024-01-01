import pygame
import time
import math
from utils import scale_image, draw, rotate_center

GRASS = scale_image(pygame.image.load("img/grass.jpg"), 1.96)
TRACK = pygame.image.load("img/track.png")
TRACK_BORDER = pygame.image.load("img/track-border.png")
FINISH = pygame.image.load("img/finish.png")
RED_CAR = scale_image(pygame.image.load("img/red-car.png"), 0.75)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
print(WIDTH, HEIGHT)
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("racing game!")\

FPS = 60
clock = pygame.time.Clock()


class Car:
    IMG = RED_CAR
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0

    def rotate(self, left = False, right = False):
        if left:
            self.angle+=self.rotation_vel
        elif right:
            self.angle-=self.rotation_vel

    def draw(self,window):
        rotate_center(window, self.img)

class PlayerCar(Car):
    IMG = RED_CAR

images = [(GRASS, (0,0)), (TRACK, (0,0))]
player_car = PlayerCar(4,4)



running = True
while running:
    clock.tick(FPS)

    WINDOW.blit(GRASS, (0,0))
    WINDOW.blit(TRACK, (0,0))
    WINDOW.blit(FINISH, (0,0))
    WINDOW.blit(RED_CAR, (27,200))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
pygame.quit()