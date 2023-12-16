import pygame
import sys
import random
import os
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
OBJECT_SIZE = 50
FALL_SPEED = 2
BUCKET_WIDTH = 100
BUCKET_HEIGHT = 50
SCORE_FONT_SIZE = 36
STAR_SIZE = 30
GLOW_DURATION = 1
STAR_ANIMATION_DELAY = 1
STAR_SPACING = 50
ANIMATION_DURATION = 750

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Falling Objects Game")
clock = pygame.time.Clock()

# Load object images
object_images_path_type1 = "path/to/your/object/images/type1"
object_images_path_type2 = "path/to/your/object/images/type2"

object_type1_images = [pygame.image.load(os.path.join("C:\\Users\\Srimanth\\Downloads\\img", filename)) for filename in
                       os.listdir("C:\\Users\\Srimanth\\Downloads\\img")]
object_type1_images = [pygame.transform.scale(image, (OBJECT_SIZE, OBJECT_SIZE)) for image in object_type1_images]

object_type2_images = [pygame.image.load(os.path.join("C:\\Users\\Srimanth\\Downloads\\img1", filename)) for filename in
                       os.listdir("C:\\Users\\Srimanth\\Downloads\\img1")]
object_type2_images = [pygame.transform.scale(image, (OBJECT_SIZE, OBJECT_SIZE)) for image in object_type2_images]

# Load star images
glowing_star_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\hi.png")
dull_star_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\hi1.png")
glowing_star_image = pygame.transform.scale(glowing_star_image, (STAR_SIZE, STAR_SIZE))
dull_star_image = pygame.transform.scale(dull_star_image, (STAR_SIZE, STAR_SIZE))

# Load background image
background_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\xx (2).jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Falling object properties
falling_objects = []
last_object_time_type1 = time.time()
last_object_time_type2 = time.time()

# Bucket properties
bucket_rect = pygame.Rect(WIDTH // 2 - BUCKET_WIDTH // 2, HEIGHT - BUCKET_HEIGHT - 20, BUCKET_WIDTH, BUCKET_HEIGHT)

# Score variables
score = 0
glowing_stars = 0
dull_stars = 0
last_star_time = time.time()

# Timer variables
start_time = time.time()
game_duration = 60

# Font for scoring
score_font = pygame.font.Font(None, SCORE_FONT_SIZE)

# Restart and Quit buttons
restart_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50)
quit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)
resume_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)

# Animation variables
animations = []

# Game state
game_paused = False
pause_menu_active = False

