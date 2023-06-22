import pygame

button_height = 100
button_width = 200
button_color = (255, 0, 0)  # Red
button_hover_color = (0, 255, 0)  # Green

class Display():

    # Initialize Pygame
    def __init__(self):
        pygame.init()

        # Set the screen dimensions
        screen_width = 800
        screen_height = 600

        # Create the screen
        self.screen = pygame.display.set_mode((screen_width, screen_height))

        # Set the button dimensions and position
        self.button_width = button_width
        self.button_height = button_height
        self.button_x = (screen_width - button_width) // 2
        self.button_y = (screen_height - button_height) // 2

        # Set the button colors


        # Set the button text properties
        self.font = pygame.font.Font(None, 36)
        self.text_color = (255, 255, 255)  # White

        # Set the initial button color
        self.button_current_color = button_color

        # Function to check if a position is inside the button

    def is_inside_button(self, pos):
        return self.button_x <= pos[0] <= self.button_x + button_width and self.button_y <= pos[1] \
            <= self.button_y + button_height

    def run(self):
        # Main loop
        global button_current_color
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    # Change button color when the mouse hovers over it
                    if self.is_inside_button(event.pos):
                        button_current_color = button_hover_color
                    else:
                        button_current_color = button_color
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the button is clicked
                    if self.is_inside_button(event.pos):
                        print("Button Clicked!")

            # Clear the screen
            self.screen.fill((0, 0, 0))  # Black

            # Draw the button
            pygame.draw.rect(self.screen, button_current_color, (self.button_x, self.button_y, button_width, button_height))

            # Render the button text
            button_text = self.font.render("Click Me!", True, self.text_color)
            button_text_rect = button_text.get_rect(
                center=(self.button_x + button_width // 2, self.button_y + button_height // 2))

            # Draw the button text onto the screen
            self.screen.blit(button_text, button_text_rect)

            # Update the display
            pygame.display.flip()
