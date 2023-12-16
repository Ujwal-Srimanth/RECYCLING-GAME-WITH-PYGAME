import pygame
import sys
import time
import subprocess
from pymongo import MongoClient
import pymongo
# Initialize Pygame
pygame.init()
VALUE,VALUE1 = 0,0
# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FONT_SIZE = 36
small_image = pygame.image.load('small_coin (1).png')  # Replace with your small image file
small_image = pygame.transform.scale(small_image, (40, 40))  # Adjust the size as needed
small_image_rect = small_image.get_rect(topright=(WIDTH - 10, 0))
client = MongoClient('mongodb://localhost:27017')  # Update with your MongoDB connection string
db = client['your_database_name']  # Update with your database name
collection = db['your_collection_name']  # Update with your collection name
new_collection = db['score'] 
def handle_powerup1_click():
    print("hi i am in powerup1")
    if get_last_inserted_value1()-150 > 0:
        mm = get_last_inserted_value1()-150
        display_small_image(mm)
        document_to_insert = {
            'health':1
        }
        health = db['heatlh'] 
        health.insert_one(document_to_insert)
def handle_powerup2_click():
    print("hi i am in powerup2_images")
    if get_last_inserted_value1()-150 > 0:
        pp = get_last_inserted_value1()-150
        display_small_image(pp)
        document_to_insert = {
            'speed':1
        }
        time = db['time'] 
        time.insert_one(document_to_insert)
