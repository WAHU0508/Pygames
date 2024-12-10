import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15

# Speeds
BALL_SPEED = [4, 4]
PADDLE_SPEED = 6

# Clock
clock = pygame.time.Clock()

# Create Paddles and Ball
player1_paddle = pygame.Rect(20, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(WIDTH - 30, (HEIGHT // 2) - (PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)

# Scores
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 50)

def reset_ball():
    ball.x, ball.y = WIDTH // 2, HEIGHT // 2
    BALL_SPEED[0] *= -1  # Switch ball direction

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key Presses
    keys = pygame.key.get_pressed()
    # Player 1 controls
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_paddle.bottom < HEIGHT:
        player1_paddle.y += PADDLE_SPEED
    # Player 2 controls
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_paddle.bottom < HEIGHT:
        player2_paddle.y += PADDLE_SPEED

    # Ball movement
    ball.x += BALL_SPEED[0]
    ball.y += BALL_SPEED[1]

    # Ball collision with top/bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED[1] = -BALL_SPEED[1]

    # Ball collision with paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        BALL_SPEED[0] = -BALL_SPEED[0]

    # Ball out of bounds
    if ball.left <= 0:
        player2_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        player1_score += 1
        reset_ball()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1_paddle)
    pygame.draw.rect(screen, WHITE, player2_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display Scores
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (WIDTH // 4, 20))
    screen.blit(player2_text, (WIDTH * 3 // 4, 20))

    # Update the display
    pygame.display.flip()
    clock.tick(60)
