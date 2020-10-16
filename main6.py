import pygame
from Vec2d import Vec2d
import os
import random
screen_width=800
screen_height=600
pygame.init()
screen=pygame.display.set_mode((screen_width,screen_height))
FONT=pygame.font.init()
white=(255,255,255)
linecolor="red"
player=Vec2d(300,300)
FONT = pygame.font.SysFont("comicsans", 50)
clock = pygame.time.Clock()
class Asteroid:
    def __init__(self,pos,color,vel):
        self.pos=pos
        self.color=color
        self.vel=vel
    def __repr__(self): 
        return f"XY: {self.pos.x,self.pos.y}"
    
    def move(self):
        self.pos+=self.vel
def draw_game(window):
    screen.fill((255,255,255))
    for i in asteroids:
        pygame.draw.circle(window,(0,255,0),(round(i.pos.x),round(i.pos.y)),20) 
    pygame.draw.rect(window,(255,0,0),(player.x,player.y,100,100))
    pygame.display.update()

def moveasteroids():
    for i in asteroids:
        i.move()

def moveplayer():
    keys=pygame.key.get_pressed()
    if keys[pygame.K_a] and player.x >0:
        player.x-=2
    if keys[pygame.K_d] and player.x + 100 < screen_width:
        player.x+=2
    if keys[pygame.K_w] and player.y >0:
        player.y-=2
    if keys[pygame.K_s] and player.y + 100 < screen_height:
        player.y+=2

def update_game(): #calculate next frame positions for all game objects. modifies the game state variables. does not draw anything on the screen"
    moveplayer()
    moveasteroids()
def init_game(): #setup all the game object positions at the start
    global asteroids
    asteroids = [ Asteroid( Vec2d(random.random()*screen_width,random.random()*screen_height), (255,0,0),Vec2d(random.random(),random.random())) for x in range(0,10) ]
init_game()

running=True

while running:
    draw_game(screen)
    update_game()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    