# Function to display stars with animation
def display_stars_with_animation():
    total_star_width = glowing_stars * (STAR_SIZE + STAR_SPACING) + dull_stars * (STAR_SIZE + STAR_SPACING) - STAR_SPACING
    start_x = WIDTH // 2 - total_star_width // 2

    for i in range(glowing_stars):
        screen.blit(glowing_star_image, (start_x + i * (STAR_SIZE + STAR_SPACING), HEIGHT // 5))

    for i in range(glowing_stars, glowing_stars + dull_stars):
        screen.blit(dull_star_image, (start_x + i * (STAR_SIZE + STAR_SPACING), HEIGHT // 5))

# Function to display +1/-1 animation
def display_animation(text, x, y, color, alpha):
    animation_text = score_font.render(text, True, (color[0], color[1], color[2], alpha))
    screen.blit(animation_text, (x, y))

# Function to handle pause menu
def show_pause_menu():
    pygame.draw.rect(screen, (0, 0, 0, 150), (0, 0, WIDTH, HEIGHT))  # Semi-transparent background
    pygame.draw.rect(screen, (255, 0, 0), resume_button_rect)
    pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)
    resume_text = score_font.render("Resume", True, (255, 255, 255))
    quit_text = score_font.render("Quit", True, (255, 255, 255))
    screen.blit(resume_text, resume_button_rect.topleft)
    screen.blit(quit_text, quit_button_rect.topleft)

MAX_LIVES = 3
current_lives = MAX_LIVES
bright_life_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\xxx.png")
dim_life_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\xxx1.png")
life_image_size = (20, 20)
bright_life_image = pygame.transform.scale(bright_life_image, life_image_size)
dim_life_image = pygame.transform.scale(dim_life_image, life_image_size)

# Position of life images
life_image_spacing = 5
life_images_top = 10
start_x = WIDTH // 2 - (MAX_LIVES * (life_image_size[0] + life_image_spacing) - life_image_spacing) // 2

# Main game loop
bucket_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\mmm.png")
bucket_image = pygame.transform.scale(bucket_image, (BUCKET_WIDTH, BUCKET_HEIGHT))
bucket_image_size = (150, 75)
bucket_image = pygame.transform.scale(bucket_image, bucket_image_size)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if game_paused and pause_menu_active:
                if resume_button_rect.collidepoint(x, y):
                    game_paused = False
                    pause_menu_active = False
                elif quit_button_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()
            elif restart_button_rect.collidepoint(x, y):
                falling_objects = []
                last_object_time_type1 = time.time()
                last_object_time_type2 = time.time()
                score = 0
                glowing_stars = 0
                dull_stars = 0
                last_star_time = time.time()
                start_time = time.time()
                game_paused = False
                current_lives = MAX_LIVES
            elif quit_button_rect.collidepoint(x, y):
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if not game_paused:
                    game_paused = True
                    pause_menu_active = True
                else:
                    game_paused = False
                    pause_menu_active = False

    if game_paused:
        if pause_menu_active:
            show_pause_menu()
    else:
        screen.blit(background_image, (0, 0))

        elapsed_time = int(time.time() - start_time)
        remaining_time = max(0, game_duration - elapsed_time - 1)

        if elapsed_time <= 20:
            FALL_SPEED = 2
        elif 20 < elapsed_time <= 40:
            FALL_SPEED = 4
        else:
            FALL_SPEED = 6

        if remaining_time == 0 or current_lives == 0:
            if score > 25:
                glowing_stars = 5
                dull_stars = 0
            elif score > 20:
                glowing_stars = 4
                dull_stars = 1
            elif score > 15:
                glowing_stars = 3
                dull_stars = 2
            elif score > 10:
                glowing_stars = 2
                dull_stars = 3
            elif score > 5:
                glowing_stars = 1
                dull_stars = 4
            else:
                glowing_stars = 0
                dull_stars = 5

            display_stars_with_animation()
            pygame.draw.rect(screen, (255, 0, 0), restart_button_rect)
            pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)
            restart_text = score_font.render("Restart", True, (255, 255, 255))
            quit_text = score_font.render("Quit", True, (255, 255, 255))
            final_score_text = score_font.render(f"Final Score: {score}", True, (255, 255, 255))
            screen.blit(restart_text, restart_button_rect.topleft)
            screen.blit(quit_text, quit_button_rect.topleft)
            screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
        else:
            if time.time() - last_object_time_type1 > 2:
                new_object_rect = object_type1_images[0].get_rect()
                new_object_rect.x = random.randint(0, WIDTH - OBJECT_SIZE)
                new_object_rect.y = 0 - OBJECT_SIZE

                new_object = {'rect': new_object_rect, 'image': random.choice(object_type1_images)}
                falling_objects.append(new_object)
                last_object_time_type1 = time.time()

            if time.time() - last_object_time_type2 > 3:
                new_object_rect = object_type2_images[0].get_rect()
                new_object_rect.x = random.randint(0, WIDTH - OBJECT_SIZE)
                new_object_rect.y = 0 - OBJECT_SIZE

                new_object = {'rect': new_object_rect, 'image': random.choice(object_type2_images)}
                falling_objects.append(new_object)
                last_object_time_type2 = time.time()

            for obj in falling_objects:
                obj['rect'].centery += FALL_SPEED

            falling_objects = [obj for obj in falling_objects if obj['rect'].y < HEIGHT]

            mouse_x, mouse_y = pygame.mouse.get_pos()
            bucket_rect.centerx = mouse_x

            for i in range(MAX_LIVES):
                if i < current_lives:
                    screen.blit(bright_life_image, (start_x + i * (life_image_size[0] + life_image_spacing),
                                                     life_images_top))
                else:
                    screen.blit(dim_life_image, (start_x + i * (life_image_size[0] + life_image_spacing),
                                                  life_images_top))

            for obj in falling_objects:
                if bucket_rect.colliderect(obj['rect']):
                    falling_objects.remove(obj)
                    if obj['image'] in object_type1_images:
                        score += 1
                        animations.append({'text': '+1', 'x': random.randint(WIDTH // 4, 3 * WIDTH // 4),
                                          'y': random.randint(HEIGHT // 4, 3 * HEIGHT // 4),
                                          'color': (0, 255, 0), 'start_time': pygame.time.get_ticks()})
                    elif obj['image'] in object_type2_images:
                        current_lives -= 1
                        animations.append({'text': '-1', 'x': random.randint(WIDTH // 4, 3 * WIDTH // 4),
                                          'y': random.randint(HEIGHT // 4, 3 * HEIGHT // 4),
                                          'color': (255, 0, 0), 'start_time': pygame.time.get_ticks()})

            animations = [animation for animation in animations if pygame.time.get_ticks() - animation['start_time'] < ANIMATION_DURATION]

            for obj in falling_objects:
                screen.blit(obj['image'], obj['rect'].topleft)

            screen.blit(bucket_image, bucket_rect.topleft)

            score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            timer_text = score_font.render(f"Time: {remaining_time}", True, (255, 255, 255))
            screen.blit(timer_text, (WIDTH - 150, 10))

            for animation in animations:
                elapsed_time = pygame.time.get_ticks() - animation['start_time']
                alpha = max(0, 255 - elapsed_time / 5)
                display_animation(animation['text'], animation['x'], animation['y'], animation['color'], alpha)

            animations = [animation for animation in animations if pygame.time.get_ticks() - animation['start_time'] < 750]

    pygame.display.flip()
    clock.tick(FPS)


