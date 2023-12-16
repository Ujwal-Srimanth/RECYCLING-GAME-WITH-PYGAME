import pygame
import sys
import random
import os
import time
import math
import pymongo
from pymongo import MongoClient
import subprocess
temp=0
# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BLACK = (0, 0, 0)
OBJECT_SIZE = 52  # Increase the size of the objects
FALL_SPEED = 3  # Adjust the fall speed
past_state=-float("inf")
BUCKET_WIDTH =100
BUCKET_HEIGHT = 80
SCORE_FONT_SIZE = 36
count11=0
STAR_SIZE = 30
GLOW_DURATION = 1  # Duration of the glowing effect in seconds
STAR_ANIMATION_DELAY = 1  # Delay between displaying stars in seconds
STAR_SPACING = 50  # Spacing between stars
ANIMATION_DURATION = 750  # Duration of +1/-1 animation in milliseconds
# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Objects Game")
clock = pygame.time.Clock()
# Load object images
object_images_path_type1 = "path/to/your/object/images/type1"
object_images_path_type2 = "path/to/your/object/images/type2"
object_type1_images = [pygame.image.load(os.path.join("img1", filename)) for filename in os.listdir("img1")]
object_type1_images = [pygame.transform.scale(image, (OBJECT_SIZE, OBJECT_SIZE)) for image in object_type1_images]
object_type2_images = [pygame.image.load(os.path.join("img2", filename)) for filename in os.listdir("img2")]
object_type2_images = [pygame.transform.scale(image, (OBJECT_SIZE, OBJECT_SIZE)) for image in object_type2_images]
object_type3_images = [pygame.image.load(os.path.join("img3", filename)) for filename in os.listdir("img3")]
object_type3_images = [pygame.transform.scale(image, (OBJECT_SIZE, OBJECT_SIZE)) for image in object_type3_images]
object_type4_images = [pygame.image.load(os.path.join("img4", filename)) for filename in os.listdir("img4")]
object_type4_images = [pygame.transform.scale(image, (OBJECT_SIZE, OBJECT_SIZE)) for image in object_type4_images]
object_type5_images = [pygame.image.load(os.path.join("img5", filename)) for filename in os.listdir("img5")]
object_type5_images = [pygame.transform.scale(image, (OBJECT_SIZE, OBJECT_SIZE)) for image in object_type5_images]
object_type6_images = [pygame.image.load(os.path.join("img6", filename)) for filename in os.listdir("img6")]
object_type6_images = [pygame.transform.scale(image, (OBJECT_SIZE, OBJECT_SIZE)) for image in object_type6_images]

