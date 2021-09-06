import pygame
from pygame.locals import *

def draw_block():
    surface.fill((92,25,84))
    surface.blit(block,(x_axis,y_axis))
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((1000,500))
    surface.fill((92,25,84))
    block=pygame.image.load('resources/block.jpg').convert()
    x_axis=200
    y_axis=200
    surface.blit(block,(x_axis,y_axis))
    pygame.display.flip()
    

    run=True
    while run:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key==K_UP:
                    y_axis=y_axis-10
                    draw_block()
                if event.key==K_DOWN:
                    y_axis=y_axis+10
                    draw_block()
                if event.key==K_LEFT:
                    x_axis=x_axis-10
                    draw_block()
                if event.key==K_RIGHT:
                    x_axis=x_axis+10
                    draw_block()
                if event.key==K_ESCAPE:
                    run=False
                    
            elif event.type == QUIT:
                run=False
            

    