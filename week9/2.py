import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake settings
snake = [(200, 200)]
direction = (20, 0)
speed = 10

# Food settings
class Food:
    def __init__(self):
        self.x = random.randint(0, WIDTH // 20 - 1) * 20
        self.y = random.randint(0, HEIGHT // 20 - 1) * 20
        self.size = random.choice([10, 15, 20])  # Different sizes = different weights
        self.value = self.size // 5  # Bigger food gives more points
        self.timer = random.randint(50, 150)  # Food disappears after some time

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.size, self.size))
    
    def update_timer(self):
        self.timer -= 1

# Initialize variables
food_list = [Food()]
score = 0
running = True
clock = pygame.time.Clock()

# Game loop
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)
    snake.pop()
    
    # Check for food collision
    for food in food_list[:]:
        if pygame.Rect(food.x, food.y, food.size, food.size).colliderect(pygame.Rect(snake[0][0], snake[0][1], 20, 20)):
            score += food.value
            snake.append(snake[-1])  # Grow snake
            food_list.remove(food)
            food_list.append(Food())
    
    # Remove food if timer runs out
    for food in food_list[:]:
        food.update_timer()
        if food.timer <= 0:
            food_list.remove(food)
            food_list.append(Food())
    
    # Draw food
    for food in food_list:
        food.draw()
    
    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], 20, 20))
    
    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(speed)

pygame.quit()