bucket_images = [pygame.image.load(os.path.join("DUST BIN", filename)) for filename in os.listdir("DUST BIN")]
bucket_images = [pygame.transform.scale(image, (OBJECT_SIZE, OBJECT_SIZE)) for image in bucket_images]
current_bucket_index = 0
bucket_image_size = (BUCKET_WIDTH, BUCKET_HEIGHT)
bucket_rect = pygame.Rect(WIDTH // 2 - BUCKET_WIDTH // 2, HEIGHT - BUCKET_HEIGHT - 160, BUCKET_WIDTH, BUCKET_HEIGHT)
bucket_image = pygame.transform.scale(bucket_images[current_bucket_index], bucket_image_size)
def change_bucket():
    global current_bucket_index
    current_bucket_index = (current_bucket_index + 1) % len(bucket_images)
    bucket_image = pygame.transform.scale(bucket_images[current_bucket_index], bucket_image_size)

score_font = pygame.font.Font(None, SCORE_FONT_SIZE)
bucket_text_font = pygame.font.Font(None, 24)

# Load star images
glowing_star_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\hi.png")
dull_star_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\hi1.png")
glowing_star_image = pygame.transform.scale(glowing_star_image, (STAR_SIZE, STAR_SIZE))
dull_star_image = pygame.transform.scale(dull_star_image, (STAR_SIZE, STAR_SIZE))
# Load background image
background_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\xx (10).jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
background_image1 = pygame.image.load("aaa.jpg")
background_image1= pygame.transform.scale(background_image1, (WIDTH, HEIGHT))
background_image2 = pygame.image.load("bbb.jpg")
background_image2 = pygame.transform.scale(background_image2, (WIDTH, HEIGHT))
background_image3 = pygame.image.load("ccc.jpg")
background_image3 = pygame.transform.scale(background_image3, (WIDTH, HEIGHT))
def something():
    health = db['heatlh']
    pipeline = [
        {"$group": {"_id": None, "total_health": {"$sum": "$health"}}}
    ]

    result = list(health.aggregate(pipeline))

    # Check if there is a result
    total_score = result[0]["total_health"]
    if total_score > 0:
        document_to_insert = {
                'health': -1,
    # Add more key-value pairs as needed
                        }
        health.insert_one(document_to_insert)

def something2():
    health = db['heatlh']
    pipeline = [
        {"$group": {"_id": None, "total_health": {"$sum": "$health"}}}
    ]

    result = list(health.aggregate(pipeline))

    # Check if there is a result
    total_score = result[0]["total_health"]
   
    return total_score
def something3():
    health = db['time']
    pipeline = [
        {"$group": {"_id": None, "total_health": {"$sum": "$speed"}}}
    ]

    result = list(health.aggregate(pipeline))

    # Check if there is a result
    total_score = result[0]["total_health"]
   
    return total_score
def something1():
    time = db['time']
    pipeline = [
        {"$group": {"_id": None, "total_health": {"$sum": "$speed"}}}
    ]

    result = list(time.aggregate(pipeline))

    # Check if there is a result
    total_score = result[0]["total_health"]
    if total_score > 0:
        document_to_insert = {
                'speed': -1,
    # Add more key-value pairs as needed
                        }
        time.insert_one(document_to_insert)

    pipeline = [
        {"$group": {"_id": None, "total_health": {"$sum": "$speed"}}}
    ]

    result = list(time.aggregate(pipeline))

    # Check if there is a result
    total_score = result[0]["total_health"]
    return total_score

# Load power-up images
powerup_increase_lives_image = pygame.image.load("life.png")
powerup_decrease_speed_image = pygame.image.load("life2.png")

# Scale the power-up images to an appropriate size
powerup_increase_lives_image = pygame.transform.scale(powerup_increase_lives_image, (50, 50))
powerup_decrease_speed_image = pygame.transform.scale(powerup_decrease_speed_image, (50, 50))

# Set initial positions for the power-up images
powerup_increase_lives_rect = powerup_increase_lives_image.get_rect(topleft=(50, HEIGHT - 100))
powerup_decrease_speed_rect = powerup_decrease_speed_image.get_rect(topleft=(120, HEIGHT - 100))


pine1_img = pygame.image.load('img/Background/pine1.png').convert_alpha()
pine2_img = pygame.image.load('img/Background/pine2.png').convert_alpha()
mountain_img = pygame.image.load('img/Background/mountain.png').convert_alpha()
sky_img = pygame.image.load('img/Background/sky_cloud.png').convert_alpha()
#store tiles in a list
TILE_TYPES = 21
ROWS = 16
bg_scroll = 0
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
TILE_SIZE = SCREEN_HEIGHT // ROWS

BG = (144, 201, 120)
img_list = []
def draw_bg():
	screen.fill(BG)
	width = sky_img.get_width()
	for x in range(5):
		screen.blit(sky_img, ((x * width) - bg_scroll * 0.5, 0))
		screen.blit(mountain_img, ((x * width) - bg_scroll * 0.6, SCREEN_HEIGHT - mountain_img.get_height() - 300))
		screen.blit(pine1_img, ((x * width) - bg_scroll * 0.7, SCREEN_HEIGHT - pine1_img.get_height() - 150))
		screen.blit(pine2_img, ((x * width) - bg_scroll * 0.8, SCREEN_HEIGHT - pine2_img.get_height()))
# Falling object properties
falling_objects = []
last_object_time_type1 = time.time()
last_object_time_type2 = time.time()
last_object_time_type3 = time.time()
last_object_time_type4 = time.time()
last_object_time_type5 = time.time()
last_object_time_type6 = time.time()
# Bucket properties
bucket_rect = pygame.Rect(WIDTH // 2 - BUCKET_WIDTH // 2, HEIGHT - BUCKET_HEIGHT - 20, BUCKET_WIDTH, BUCKET_HEIGHT)
# Score variables
score = 0
glowing_stars = 0
dull_stars = 0
last_star_time = time.time()
# Timer variables
start_time = time.time()
game_duration = 70  # seconds
plays = 0
# Font for scoring
score_font = pygame.font.Font(None, SCORE_FONT_SIZE)
# Restart and Quit buttons
restart_button_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\restart.png")
restart_button_size = (200, 50)  # Adjust the size as needed
restart_button_image = pygame.transform.scale(restart_button_image, restart_button_size)
restart_button_rect = pygame.Rect(WIDTH // 2 - restart_button_size[0] // 2, HEIGHT // 2 + 50, restart_button_size[0], restart_button_size[1])
quit_button_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\quit.png")
quit_button_image = pygame.transform.scale(quit_button_image, (200, 50))  # Adjust the size as needed
quit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)
resume_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
quit1_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)
# Animation variables
animations = []
# Game state
game_paused = False
pause_menu_active = False
instructions_font = pygame.font.Font(None, 24)
instructions_text = [
    "Welcome to the Waste segregation level!",
    "Catch the falling objects with the bucket.",
    "Use the mouse to move the bucket left and right.",
    "Use C button to click change the bucket.",
    "If a particular type waste is caught with that bucket score is +1",
    "if wrong object is caught the live decreases"
    "You have 3 lives. Game ends if lives reach 0.",
    "Get the highest score before the time runs out!",
    "Stars indicate your performance at the end.",
    "a score close to 10 is amazing score and u would be a master in segregation",
    "Press ESC to pause the game.",
]
def get_average_score():
    scores = collection.find({}, {'final_score': 1, '_id': 0})
    scores = [score['final_score'] for score in scores]
    if scores:
        average_score = sum(scores) / len(scores)
        return round(average_score, 2)
    return 0
start_time_instructions = time.time()
# Display instructions for 10 seconds
while time.time() - start_time_instructions < 10:
    screen.blit(background_image, (0,0))
    # Create a semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (0, 0, 0, 150), (0, 0, WIDTH, HEIGHT))
    screen.blit(overlay, (0, 0))
    # Display instructions
    for i, line in enumerate(instructions_text):
        text = instructions_font.render(line, True, (255, 255, 255))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - len(instructions_text) * 12 + i * 24))
    pygame.display.update()  # Update the display
    clock.tick(FPS)
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
    resume_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
    quit1_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 50)
    pygame.draw.rect(screen, (255, 0, 0), resume_button_rect)
    pygame.draw.rect(screen, (255, 0, 0), quit1_button_rect)
    resume_text = score_font.render("Resume", True, (255, 255, 255))
    quit_text = score_font.render("Quit", True, (255, 255, 255))
    screen.blit(resume_text, resume_button_rect.topleft)
    screen.blit(quit_text, quit1_button_rect.topleft)
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
# bucket_image = pygame.image.load("C:\\Users\\Srimanth\\Downloads\\mmm.png")
# bucket_image = pygame.transform.scale(bucket_image, (BUCKET_WIDTH, BUCKET_HEIGHT))
# bucket_image_size = (150, 75)  # Adjust the size as needed
# bucket_image = pygame.transform.scale(bucket_image, bucket_image_size)
def choose_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b
class Streak():
    def __init__(self, x, y):
        self.color = choose_random_color()
        self.x = x
        self.y = y
        angle = random.uniform(-60, 240)
        velocity_mag = random.uniform(.3, 2.5)
        self.vx = velocity_mag*math.cos(math.radians(angle))  #velocity x
        self.vy = -velocity_mag*math.sin(math.radians(angle))  #velocity y
        self.timer = 0
        self.ended = False
    def get_angle(self):
        return math.atan2(-self.vy, self.vx)
    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.timer += 1
        if self.timer >= 90:
            self.ended = True
    def draw(self):
        angle = self.get_angle()
        length = 1
        dx = length*math.cos(angle)
        dy = length*math.sin(angle)
        a = [int(self.x+dx), int(self.y-dy)]
        b = [int(self.x-dx), int(self.y+dy)]
        pygame.draw.line(screen, self.color, a, b, 1)
