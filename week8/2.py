import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = (CELL_SIZE, 0)
        self.growing = False

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Check for collisions with walls
        if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
            return False  # Game over
        
        # Check for collisions with itself
        if new_head in self.body:
            return False  # Game over
        
        self.body.insert(0, new_head)
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False
        
        return True

    def grow(self):
        self.growing = True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

# Food class
class Food:
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)

    def generate_position(self, snake_body):
        while True:
            pos = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                   random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
            if pos not in snake_body:
                return pos

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, CELL_SIZE, CELL_SIZE))

# Main function
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food(snake.body)
    score = 0
    level = 1
    speed = FPS

    running = True
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, CELL_SIZE):
                    snake.direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -CELL_SIZE):
                    snake.direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and snake.direction != (CELL_SIZE, 0):
                    snake.direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-CELL_SIZE, 0):
                    snake.direction = (CELL_SIZE, 0)
        
        if not snake.move():
            break  # Game over
        
        if snake.body[0] == food.position:
            snake.grow()
            food = Food(snake.body)
            score += 1
            if score % 4 == 0:  # Increase level every 4 points
                level += 1
                speed += 2
        
        snake.draw()
        food.draw()
        
        # Display score and level
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))
        
        pygame.display.flip()
        clock.tick(speed)
    
    pygame.quit()

if __name__ == "__main__":
    main()