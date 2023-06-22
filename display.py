import pygame
from button import Button

button_height = 100
button_width = 200
button_color = (255, 0, 0)  # Red
button_hover_color = (0, 255, 0)  # Green


def on_click_yes():
    print('click click click yes')


def on_click_no():
    print('click click click no')


def on_click_maybe():
    print('click click click maybe')


def on_click_dont_know():
    print('click click click don\'t know')


class Display:

    # Initialize Pygame
    def __init__(self):
        pygame.init()

        # Set the screen dimensions
        screen_width = 800
        screen_height = 600

        # Create the screen
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font = pygame.font.Font(None, 36)

        # self.button = Button((screen_width - button_width) // 2, (screen_height - button_height) // 2, self.screen,
        #                     button_color, button_hover_color, self.font)
        # Set the button colors

        # Set the button text properties
        self.text_color = (255, 255, 255)  # White

        # Set the initial button color
        self.button_current_color = button_color

        rows = 2
        colums = 2
        flag = 1
        flag2 = 1
        dis = 50
        dis2 = 40

        button_x = (screen_width - button_width) // (rows + 1)
        button_y = (screen_height - button_height) // (colums + 1)
        strings = ['Yes', 'No', 'Maybe', 'don\'t know']
        funcs = [on_click_yes, on_click_no, on_click_maybe, on_click_dont_know]
        counter = 0
        self.buttons = []
        for i in range(colums):
            button_line = []
            for j in range(rows + 1):
                if j % 2 != 0:
                    continue
                button_line.append(Button((1 + j) * button_y + dis * flag, (1 + i) * button_x + dis2*flag2,
                                          self.screen, button_color,
                                          button_hover_color, self.font, text=strings[counter], func=funcs[counter]))
                counter += 1
                flag *= -1
            self.buttons.extend(button_line)
            flag2 *= -1
    def run(self):
        start_time = -4000
        last_choice = ''
        # Main loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEMOTION:
                    # Change button color when the mouse hovers over it
                    for button in self.buttons:
                        button.calc_color(event.pos)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button.is_inside(event.pos):
                            start_time = pygame.time.get_ticks()
                            last_choice = button.execute()
                    # Check if the button is clicked

            # Clear the screen
            self.screen.fill((255, 255, 255))  # white
            elapsed_time = pygame.time.get_ticks() - start_time
            if elapsed_time <= 2000:
                text_surface = self.font.render(last_choice, True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(400, 100))

                # Draw the text onto the screen
                self.screen.blit(text_surface, text_rect)
            # Draw the button
            for button in self.buttons:
                button.draw()
            # self.button.draw()

            # Update the display
            pygame.display.flip()