powerup1_image = pygame.image.load('life (1).png')  # Replace with your image file
powerup1_image = pygame.transform.scale(powerup1_image, (150, 100))
powerup2_image = pygame.image.load('life2 (1).png')  # Replace with your image file
powerup2_image = pygame.transform.scale(powerup2_image, (150, 100))
powerup1_rect = powerup1_image.get_rect(topleft=(20, HEIGHT // 4 - 80))
powerup2_rect = powerup2_image.get_rect(topright=(400, HEIGHT // 4 - 80))

button1_image = pygame.image.load('coin.png')
button1_image = pygame.transform.scale(button1_image, (140, 40))
button2_image = pygame.image.load('coin.png')
button2_image = pygame.transform.scale(button2_image, (140, 40))

button1_rect = pygame.Rect(powerup2_rect.left - 220 , powerup2_rect.bottom + 10, 100, 30)
button2_rect = pygame.Rect(powerup2_rect.left , powerup2_rect.bottom + 10, 100, 30)

def show_powerups_dialog():
    global show_powerups_flag
    dialog_shown = True
    
    powerups_dialog_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
    powerups_dialog_surface = pygame.Surface((WIDTH // 2, HEIGHT // 2))
    background_image = pygame.image.load('C://Users//Srimanth//Downloads//xx (2).jpg')  # Replace with your image file
    background_image = pygame.transform.scale(background_image, (WIDTH // 2, HEIGHT // 2))
    powerups_dialog_surface.blit(background_image, (0, 0))
    pygame.draw.rect(powerups_dialog_surface, BLACK, powerups_dialog_surface.get_rect(), 5)
    # Powerup images False

    # Display powerup images and prices
    
    powerups_dialog_surface.blit(powerup1_image, powerup1_rect)
    powerups_dialog_surface.blit(powerup2_image, powerup2_rect)
    
    powerups_dialog_surface.blit(button1_image, button1_rect.topleft)
    powerups_dialog_surface.blit(button2_image, button2_rect.topleft)
    # Display the powerups dialog box
    screen.blit(powerups_dialog_surface, powerups_dialog_rect)
  
    pygame.display.flip()
# Function to display the small image and value
def display_small_image(value):
    global VALUE
    global VALUE1
    screen.blit(small_image, small_image_rect)
    draw_text(str(value), WHITE, (WIDTH - 70, 25), 24)
    document_to_insert = {
    'final_score': value,
    # Add more key-value pairs as needed
    }
    VALUE = value
    VALUE1 = value
# Insert the document into the collection
    new_collection.insert_one(document_to_insert)

client = MongoClient('mongodb://localhost:27017')  # Update with your MongoDB connection string
db = client['your_database_name']  # Update with your database name
collection = db['your_collection_name']  # Update with your collection name

# Function to get the sum of final scores from MongoDB
def get_total_score():
    result = collection.aggregate([
        {
            '$group': {
                '_id': None,
                'total': {'$sum': '$final_score'}
            }
        }
    ])

    total_score = 0
    for doc in result:
        total_score = doc['total']

    return total_score

def get_last_inserted_value():
    # Sort by _id in descending order and retrieve the first document
    result = collection.find_one(sort=[('_id', pymongo.DESCENDING)])
    if result:
        return result.get('final_score')
    else:
        return None

new_collection = db['score'] 
def get_last_inserted_value1():
    # Sort by _id in descending order and retrieve the first document
    result = new_collection.find_one(sort=[('_id', pymongo.DESCENDING)])
    if result:
        return result.get('final_score')
    else:
        return None
print(get_last_inserted_value1())

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Recycle Game")
clock = pygame.time.Clock()

# Text properties
font = pygame.font.Font(None, FONT_SIZE)

# Buttons
try:
    start_button_image = pygame.image.load('newgame.png')  # Replace with your image file
    quit_button_image = pygame.image.load('exit.png')  # Replace with your image file
except pygame.error as e:
    print("Error loading button images:", e)
    sys.exit()

try:
    easy_button_image = pygame.image.load('easy111.png')  # Replace with your image file
    hard_button_image = pygame.image.load('hard111.png')  # Replace with your image file
except pygame.error as e:
    print("Error loading button images:", e)
    sys.exit()
try:
    welcome_button_image = pygame.image.load('ppp.png')  # Replace with your image file
except pygame.error as e:
    print("Error loading button images:", e)
    sys.exit()
button_width, button_height = 220, 60
start_button_image = pygame.transform.scale(start_button_image, (220, 70))
quit_button_image = pygame.transform.scale(quit_button_image, (button_width, button_height))

welcome_button_image = pygame.transform.scale(welcome_button_image, (220, 60))
welcome = welcome_button_image.get_rect(topleft=(WIDTH // 2 - 100, HEIGHT // 2 - 50))

# Use Rect objects to handle button collisions
start_button_rect = start_button_image.get_rect(topleft=(WIDTH // 2 - 117, HEIGHT // 2))
quit_button_rect = quit_button_image.get_rect(topleft=(WIDTH // 2 - 111, HEIGHT // 2 + 100))
# Set the size of the button images
button_width, button_height = 220, 6 
easy_button_image = pygame.transform.scale(easy_button_image, (220, 70))
hard_button_image = pygame.transform.scale(hard_button_image, (220, 70))
# Use Rect objects to handle button collisions
easy_button_rect = easy_button_image.get_rect(topleft=(WIDTH // 2 - 100, HEIGHT // 2))
hard_button_rect = hard_button_image.get_rect(topleft=(WIDTH // 2 - 100, HEIGHT // 2 + 100))
# Loading bar variables
loading_bar_rect = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 200, WIDTH // 2, 20)
loading_progress = 0
loading_speed = 2
# Timer to simulate loading
start_time = time.time()
loading_time = 5  # seconds
def draw_text(text, color, position, size):
    font = pygame.font.Font(None, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=position)
    screen.blit(surface, rect)
loading_complete = False
# Game state variable
show_levels_flag = False
# Load background image for the welcome page
welcome_background = pygame.image.load('C://Users//Srimanth//Downloads//oo5.jpg')  # Replace with your image file
welcome_background = pygame.transform.scale(welcome_background, (WIDTH, HEIGHT))
# Original background for the level page
level_background = pygame.image.load('mm.png')  # Replace with your image file
level_background = pygame.transform.scale(level_background, (WIDTH, HEIGHT))\
# Function to handle the game logic after "Start" button is clicked
def show_levels():
    global show_levels_flag
    show_levels_flag = True
# Function to handle the game logic after "Easy" button is clicked
def start_easy_level():
    subprocess.run(['python', 'game99.py'])
def start_hard_level():
    subprocess.run(['python', 'game100.py'])
show_powerups_flag = False
flag = db['flag_col']
document_to_insert = {
    'flag': 0,
    # Add more key-value pairs as needed
}
# Insert the document into the collection
flag.insert_one(document_to_insert)
def get_last_inserted_value2():
    # Sort by _id in descending order and retrieve the first document
    result = flag.find_one(sort=[('_id', pymongo.DESCENDING)],skip=1)
    if result:
        return result.get('flag')
    else:
        return None
if get_last_inserted_value2():
    VALUE = get_last_inserted_value1()+get_last_inserted_value()
else:
    VALUE1 = get_last_inserted_value1()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            wait_for_response = True
            while wait_for_response:
                show_powerups_flag = True
                show_powerups_dialog()
                for inner_event in pygame.event.get():
                    if inner_event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        if button1_rect.collidepoint(x, y):
                            # Call a function when powerup_rect1 is clicked
                            handle_powerup1_click()
                        if button2_rect.collidepoint(x, y):
                            # Call a function when powerup_rect2 is clicked
                            handle_powerup2_click()
                    if inner_event.type == pygame.KEYDOWN and inner_event.key == pygame.K_q:
                        wait_for_response = False
                        show_levels_flag = False
                        show_powerups_flag = False
                        break
                    if inner_event.type == pygame.KEYDOWN and inner_event.key == pygame.K_b:
                        handle_powerup1_click()
                    if inner_event.type == pygame.KEYDOWN and inner_event.key == pygame.K_n:
                        handle_powerup2_click()
       
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if easy_button_rect.collidepoint(x, y) and show_levels_flag:
                document_to_insert = {
                    'flag': 1,
    # Add more key-value pairs as needed
                }
                flag.insert_one(document_to_insert)
                start_easy_level()
            elif hard_button_rect.collidepoint(x, y) and show_levels_flag:
                document_to_insert = {
                    'flag': 1,
    # Add more key-value pairs as needed
                }
                flag.insert_one(document_to_insert)
                start_hard_level()
            elif start_button_rect.collidepoint(x, y):
                show_levels()  # Call the function to show levels when "Start" is clicked
            elif quit_button_rect.collidepoint(x, y):
                pygame.quit()
                sys.exit()
        
            
    # Update loading progress
    elapsed_time = time.time() - start_time
    loading_progress = min(1.0, elapsed_time / loading_time)
    # Draw the background based on the game state
    if show_levels_flag:
        screen.blit(level_background, (0, 0))
    else:
        screen.blit(welcome_background, (0, 0))
    # Draw the raining animation
    if not show_levels_flag:
        for _ in range(20):
            pygame.draw.line(screen, WHITE, (pygame.time.get_ticks() % WIDTH, pygame.time.get_ticks() % HEIGHT),
                             (pygame.time.get_ticks() % WIDTH, pygame.time.get_ticks() % HEIGHT + 5), 2)
    # Draw the loading bar (only on the welcome page)
    if not show_levels_flag and not loading_complete:
        pygame.draw.rect(screen, (255, 87, 51), loading_bar_rect)
        draw_text(f"Loading... {int(loading_progress * 100)}%", WHITE, (WIDTH // 2, HEIGHT // 2 + 50),24)
        loading_bar_rect.width = loading_progress * (WIDTH // 2)
    # Display text based on loading progress
    if not show_levels_flag and loading_progress < 1.0:
        screen.blit(welcome_button_image, welcome)
        if get_last_inserted_value2() == 1:
            display_small_image(VALUE)
            document_to_insert = {
                    'final_score': VALUE,
                 # Add more key-value pairs as needed
            }
            new_collection.insert_one(document_to_insert)

        else:
            display_small_image(VALUE1)
            document_to_insert = {
                    'final_score': VALUE1,
                 # Add more key-value pairs as needed
            }
            new_collection.insert_one(document_to_insert)

    if not show_levels_flag and loading_complete:  # Draw only if not in the level page
        title_image = pygame.image.load("AI.png")
        screen.blit(title_image, (WIDTH // 2 - title_image.get_width() // 2, HEIGHT // 2 - 80 - title_image.get_height() // 2))
        screen.blit(start_button_image, start_button_rect)
        screen.blit(quit_button_image, quit_button_rect)
        if get_last_inserted_value2()==1:
            display_small_image(VALUE)
            document_to_insert = {
                    'final_score': VALUE,
                 # Add more key-value pairs as needed
            }
            new_collection.insert_one(document_to_insert)
        else:
            display_small_image(VALUE1)
            document_to_insert = {
                    'final_score': VALUE1,
                 # Add more key-value pairs as needed
            }
            new_collection.insert_one(document_to_insert)
        # Display buttons after loading is complete
    if not show_levels_flag and loading_progress >= 1.0:
        loading_complete = True
    if show_levels_flag:
        # Draw "Select Level" text in the center
        draw_text("Select Level", BLACK, (WIDTH // 2, HEIGHT // 2 - 50),35)
        screen.blit(easy_button_image, easy_button_rect)
        screen.blit(hard_button_image, hard_button_rect)
    if show_powerups_flag:
        show_powerups_dialog()
    pygame.display.flip()
    clock.tick(FPS)