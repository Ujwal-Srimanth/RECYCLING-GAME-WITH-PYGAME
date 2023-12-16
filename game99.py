import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Background Image Example")

# Load the background images
background_images = ["non.jpg", "rec.jpg"]  # Add more images if needed
current_image_index = 0
original_background_image = pygame.image.load(background_images[current_image_index])
current_background_image = pygame.transform.scale(original_background_image, (WIDTH, HEIGHT))

# Flags to track key presses
a_key_pressed = False
s_key_pressed = False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                # 'a' key is pressed, toggle the flag
                a_key_pressed = not a_key_pressed
                if a_key_pressed:
                    # Change the background image
                    current_image_index = (current_image_index + 1) % len(background_images)
                    original_background_image = pygame.image.load(background_images[current_image_index])
                    current_background_image = pygame.transform.scale(original_background_image, (WIDTH, HEIGHT))

                    # Draw the updated background image
                    screen.blit(current_background_image, (0, 0))
                    pygame.display.flip()

                    # Wait for a short duration (e.g., 2 seconds)
                    time.sleep(2)
            elif event.key == pygame.K_s:
                # 's' key is pressed, exit the loop
                s_key_pressed = True

    # Draw the current background image
    screen.blit(current_background_image, (0, 0))

    # Update the display
    pygame.display.flip()

    # If 's' key is pressed, exit the loop
    if s_key_pressed:
        break

# Quit Pygame
pygame.quit()

# Now, you can call another Python file or perform any other actions
# For example, you can use subprocess to run another Python script
import subprocess
subprocess.run(["python", "game3.py"])
