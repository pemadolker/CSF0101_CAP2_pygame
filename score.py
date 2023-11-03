import pygame
import random
import os

# Initialize pygame
pygame.init()

# Game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jumpy')

# Set frame rate
clock = pygame.time.Clock()
FPS = 60

# Game variables
SCROLL_THRESH = 200
GRAVITY = 1
scroll = 0
bg_scroll = 0
game_over = False
score = 0
fade_counter = 0

if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
        high_score = int(file.read())
else:
    high_score = 0

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PANEL = (153, 217, 234)

# Define fonts
font_small = pygame.font.SysFont('Lucida Sans', 18)
font_big = pygame.font.SysFont('Lucida Sans', 22)

# Load images 
jumpy_image = pygame.image.load(r'C:\Users\DELL\Downloads\unicorn_1049948.png').convert_alpha()
bg_image = pygame.image.load(r'C:\Users\DELL\Downloads\i need.jpg').convert_alpha()
platform_image = pygame.image.load(r'C:\Users\DELL\Desktop\platform.jpg').convert_alpha()
#bird
bird_sheet_img = pygame.image.load(r'C:\Users\DELL\Downloads\chick.png').convert_alpha()


# Function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Function for drawing the background
def draw_bg(bg_scroll):
    screen.blit(bg_image, (0, 0 + bg_scroll))
    screen.blit(bg_image, (0, -600 - bg_scroll))

class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(jumpy_image, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False

    def move(self):
        # Reset variables
        scroll = 0
        dx = 0
        dy = 0

        # Process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            dx = 10
            self.flip = True
        if key[pygame.K_LEFT]:
            dx = 10
            self.flip = False

        # Gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # Ensure player doesn't go off the edge of the screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

        # Update rectangle position
        self.rect.x += dx
        self.rect.y += dy + scroll

        return scroll

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 9, self.rect.y - 6))
        pygame.draw.rect(screen, WHITE, self.rect, 1)

# Create a player instance
jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

# Game loop
run = True
while run:
    clock.tick(FPS)

    if game_over == False:
        scroll = jumpy.move()

        # Draw background
        bg_scroll += scroll
        if bg_scroll >= 600:
            bg_scroll = 0
        draw_bg(bg_scroll)

        # Update score
        if scroll > 0:
            score += scroll

        # Draw line at previous high score
        pygame.draw.line(screen, WHITE, (0, score - high_score + SCROLL_THRESH), (SCREEN_WIDTH, score - high_score + SCROLL_THRESH), 3)
        draw_text('HIGH SCORE', font_small, WHITE, SCREEN_WIDTH - 130, score - high_score + SCROLL_THRESH)

        # Draw player
        jumpy.draw()

        # Draw panel
        pygame.draw.rect(screen, PANEL, (0, 0, SCREEN_WIDTH, 30))
        pygame.draw.line(screen, WHITE, (0, 30), (SCREEN_WIDTH, 30), 2)
        draw_text('SCORE: ' + str(score), font_small, WHITE, 0, 0)

        # Check game over
        if jumpy.rect.top > SCREEN_HEIGHT:
            game_over = True

    else:
        if fade_counter < SCREEN_WIDTH:
            fade_counter += 5
            for y in range(0, 6, 2):
                pygame.draw.rect(screen, BLACK, (0, y * 100, fade_counter, 100))
                pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - fade_counter, (y + 1)))
        else:
            draw_text('GAME OVER!', font_big, WHITE, 130, 200)
            draw_text('SCORE: ' + str(score), font_big, WHITE, 130, 250)
            draw_text('PRESS SPACE TO PLAY AGAIN', font_big, WHITE, 40, 300)
            # Update high score
            if score > high_score:
                high_score = score
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                # Reset variables
                game_over = False
                score = 0
                scroll = 0
                fade_counter = 0
                # Reposition jumpy
                jumpy.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Update high score
            if score == high_score:
                high_score = score
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))
            run = False

pygame.quit()