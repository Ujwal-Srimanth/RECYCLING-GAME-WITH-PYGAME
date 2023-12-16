import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Game state
current_page = "welcome"

# Functions
def draw_text(text, color, x, y):
    surface = FONT.render(text, True, color)
    screen.blit(surface, (x, y))

def welcome_page():
    screen.fill(WHITE)
    draw_text("Welcome to Recycling Game", BLACK, WIDTH // 4, HEIGHT // 2 - 50)
    # Add animations here
    # Draw start button
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 50, HEIGHT // 2 + 50, 100, 50))
    draw_text("Start", WHITE, WIDTH // 2 - 25, HEIGHT // 2 + 60)

def level_select_page():
    screen.fill(WHITE)
    draw_text("Select Level", BLACK, WIDTH // 4, HEIGHT // 2 - 50)
    # Draw buttons for easy and hard levels
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 100, HEIGHT // 2, 200, 50))
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50))
    draw_text("Easy", WHITE, WIDTH // 2 - 30, HEIGHT // 2 + 10)
    draw_text("Hard", WHITE, WIDTH // 2 - 30, HEIGHT // 2 + 110)

def game_page(level):
    screen.fill(WHITE)
    draw_text("Game Page - Level: {}".format(level), BLACK, WIDTH // 4, HEIGHT // 2 - 50)
    # Implement game logic here

def settings_page():
    screen.fill(WHITE)
    draw_text("Settings", BLACK, WIDTH // 4, HEIGHT // 2 - 50)
    # Draw buttons for resume and quit
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 100, HEIGHT // 2, 200, 50))
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50))
    draw_text("Resume", WHITE, WIDTH // 2 - 40, HEIGHT // 2 + 10)
    draw_text("Quit", WHITE, WIDTH // 2 - 20, HEIGHT // 2 + 110)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recycling Game")
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if current_page == "welcome":
                if WIDTH // 2 - 50 <= x <= WIDTH // 2 + 50 and HEIGHT // 2 + 50 <= y <= HEIGHT // 2 + 100:
                    current_page = "level_select"
            elif current_page == "level_select":
                if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT // 2 <= y <= HEIGHT // 2 + 50:
                    current_page = "game_easy"
                elif WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT // 2 + 100 <= y <= HEIGHT // 2 + 150:
                    current_page = "game_hard"
            elif current_page == "settings":
                if WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT // 2 <= y <= HEIGHT // 2 + 50:
                    current_page = "game_resume"
                elif WIDTH // 2 - 100 <= x <= WIDTH // 2 + 100 and HEIGHT // 2 + 100 <= y <= HEIGHT // 2 + 150:
                    pygame.quit()
                    sys.exit()

    if current_page == "welcome":
        welcome_page()
    elif current_page == "level_select":
        level_select_page()
    elif current_page == "game_easy":
        game_page("Easy")
    elif current_page == "game_hard":
        game_page("Hard")
    elif current_page == "settings":
        settings_page()

    pygame.display.flip()
    clock.tick(FPS)
