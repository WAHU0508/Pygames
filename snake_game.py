import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Game variables
block_size = 20
snake = [[100, 50], [80, 50], [60, 50]]
snake_direction = 'RIGHT'
food_x = random.randint(0, (WIDTH - block_size) // block_size) * block_size
food_y = random.randint(0, (HEIGHT - block_size) // block_size) * block_size
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Game over function
def game_over():
    game_over_text = font.render("Game Over!", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Snake direction control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != 'DOWN':
        snake_direction = 'UP'
    if keys[pygame.K_DOWN] and snake_direction != 'UP':
        snake_direction = 'DOWN'
    if keys[pygame.K_LEFT] and snake_direction != 'RIGHT':
        snake_direction = 'LEFT'
    if keys[pygame.K_RIGHT] and snake_direction != 'LEFT':
        snake_direction = 'RIGHT'

    # Move the snake
    head = snake[0]
    if snake_direction == 'UP':
        new_head = [head[0], head[1] - block_size]
    elif snake_direction == 'DOWN':
        new_head = [head[0], head[1] + block_size]
    elif snake_direction == 'LEFT':
        new_head = [head[0] - block_size, head[1]]
    elif snake_direction == 'RIGHT':
        new_head = [head[0] + block_size, head[1]]

    # Add new head
    snake.insert(0, new_head)

    # Check if snake eats the food
    if snake[0][0] == food_x and snake[0][1] == food_y:
        score += 1
        food_x = random.randint(0, (WIDTH - block_size) // block_size) * block_size
        food_y = random.randint(0, (HEIGHT - block_size) // block_size) * block_size
    else:
        snake.pop()

    # Check if snake hits itself or walls
    if (
        new_head in snake[1:]
        or new_head[0] < 0
        or new_head[0] >= WIDTH
        or new_head[1] < 0
        or new_head[1] >= HEIGHT
    ):
        game_over()

    # Draw the food
    pygame.draw.rect(screen, RED, (food_x, food_y, block_size, block_size))
    # Draw the snake
    for block in snake:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], block_size, block_size))
    # Draw the score
    score_text = font.render(f"Score : {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    # Update display
    pygame.display.flip()
    # Control frame rate
    clock.tick(7)

# Quit game
pygame.quit()
sys.exit()
            
