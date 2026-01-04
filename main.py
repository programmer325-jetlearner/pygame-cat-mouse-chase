import pygame
import random

pygame.init()
screen=pygame.display.set_mode((600,600))
RED=(255,0,0)
score=0
cat_x=200
cat_y=200
mouse_x=150
mouse_y=300
random_x=random.randint(-500,500)
random_y=random.randint(-500,500)                 
player_speed=7
cat=pygame.image.load("images/cat.png")
mouse=pygame.image.load("images/mouse.png")
bg=pygame.image.load("images/bg.jpg")
clock=pygame.time.Clock()




while True:
    font1=pygame.font.SysFont("Arial",70)
    screen.blit(bg,(0,0))
    screen.blit(cat,(cat_x,cat_y))
    screen.blit(mouse,(mouse_x,mouse_y))
    text=font1.render(str(score),True,RED)
    screen.blit(text,(500,100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
   
    keys=pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        cat_y-=player_speed
    if keys[pygame.K_DOWN]:
        cat_y+=player_speed
    if keys[pygame.K_LEFT]:
        cat_x-=player_speed
    if keys[pygame.K_RIGHT]:
        cat_x+=player_speed

    if cat_x==mouse_y-20 or  cat_y==mouse_x-20 or cat_y==mouse_y-20 or cat_x==mouse_x-20:
      random_x=random.randint(-250,250)
      random_y=random.randint(-250,200) 
      mouse_x=random_x
      mouse_y=random_y
      score+=1



pygame.quit




