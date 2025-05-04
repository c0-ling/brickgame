import pygame
class Ball():
    def __init__(self,surface,color,center,radius):
        self.surface = surface
        self.color = color
        self.center = center
        self.radius = radius
        self.rect = pygame.Rect(self.center[0] - self.radius,self.center[1] - self.radius,self.radius * 2,self.radius * 2)
        self.dx = 5
        self.dy = -5
    def draw(self):
        pygame.draw.circle(self.surface,self.color,self.center,self.radius)
    def move(self):
        self.center[0] += self.dx
        self.center[1] += self.dy
        if self.center[0] - self.radius <= 0 or self.center[0] + self.radius >= 800:
            self.dx *= -1 
        if self.center[1] + self.radius <= 0:
            self.dy *= -1
        if self.center[1] - self.radius >= 580:
            self.dx *=0
            self.dy *=0
    def collision_check(self,rect):
        self.rect = pygame.Rect(self.center[0] - self.radius,self.center[1] - self.radius,self.radius * 2,self.radius * 2)
#Rect(left, top, width, height) 
#circle(surface, color, center, radius) -> Rect
        if self.rect.colliderect(rect):
            dx = (self.center[0] - rect.centerx) / rect.width
            dy = (self.center[1] - rect.centery) / rect.height
            if abs(dx) > abs(dy):
                self.dx *= -1 
            else:
                self.dy *= -1 
class Platform():
    def __init__(self,surface,color,rect):
        self.surface = surface
        self.color = color
        self.rect = pygame.Rect(rect)
    def draw(self):
        pygame.draw.rect(self.surface,self.color,self.rect)
    def move(self,onlyx):
        self.rect.x += onlyx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
#Rect(left, top, width, height) -> Rect
class Brick():
    def __init__(self,surface,color,rect):
        self.surface = surface
        self.color = color
        self.rect = pygame.Rect(rect)
        self.exist = True
    def draw(self):
        if self.exist==True:
            pygame.draw.rect(self.surface,self.color,self.rect)
    def collision_gone(self,rect):
        brick_rect=pygame.Rect(self.rect)
        if brick_rect.colliderect(rect):
            self.exist = False
    def bricks_color(self):
        pass

class Counter():
    def __init__(self,screen):
        self.screen=screen
    def timer(self,screen):
        passing_time_ms = pygame.time.get_ticks()
        passing_time_sec = passing_time_ms//1000
        font = pygame.font.SysFont(None, 48)
        time_showing = font.render(f"TIME : {passing_time_sec}",True,(255, 255, 255))
        screen.blit(time_showing, (20, 20))

