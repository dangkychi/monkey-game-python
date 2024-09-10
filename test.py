import pygame

# Initialize the Pygame library
pygame.init()

# Set the window size
screen = pygame.display.set_mode((400, 300))

# Create a rectangle object
rect = pygame.Rect(100, 100, 50, 50)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            rect.centerx = event.pos[0]
            rect.centery = event.pos[1]
    
    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the rectangle
    pygame.draw.rect(screen, (255, 0, 0), rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()