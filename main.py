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
player_speed=1
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

    # Create rectangles for collision
    cat_rect = pygame.Rect(cat_x, cat_y, cat.get_width(), cat.get_height())
    mouse_rect = pygame.Rect(mouse_x, mouse_y, mouse.get_width(), mouse.get_height())

# Collision check
    if cat_rect.colliderect(mouse_rect):
      mouse_x = random.randint(0, 550)
      mouse_y = random.randint(0, 550)
      score += 1





pygame.quit()




