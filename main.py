import pygame
import random , sys
from object import*
pygame.init()
SCREEN_WEIGHT = 800
SCREEN_HEIGHT = 600
score = 0
screen = pygame.display.set_mode((SCREEN_WEIGHT,SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
SCREEN_COLOR = 16, 33, 89
dt = 0
platform_x = 350
platform_y = 550
ball_x = platform_x+50
ball_y = platform_y-20
brick_x = 10
brick_y = 10
pygame.display.set_caption("Bricks Game")
pygame.display.update()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
platform = Platform(screen, (255, 255, 255), (platform_x,platform_y, 120, 20))
ball = Ball(screen, (255, 0, 0), [ball_x, ball_y], 10)
brick = Brick(screen, (0, 255, 0), (brick_x, brick_y, 80, 30))
timer = Counter(screen)
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SCREEN_COLOR)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platform.move(-10)
    if keys[pygame.K_RIGHT]:
        platform.move(10)
    if keys[pygame.K_BACKSPACE]:
        pygame.quit()
        sys.exit()
    ball.draw()
    brick.draw()
    platform.draw()
    ball.move()
    ball.collision_check(platform.rect)
    ball.collision_check(brick.rect)
    timer.timer(screen)
    pygame.display.update() 
pygame.quit()