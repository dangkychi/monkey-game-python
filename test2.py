import pygame

# Initialize Pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((1300, 900))

# Load images
figure_1 = pygame.image.load("./images/figure1.png")
figure_2 = pygame.image.load("./images/figure1.png")

figure_1 = pygame.transform.scale(figure_1, (240, 240))
figure_2 = pygame.transform.scale(figure_2, (240, 240))
# Set background color
bg_color = (255, 255, 255)

# Define clock
clock = pygame.time.Clock()

# Initialize selected figure
selected_figure = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pos[0] < 400:
                selected_figure = figure_1
            else:
                selected_figure = figure_2
    
    # Clear screen
    screen.fill(bg_color)
    
    # Display figures
    screen.blit(figure_1, (100, 200))
    screen.blit(figure_2, (500, 200))
    
    # Highlight selected figure
    if selected_figure:
        pygame.draw.rect(screen, (0, 255, 0), (selected_figure == figure_1 and (80, 180) or (480, 180), (240, 240)), 5)
    
    # Update screen
    pygame.display.update()
    
    # Check if figure is selected
    if selected_figure:
        running = False
    
    # Limit FPS
    clock.tick(30)

# Quit Pygame
pygame.quit()
