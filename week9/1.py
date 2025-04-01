import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Load assets
player_car = pygame.Rect(175, 500, 50, 100)
enemy_car = pygame.Rect(random.randint(50, 300), -100, 50, 100)
clock = pygame.time.Clock()

# Coin settings
class Coin:
    def __init__(self):
        self.x = random.randint(50, 350)
        self.y = random.randint(-600, -50)
        self.radius = random.choice([5, 10, 15])  # Different coin sizes/weights
        self.value = self.radius // 5  # Larger coins give more points

    def move(self, speed):
        self.y += speed

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x, self.y), self.radius)

# Initialize variables
coins = [Coin() for _ in range(5)]
score = 0
enemy_speed = 5
running = True

# Game loop
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move enemy car
    enemy_car.y += enemy_speed
    if enemy_car.y > HEIGHT:
        enemy_car.x = random.randint(50, 300)
        enemy_car.y = -100
    
    # Move and collect coins
    for coin in coins[:]:
        coin.move(3)
        if coin.y > HEIGHT:
            coins.remove(coin)
            coins.append(Coin())
        
        if player_car.colliderect(pygame.Rect(coin.x - coin.radius, coin.y - coin.radius, coin.radius*2, coin.radius*2)):
            score += coin.value
            coins.remove(coin)
            coins.append(Coin())
    
    # Increase enemy speed after collecting N coins
    if score >= 10:
        enemy_speed = 7
    if score >= 20:
        enemy_speed = 9
    
    # Draw objects
    pygame.draw.rect(screen, RED, player_car)
    pygame.draw.rect(screen, RED, enemy_car)
    for coin in coins:
        coin.draw()
    
    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