class Firework():
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = 600
        self.velocity = random.uniform(3.5, 7)
        self.end_y = random.uniform(10, 300)
        self.ended = False
        self.start_time = pygame.time.get_ticks()
    def move(self):
        self.y -= self.velocity
        if self.y <= self.end_y or pygame.time.get_ticks() - self.start_time >= 2000:  # Adjust the duration as needed (2000 milliseconds = 2 seconds)
            self.ended = True
    def draw(self):
        a = [self.x, int(self.y + 15)]
        b = [self.x, int(self.y - 15)]
        pygame.draw.line(screen, (128, 128, 128), a, b, 4)
def game():
    fireworks = [Firework()]
    streaks = []
    fireworks_start_time = pygame.time.get_ticks()  # Store the start time of fireworks
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if random.uniform(0, 1) <= 1 / 60:
            fireworks.append(Firework())
        for firework in fireworks:
            firework.move()
            firework.draw()
            if firework.ended:
                streaks += [Streak(firework.x, firework.y) for _ in range(random.randint(20, 40))]
                fireworks.remove(firework)
        for streak in streaks:
            streak.move()
            streak.draw()
            if streak.ended:
                streaks.remove(streak)
        # Check if the fireworks should stop after 3 seconds
        elapsed_time = pygame.time.get_ticks() - fireworks_start_time
        if elapsed_time >= 9000:  # Adjust the duration as needed (3000 milliseconds = 3 seconds)
            break
        pygame.display.update()
        clock.tick(FPS)
