import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Background Image Example")

# Load the background image
background_image = pygame.image.load("back.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            # 'a' key is pressed, exit the loop
            pygame.quit()
            # Now, you can call another Python file or perform any other actions
            # For example, you can use subprocess to run another Python script
            import subprocess
            subprocess.run(["python", "game79.py"])

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Update the display
    pygame.display.flip()
