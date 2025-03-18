import pygame

pygame.init()

screen= pygame.display.set_mode((500,500))
pygame.display.set_caption("Ball")
x,y = 250,250
move = 20

running = True
while running:
    pygame.time.delay(50)
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    key = pygame.key.get_pressed()     
    if key[pygame.K_LEFT] and x - 25 - 20 >=0:
        x -= move
    if key[pygame.K_RIGHT] and x + 25 + 20<=500:
        x += move
    if key[pygame.K_UP] and y - 25 - 20 >=0:
        y -= move
    if key[pygame.K_DOWN] and y + 25 +20 <=500:
        y += move

    screen.fill((255,255,255))
    pygame.draw.circle(screen,'Red', (x,y),25)

    pygame.display.update()
pygame.quit()