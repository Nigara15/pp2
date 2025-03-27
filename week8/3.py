import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ERASER = WHITE

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Program")
screen.fill(WHITE)

# Variables
drawing = False
shape = "brush"  # Default tool
color = BLACK
start_pos = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                shape = "brush"
            elif event.key == pygame.K_r:
                shape = "rectangle"
            elif event.key == pygame.K_c:
                shape = "circle"
            elif event.key == pygame.K_e:
                shape = "eraser"
            elif event.key == pygame.K_1:
                color = BLACK
            elif event.key == pygame.K_2:
                color = RED
            elif event.key == pygame.K_3:
                color = GREEN
            elif event.key == pygame.K_4:
                color = BLUE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            if shape == "rectangle":
                end_pos = event.pos
                rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, color, rect, 2)
            elif shape == "circle":
                end_pos = event.pos
                radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
                center = (start_pos[0] + (end_pos[0] - start_pos[0]) // 2, start_pos[1] + (end_pos[1] - start_pos[1]) // 2)
                pygame.draw.circle(screen, color, center, radius, 2)
        elif event.type == pygame.MOUSEMOTION and drawing:
            if shape == "brush":
                pygame.draw.circle(screen, color, event.pos, 5)
            elif shape == "eraser":
                pygame.draw.circle(screen, ERASER, event.pos, 10)
    
    pygame.display.flip()

pygame.quit()
