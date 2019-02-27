
# coding: utf-8

# In[ ]:


import pygame
import random
from pygame.locals import *

pygame.init()
# 背景设置
SIZE = (432, 648)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("周先生O(∩_∩)O~圣诞快乐")
background = pygame.image.load('snow.jpg')
# 输出字体
myfont = pygame.font.SysFont("segoeuisemibold", 20)
textImage = myfont.render(u"I Love You, Jim!!! ~O(∩_∩)O~", True, (15, 91, 239))

snow = []



for index in range(300):
    x = random.randrange(0, SIZE[0])
    y = random.randrange(0, SIZE[1])
    speedx = random.randint(-1, 2)
    speedy = random.randint(2, 5)
    snow.append([x, y, speedx, speedy])
    
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.blit(background, (0, 0))
    screen.blit(textImage, (100, 180))
# pygame.display.update()
    for index in range(len(snow)):
        pygame.draw.circle(screen, (255, 255, 255), snow[index][:2], snow[index][3])
        
        snow[index][0] += snow[index][2]
        snow[index][1] += snow[index][3]
        
        if snow[index][1] > SIZE[1]:
            snow[index][1] = random.randrange(-50, -10)
            snow[index][0] = random.randrange(0, SIZE[0])
            
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
    


# In[3]:


pygame.font.get_fonts()

