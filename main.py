import pygame
import math
SCREEN_WIDTH = 1244
SCREEN_HEIGHT = 1016
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
TRACK = pygame.image.load('imgs/track.png')

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load('imgs/car.png')
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(490, 820))
        self.isDriving = False
        self.vel_vector = pygame.math.Vector2(1, 0)
        self.angle = 0
        self.rotation_vel = 5
        self.direction = 0
        self.vel = 0
        self.max_vel = 6
        self.acceleration = 0.5

    def update(self):
        self.drive()
        self.rotate()
        self.radar()

    def drive(self):
        if self.isDriving:
            self.vel = min(self.vel + self.acceleration, self.max_vel)
            self.rect.center += self.vel_vector * self.vel # ERROR SPEED OF THE CAR
            
    def rotate(self):    
        self.angle -= self.direction*self.rotation_vel
        self.vel_vector.rotate_ip(self.direction*self.rotation_vel)
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def radar(self, radar_angle):
        length = 0
        x = int(self.rect.center[0])
        y = int(self.rect.center[1])

        while not SCREEN.get_at((x, y)) == pygame.Color(2, 105, 31, 255) and length < 200:
            length += 1
            x = int(self.rect.center[0] + math.cos(math.radians(self.angle + radar_angle)) * length)
            y = int(self.rect.center[1] - math.sin(math.radians(self.angle + radar_angle)) * length)

        # Draw Radar
        pygame.draw.line(SCREEN, (255, 255, 255, 255), self.rect.center, (x, y), 1)
        pygame.draw.circle(SCREEN, (0, 255, 0, 0), (x, y), 3)

        dist = int(math.sqrt(math.pow(self.rect.center[0] - x, 2)
                             + math.pow(self.rect.center[1] - y, 2)))

        self.radars.append([radar_angle, dist])

    def data(self):
        input = [0, 0, 0, 0, 0]
        for i, radar in enumerate(self.radars):
            input[i] = int(radar[1])
        return input

car = pygame.sprite.GroupSingle(Car())

def eval_genomes():
    run = True
    while run:
        car.sprite.isDriving = False
        car.sprite.direction = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        SCREEN.blit(TRACK, (0, 0))
        user_input = pygame.key.get_pressed()
    

        if user_input[pygame.K_UP]:
            car.sprite.isDriving = True
        if user_input[pygame.K_LEFT]:
            car.sprite.direction = -1
        elif user_input[pygame.K_RIGHT]:
            car.sprite.direction = 1

        car.draw(SCREEN)
        car.update()
        pygame.display.update()

eval_genomes()