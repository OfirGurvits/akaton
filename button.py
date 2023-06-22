import pygame


def default_func():
    print('click click click')


class Button:
    button_height = 100
    button_width = 200

    def __init__(self, x, y, screen, button_color, button_hover_color, font, text_color=(255, 255, 255),
                 text="Click Me!", func=default_func):
        self.font = font
        self.text_color = text_color
        self.button_x = x
        self.button_y = y
        self.button_current_color = button_color
        self.button_color = button_color
        self.screen = screen
        self.button_hover_color = button_hover_color
        self.text = text
        self.func = func

    def is_inside(self, pos):
        return self.button_x <= pos[0] <= self.button_x + self.button_width and self.button_y <= pos[1] \
            <= self.button_y + self.button_height

    def calc_color(self, pos):
        if self.is_inside(pos):
            self.button_current_color = self.button_hover_color
        else:
            self.button_current_color = self.button_color

    def draw(self):
        pygame.draw.rect(self.screen, self.button_current_color,
                         (self.button_x, self.button_y, self.button_width, self.button_height))
        # Render the button text
        button_text = self.font.render(self.text, True, self.text_color)
        button_text_rect = button_text.get_rect(
            center=(self.button_x + self.button_width // 2, self.button_y + self.button_height // 2))

        # Draw the button text onto the screen
        self.screen.blit(button_text, button_text_rect)

    def execute(self):
        self.func()
        return self.text
