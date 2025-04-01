import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Shapes")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize variables
drawing = False
shape = "square"  # Default shape
start_pos = (0, 0)

# Function to draw shapes
def draw_shape(start, end):
    if shape == "square":
        size = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
        pygame.draw.rect(screen, RED, (start[0], start[1], size, size), 2)
    elif shape == "right_triangle":
        pygame.draw.polygon(screen, RED, [start, (start[0], end[1]), end], 2)
    elif shape == "equilateral_triangle":
        h = (3 ** 0.5) / 2 * abs(end[0] - start[0])
        pygame.draw.polygon(screen, RED, [start, (start[0] + (end[0] - start[0]) // 2, start[1] - h), end], 2)
    elif shape == "rhombus":
        w, h = abs(end[0] - start[0]), abs(end[1] - start[1])
        center = (start[0] + w // 2, start[1] + h // 2)
        pygame.draw.polygon(screen, RED, [(center[0], start[1]), (end[0], center[1]), (center[0], end[1]), (start[0], center[1])], 2)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            draw_shape(start_pos, end_pos)
            drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                shape = "square"
            elif event.key == pygame.K_2:
                shape = "right_triangle"
            elif event.key == pygame.K_3:
                shape = "equilateral_triangle"
            elif event.key == pygame.K_4:
                shape = "rhombus"
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()