button_font = pygame.font.Font(None, 30)
button_color = (255, 0, 0)
button_hover_color = (200, 0, 0)
def draw_button(rect, text, font_color):
    pygame.draw.rect(screen, button_color, rect)
    button_text = button_font.render(text, True, font_color)
    text_rect = button_text.get_rect(center=rect.center)
    screen.blit(button_text, text_rect)

flag=0
client = MongoClient('mongodb://localhost:27017')  # Update with your MongoDB connection string
db = client['your_database_name']  # Update with your database name
collection = db['your_collection_name']
collection1 = db['level2']  # Update with your collection name
# Function to save final score to MongoDB
def save_final_score(score):
    data = {'final_score': score}
    collection.insert_one(data)
    collection1.insert_one(data)

DIFFICULTY_CHECK_INTERVAL = 10  # seconds
last_difficulty_check_time = time.time()
# Adjusting difficulty
def display_message(message, duration):
    message_font = pygame.font.Font(None, 30)
    message_text = message_font.render(message, True, (255, 255, 255))
    screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.delay(1000)  # Display the message for 1 second
    pygame.draw.rect(screen, BLACK, (WIDTH // 2 - message_text.get_width() // 2, HEIGHT // 2, message_text.get_width(), message_text.get_height()))
    pygame.display.flip()
m = [0,0,0]
def handle_powerup_click(x, y):
    global current_lives, FALL_SPEED, powerup_1_count, powerup_2_count
    if powerup_increase_lives_rect.collidepoint(x, y):
        rem = something()
        # Handle increase lives power-up
        print("Increasing")

        current_lives += 1
    elif powerup_decrease_speed_rect.collidepoint(x, y):
        # Handle decrease speed power-up
        rem1 = something1()
        print("decreasing")
        FALL_SPEED -= 3 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
               
                if game_paused and pause_menu_active:
                    if resume_button_rect.collidepoint(x, y):
                        # Resume the game
                        game_paused = False
                        pause_menu_active = False
                    if quit1_button_rect.collidepoint(x, y):
                        # Ask for confirmation before quitting
                        pygame.quit()
                        sys.exit()
                elif quit_button_rect.collidepoint(x, y):
                        # Ask for confirmation before quitting
                    confirm_quit_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2 - 50, WIDTH // 2, 100)
                    pygame.draw.rect(screen, (0, 0, 0, 150), confirm_quit_rect)
                    draw_button(pygame.Rect(WIDTH // 4 + 20, HEIGHT // 2 - 20, WIDTH // 4 - 40, 40), "Yes", (255, 255, 255))
                    draw_button(pygame.Rect(WIDTH // 2, HEIGHT // 2 - 20, WIDTH // 4 - 40, 40), "No", (255, 255, 255))
                    confirm_quit_text = button_font.render("Are you sure you want to quit?", True, (255, 255, 255))
                    screen.blit(confirm_quit_text, (WIDTH // 4 + 10, HEIGHT // 2 - 40))
                    pygame.display.flip()
                    # Wait for user response
                    waiting_for_response = True
                    while waiting_for_response:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = pygame.mouse.get_pos()
                                if pygame.Rect(WIDTH // 4 + 20, HEIGHT // 2 - 20, WIDTH // 4 - 40, 40).collidepoint(x, y):
                                    pygame.quit()
                                    sys.exit()
                                elif pygame.Rect(WIDTH // 2, HEIGHT // 2 - 20, WIDTH // 4 - 40, 40).collidepoint(x, y):
                                    waiting_for_response = False
                    confirm_quit_rect = pygame.Rect(0, 0, 0, 0)  # Hide the confirmation dialog
                elif restart_button_rect.collidepoint(x, y):
                    # Ask for confirmation before restarting
                    confirm_restart_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2 - 50, WIDTH // 2, 100)
                    pygame.draw.rect(screen, (0, 0, 0, 150), confirm_restart_rect)
                    draw_button(pygame.Rect(WIDTH // 4 + 20, HEIGHT // 2 - 20, WIDTH // 4 - 40, 40), "Yes", (255, 255, 255))
                    draw_button(pygame.Rect(WIDTH // 2, HEIGHT // 2 - 20, WIDTH // 4 - 40, 40), "No", (255, 255, 255))
                    confirm_restart_text = button_font.render("Are you sure you want to restart?", True, (255, 255, 255))
                    screen.blit(confirm_restart_text, (WIDTH // 4 + 10, HEIGHT // 2 - 40))
                    pygame.display.flip()
                    # Wait for user response
                    waiting_for_response = True
                    while waiting_for_response:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = pygame.mouse.get_pos()
                                if pygame.Rect(WIDTH // 4 + 20, HEIGHT // 2 - 20, WIDTH // 4 - 40, 40).collidepoint(x, y):
                                    # Restart the game
                                    falling_objects = []
                                    last_object_time_type1 = time.time()
                                    last_object_time_type2 = time.time()
                                    score = 0
                                    m = [0,0,0]
                                    glowing_stars = 0
                                    dull_stars = 0
                                    count11 = 0
                                    past_score = -float("inf")
                                    last_star_time = time.time()
                                    start_time = time.time()
                                    FALL_SPEED = 3
                                    game_paused = False
                                    last_difficulty_check_time=0
                                    plays = 1
                                    current_lives = MAX_LIVES
                                    waiting_for_response = False
                                elif pygame.Rect(WIDTH // 2, HEIGHT // 2 - 20, WIDTH // 4 - 40, 40).collidepoint(x, y):
                                    waiting_for_response = False
                    confirm_restart_rect = pygame.Rect(0, 0, 0, 0) 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Toggle pause state
                game_paused = not game_paused
                pause_menu_active = True 
            elif event.key == pygame.K_DELETE:
            # Implement the redirection logic here
            # For example, open a new URL in a web browser
                subprocess.run(["python", "game.py"])
            elif event.key == pygame.K_b:
                    if current_lives < 3:
                
                        rem = something()
        # Handle increase lives power-up
                        print("Increasing")
                        current_lives += 1
            elif event.key == pygame.K_n:
                
        # Handle increase lives power-up
                if FALL_SPEED > 4:
                    FALL_SPEED -= 3
                    rem = something1()
                elif FALL_SPEED > 1:
                    FALL_SPEED -= 1
                    rem = something1()
            elif event.key == pygame.K_c:
                change_bucket()


            
    if game_paused:
        if pause_menu_active:
            # Display pause menu
            show_pause_menu()
        else:
            # Display pause message
            pause_text = score_font.render("Game Paused", True, (255, 255, 255))
            screen.blit(pause_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
    else:
        # Draw background
        waste = ['EWASTE','GLASS','METAL','ORGANIK','PAPER','PLASTIC']
        bucket_text = waste[current_bucket_index]
        bucket_text_render = score_font.render(bucket_text, True, (25,25,25))
    # Display bucket index text
       
        if score < 6:
            screen.blit(background_image1, (0, 0))
        elif 6 <= score <= 14:
            screen.blit(background_image2, (0, 0))
        elif score > 14:
            screen.blit(background_image3, (0, 0))
        screen.blit(powerup_increase_lives_image, (50, 50))
        screen.blit(powerup_decrease_speed_image, (150, 50))
        screen.blit(bucket_text_render, (350,50))
        font = pygame.font.Font(pygame.font.get_default_font(), 36)
    # Display power-up counts
        text_1 = font.render(str(something2()), True, BLACK)
        text_2 = font.render(str(something3()), True, BLACK)
        screen.blit(text_1, (100, 50))
        screen.blit(text_2, (200, 50))
        # Draw background
        # Check if the game time is up
        elapsed_time = int(time.time() - start_time)
        remaining_time = max(0, game_duration - elapsed_time - 1)
        # Update FALL_SPEED based on elapsed time
        if remaining_time == 0 or current_lives == 0:
            # Calculate the star rating based on the score
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
            # Draw stars after the game ends
            display_stars_with_animation()
            screen.blit(restart_button_image, restart_button_rect.topleft)
            screen.blit(quit_button_image, quit_button_rect.topleft)
            #pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)
            #restart_text = score_font.render("Restart", True, (255, 255, 255))
            #quit_text = score_font.render("Quit", True, (255, 255, 255))
            final_score_text = score_font.render(f"Final Score: {score}", True, (139, 69, 19))
            screen.blit(final_score_text, (WIDTH // 2 - 80, HEIGHT // 2 - 50))
            save_final_score(score)
        # Fetch and display the highest score from MongoDB
            highest_score = collection1.find_one(sort=[("final_score", pymongo.DESCENDING)])
            if highest_score:
                highest_score_text = score_font.render(f"Highest Score: {highest_score['final_score']}", True, (139, 69, 19))  # Dark brown color
                highest_score_rect = highest_score_text.get_rect(center=(WIDTH // 2 , HEIGHT // 2 + 20 ))  # Adjust the vertical position as needed
                screen.blit(highest_score_text, highest_score_rect.topleft)
            if glowing_stars >= 3 or glowing_stars==5:
                if flag==0:
                    flag=1
                    game()
            # Display firecracker burst animation
            #screen.blit(restart_text, restart_button_rect.topleft)
            #screen.blit(quit_text, quit_button_rect.topleft)
        else:
            # Add new objects periodically only if the game is still running
            if time.time() - last_object_time_type1 > 10:
                new_object_rect = object_type1_images[0].get_rect()
                # Set the initial position randomly along the top edge
                new_object_rect.x = random.randint(0, WIDTH - OBJECT_SIZE)
                new_object_rect.y = 0 - OBJECT_SIZE  # Start above the screen
                new_object = {'rect': new_object_rect, 'image': random.choice(object_type1_images)}
                falling_objects.append(new_object)
                last_object_time_type1 = time.time()
            if time.time() - last_object_time_type2 > 13 :
                new_object_rect = object_type2_images[0].get_rect()
                # Set the initial position randomly along the top edge
                new_object_rect.x = random.randint(0, WIDTH - OBJECT_SIZE)
                new_object_rect.y = 0 - OBJECT_SIZE  # Start above the screen
                new_object = {'rect': new_object_rect, 'image': random.choice(object_type2_images)}
                falling_objects.append(new_object)
                last_object_time_type2 = time.time()
            if time.time() - last_object_time_type3 > 16:
                new_object_rect = object_type3_images[0].get_rect()
                # Set the initial position randomly along the top edge
                new_object_rect.x = random.randint(0, WIDTH - OBJECT_SIZE)
                new_object_rect.y = 0 - OBJECT_SIZE  # Start above the screen
                new_object = {'rect': new_object_rect, 'image': random.choice(object_type3_images)}
                falling_objects.append(new_object)
                last_object_time_type3 = time.time()
            if time.time() - last_object_time_type4> 19:
                new_object_rect = object_type4_images[0].get_rect()
                # Set the initial position randomly along the top edge
                new_object_rect.x = random.randint(0, WIDTH - OBJECT_SIZE)
                new_object_rect.y = 0 - OBJECT_SIZE  # Start above the screen
                new_object = {'rect': new_object_rect, 'image': random.choice(object_type4_images)}
                falling_objects.append(new_object)
                last_object_time_type4 = time.time()
            if time.time() - last_object_time_type5 > 22:
                new_object_rect = object_type5_images[0].get_rect()
                # Set the initial position randomly along the top edge
                new_object_rect.x = random.randint(0, WIDTH - OBJECT_SIZE)
                new_object_rect.y = 0 - OBJECT_SIZE  # Start above the screen
                new_object = {'rect': new_object_rect, 'image': random.choice(object_type5_images)}
                falling_objects.append(new_object)
                last_object_time_type5 = time.time()
            if time.time() - last_object_time_type6> 25:
                new_object_rect = object_type6_images[0].get_rect()
                # Set the initial position randomly along the top edge
                new_object_rect.x = random.randint(0, WIDTH - OBJECT_SIZE)
                new_object_rect.y = 0 - OBJECT_SIZE  # Start above the screen
                new_object = {'rect': new_object_rect, 'image': random.choice(object_type6_images)}
                falling_objects.append(new_object)
                last_object_time_type6 = time.time()
            # Move objects (simulate falling)
            for obj in falling_objects:
                obj['rect'].centery += FALL_SPEED
            
            # Check if objects go off the screen, remove them
            falling_objects = [obj for obj in falling_objects if obj['rect'].y < HEIGHT]
            # Move the bucket with the mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bucket_rect.centerx = mouse_x
            # Check if objects are caught in the bucket
            for i in range(MAX_LIVES):
                if i < current_lives:
                    screen.blit(bright_life_image, (start_x + i * (life_image_size[0] + life_image_spacing), life_images_top))
                else:
                    screen.blit(dim_life_image, (start_x + i * (life_image_size[0] + life_image_spacing), life_images_top))
            for obj in falling_objects:
                if bucket_rect.colliderect(obj['rect']):
                    falling_objects.remove(obj)
                    if obj['image'] in object_type1_images and current_bucket_index == 0:
                        # Type 1 object caught
                        score += 1
                        # Display +1 animation in green
                        animations.append({'text': '+1', 'x': random.randint(WIDTH // 4, 3 * WIDTH // 4),
                                        'y': random.randint(HEIGHT // 4, 3 * HEIGHT // 4),
                                        'color': (0, 255, 0), 'start_time': pygame.time.get_ticks()})
                    elif obj['image'] in object_type2_images and current_bucket_index == 1:
                        # Type 1 object caught
                        score += 1
                        # Display +1 animation in green
                        animations.append({'text': '+1', 'x': random.randint(WIDTH // 4, 3 * WIDTH // 4),
                                        'y': random.randint(HEIGHT // 4, 3 * HEIGHT // 4),
                                        'color': (0, 255, 0), 'start_time': pygame.time.get_ticks()})
                    elif obj['image'] in object_type3_images and current_bucket_index == 2:
                        # Type 1 object caught
                        score += 1
                        # Display +1 animation in green
                        animations.append({'text': '+1', 'x': random.randint(WIDTH // 4, 3 * WIDTH // 4),
                                        'y': random.randint(HEIGHT // 4, 3 * HEIGHT // 4),
                                        'color': (0, 255, 0), 'start_time': pygame.time.get_ticks()})
                    elif obj['image'] in object_type4_images and current_bucket_index == 3:
                        # Type 1 object caught
                        score += 1
                        # Display +1 animation in green
                        animations.append({'text': '+1', 'x': random.randint(WIDTH // 4, 3 * WIDTH // 4),
                                        'y': random.randint(HEIGHT // 4, 3 * HEIGHT // 4),
                                        'color': (0, 255, 0), 'start_time': pygame.time.get_ticks()})
                    elif obj['image'] in object_type5_images and current_bucket_index == 4:
                        # Type 1 object caught
                        score += 1
                        # Display +1 animation in green
                        animations.append({'text': '+1', 'x': random.randint(WIDTH // 4, 3 * WIDTH // 4),
                                        'y': random.randint(HEIGHT // 4, 3 * HEIGHT // 4),
                                        'color': (0, 255, 0), 'start_time': pygame.time.get_ticks()})
                    elif obj['image'] in object_type6_images and current_bucket_index == 5:
                        # Type 1 object caught
                        score += 1
                        # Display +1 animation in green
                        animations.append({'text': '+1', 'x': random.randint(WIDTH // 4, 3 * WIDTH // 4),
                                        'y': random.randint(HEIGHT // 4, 3 * HEIGHT // 4),
                                        'color': (0, 255, 0), 'start_time': pygame.time.get_ticks()})
                    else:
                        current_lives-=1
                    
                        # Display -1 animation in red
            # Remove faded animations
            animations = [animation for animation in animations if pygame.time.get_ticks() - animation['start_time'] < ANIMATION_DURATION]
            # Draw falling objects
            for obj in falling_objects:
                screen.blit(obj['image'], obj['rect'].topleft)

            # Draw the bucket
            screen.blit(bucket_image, bucket_rect.topleft)
            # Draw the score
            score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
            # Draw the timer
            timer_text = score_font.render(f"Time: {remaining_time}", True, (255, 255, 255))
            screen.blit(timer_text, (WIDTH - 150, 10))
            # Draw animations
            for animation in animations:
                elapsed_time = pygame.time.get_ticks() - animation['start_time']
                alpha = max(0, 255 - elapsed_time / 5)  # Decrease alpha for fading effect
                display_animation(animation['text'], animation['x'], animation['y'], animation['color'], alpha)
            # Remove faded animations
            animations = [animation for animation in animations if pygame.time.get_ticks() - animation['start_time'] < 750]
    pygame.display.flip()
    clock.tick(FPS)
