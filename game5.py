# import pygame
# import sys
# import os

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 800, 600
# WHITE = (255, 255, 255)
# FONT = pygame.font.Font(None, 36)

# # Create the screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption('Recyclable and Non-Recyclable Items')

# # Function to display text
# def display_text(text, position):
#     text_surface = FONT.render(text, True, (0, 0, 0))
#     screen.blit(text_surface, position)



# # Function to display images and text
# def display_item(image, text, position):
#     screen.blit(image, position)
#     display_text(text, (position[0] + 70, position[1]))  # Adjust text position based on image position

# # Main loop
# def instruction_page():
#     running = True
#     while running:
#         screen.fill(WHITE)
        
#         display_text('Recyclable Items:', (50, 50))
#         display_item(cardboard_img, '- Cardboard', (50, 100))
#         display_item(paper_img, '- Paper', (50, 150))
#         display_item(cans_img, '- Cans', (50, 200))
#         display_item(iron_img, '- Iron', (50, 250))
#         display_item(cloth_img, '- Cloth', (50, 300))
#         display_item(water_bottle_img, '- Water Bottle', (50, 350))
#         display_item(glass_img, '- Glass', (50, 400))
        
#         display_text('Non-Recyclable Items:', (400, 50))
#         display_item(mobile_img, '- Mobile', (400, 100))
#         display_item(cd_img, '- CD', (400, 150))
#         display_item(diapers_img, '- Diapers', (400, 200))
#         display_item(bulbs_img, '- Bulbs', (400, 250))
#         display_item(foam_boxes_img, '- Foam Boxes', (400, 300))
#         display_item(paint_cans_img, '- Paint Cans', (400, 350))
#         display_item(laptop_img, '- Laptop', (400, 400))
        
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#                 pygame.quit()
#                 sys.exit()
        
#         pygame.display.flip()

# instruction_page()
import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Recyclable and Non-Recyclable Items')

# Function to display text
def display_text(text, position):
    text_surface = FONT.render(text, True, (0, 0, 0))
    screen.blit(text_surface, position)

# Load images for recyclable items
# # Load images for recyclable items
cardboard_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img\\cardboard.png')
paper_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img\\paper.png')
cans_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img\\tin.png')
iron_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img\\iron.png')
cloth_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img\\cloth.png')
water_bottle_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img\\water bottle.png')
glass_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img\\glass.png')

# Load images for non-recyclable items
mobile_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img1\\mobile.png')
cd_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img1\\cd.png')
diapers_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img1\\diaper.png')
bulbs_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img1\\bulb.png')
foam_boxes_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img1\\foam box.png')
paint_cans_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img1\\paint.png')
laptop_img = pygame.image.load('C:\\Users\\Srimanth\\Downloads\\img1\\laptop.png')

# Function to display images and text
def display_item(image, text, position):
    screen.blit(image, position)
    display_text(text, (position[0] + 70, position[1]))  # Adjust text position based on image position

# Main loop
def instruction_page():
    running = True
    while running:
        screen.fill(WHITE)
        
        display_text('Recyclable Items:', (50, 50))
        display_item(cardboard_img, '- Cardboard', (50, 100))
        display_item(paper_img, '- Paper', (50, 150))
        display_item(cans_img, '- Cans', (50, 200))
        display_item(iron_img, '- Iron', (50, 250))
        display_item(cloth_img, '- Cloth', (50, 300))
        display_item(water_bottle_img, '- Water Bottle', (50, 350))
        display_item(glass_img, '- Glass', (50, 400))
        
        display_text('Non-Recyclable Items:', (400, 50))
        display_item(mobile_img, '- Mobile', (400, 100))
        display_item(cd_img, '- CD', (400, 150))
        display_item(diapers_img, '- Diapers', (400, 200))
        display_item(bulbs_img, '- Bulbs', (400, 250))
        display_item(foam_boxes_img, '- Foam Boxes', (400, 300))
        display_item(paint_cans_img, '- Paint Cans', (400, 350))
        display_item(laptop_img, '- Laptop', (400, 400))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
        
        pygame.display.flip()

instruction_page()