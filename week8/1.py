import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
ROAD_WIDTH = 400
LANE_WIDTH = ROAD_WIDTH // 3
FPS = 60

# Colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Player class
class Player:
    def __init__(self):
        self.x = WIDTH // 2 - 25
        self.y = HEIGHT - 120
        self.speed = 5
        self.score = 0
        self.width = 50
        self.height = 100

    def move(self, direction):
        if direction == "left" and self.x > WIDTH//2 - ROAD_WIDTH//2:
            self.x -= LANE_WIDTH
        if direction == "right" and self.x < WIDTH//2 + ROAD_WIDTH//2 - self.width:
            self.x += LANE_WIDTH

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# Coin class
class Coin:
    def __init__(self):
        self.x = random.choice([
            WIDTH // 2 - ROAD_WIDTH // 2 + LANE_WIDTH // 2 - 15,
            WIDTH // 2 - 15,
            WIDTH // 2 + ROAD_WIDTH // 2 - LANE_WIDTH // 2 - 15
        ])
        self.y = -50
        self.speed = 5
        self.size = 30

    def move(self):
        self.y += self.speed

    def draw(self):
        pygame.draw.circle(screen, YELLOW, (self.x + self.size // 2, self.y + self.size // 2), self.size // 2)

# Main function
def main():
    clock = pygame.time.Clock()
    player = Player()
    coins = []
    running = True

    while running:
        screen.fill(GRAY)
        pygame.draw.rect(screen, YELLOW, (WIDTH//2 - ROAD_WIDTH//2, 0, ROAD_WIDTH, HEIGHT))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move("left")
                if event.key == pygame.K_RIGHT:
                    player.move("right")
        
        # Spawn coins
        if random.randint(1, 100) < 2:  # Low probability to add a new coin
            coins.append(Coin())
        
        # Move and draw coins
        for coin in coins[:]:
            coin.move()
            coin.draw()
            if coin.y > HEIGHT:
                coins.remove(coin)
            if pygame.Rect(player.x, player.y, player.width, player.height).colliderect(
               pygame.Rect(coin.x, coin.y, coin.size, coin.size)):
                player.score += 1
                coins.remove(coin)
        
        # Draw player
        player.draw()
        
        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Coins: {player.score}", True, WHITE)
        screen.blit(score_text, (WIDTH - 150, 20))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()
