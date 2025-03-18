import pygame
import time
import math

pygame.init()
screen = pygame.display.set_mode((891,893))
center = (445.5, 446.5)
fps = 60

background = pygame.image.load('images/mickey.png')
right = pygame.image.load('images/right.png')
left = pygame.image.load('images/left.png')

background = pygame.transform.scale(background,((891,893)))

def rotate(image,angle,pos):
    rotated = pygame.transform.rotate(image, -angle)
    new_rect = rotated.get_rect(center = pos)
    return rotated, new_rect

running = True
clock = pygame.time.Clock()
while running:
    screen.fill((255,255,255))
    screen.blit(background,(0,0))

    t = time.localtime()
    min = t.tm_min
    sec = t.tm_sec

    min_angle = (min % 60) * 6
    sec_angle = (sec % 60) * 6

    r_rot , r_rec = rotate(right , min_angle, center)
    l_rot , l_rec = rotate(left, sec_angle, center)

    screen.blit(r_rot, r_rec.topleft)
    screen.blit(l_rot, l_rec.topleft)

    pygame.display.update()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
    