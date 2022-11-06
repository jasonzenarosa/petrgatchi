import pygame
import random
from Petrgotchi import Petrgotchi


_FRAME_RATE = 30
_INITIAL_WIDTH = 700
_INITIAL_HEIGHT = 700
_BACKGROUND_COLOR = pygame.Color(175, 95, 0)


class PetrTamagotchi:
    def __init__(self):
        self._running = True
        self._topleft_x = _INITIAL_WIDTH // 3
        self._topleft_y = _INITIAL_HEIGHT // 3
        self._xv = 1
        self._yv = 1

        self._petrgotchi = Petrgotchi()
        

    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()
            second_counter = 0

            self._petr = pygame.image.load('image_petr.png')
            self._feed = pygame.image.load('image_food.svg')
            self._clean = pygame.image.load('image_shower.svg')
            self._play = pygame.image.load('image_play.svg')

            self._create_display((_INITIAL_WIDTH, _INITIAL_HEIGHT))

            while self._running:
                second_counter += 1
                clock.tick(_FRAME_RATE)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self._running = False
<<<<<<< HEAD
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        
                        if 213 <= mouse[0] <= 256 and 633 <= mouse[1] <= 673:
                            self._petrgotchi.increase_hunger()
                        elif 326 <= mouse[0] <= 377 and 633 <= mouse[1] <= 673:
                            self._petrgotchi.increase_entertainment()
                        elif 447 <= mouse[0] <= 490 and 633 <= mouse[1] <= 673:
                            self._petrgotchi.increase_cleanliness()
                
                self._petrgotchi.decrease_cleanliness()
                self._petrgotchi.decrease_entertainment()
                self._petrgotchi.decrease_hunger()
                
                if second_counter == 30:
                    self._update_velocity()
                    second_counter = 0
                
                if self._petrgotchi.mood() == "dead":
                    self._petr = pygame.image.load('petr_dead.png')
                elif self._petrgotchi.mood() == "sad":
                    self._petr = pygame.image.load('petr_sad.png')
                elif self._petrgotchi.mood() == "stinky":
                    self._petr = pygame.image.load('petr_stinky.png')
                else:
                    self._petr = pygame.image.load('image_petr.png')
                
=======

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
                            pass

>>>>>>> 73c5008b88aee3338510d42adf0a65dfa6a0eb8f
                self._redraw()
        finally:
            pygame.quit()
    

    def _create_display(self, dimensions) -> None:
        pygame.display.set_mode(dimensions, pygame.RESIZABLE)
    

    def _redraw(self) -> None:
        surface = pygame.display.get_surface()
        surface.fill(_BACKGROUND_COLOR)
        self._draw_petr()
        self._draw_buttons()
        self._display_hunger()
        self._display_entertainment()
        self._display_cleanliness()

        pygame.display.flip()
    

    def _draw_petr(self) -> None:
        surface = pygame.display.get_surface()

        petr_width = _round(surface.get_width() / 3)
        petr_height = _round(surface.get_height() / 3)

        if 0 <= self._topleft_x + self._xv <= surface.get_width() - petr_width:
            self._topleft_x += self._xv
        else:
            self._xv = -self._xv
            self._topleft_x += self._xv
        
        if surface.get_height() / 5.1 <= self._topleft_y + self._yv <= surface.get_height() / 1.125 - petr_height:
            self._topleft_y += self._yv
        else:
            self._yv = -self._yv
            self._topleft_y += self._yv

        petr_rect = pygame.Rect(self._topleft_x, self._topleft_y, petr_width, petr_height)
        scaled_petr = pygame.transform.scale(self._petr, (petr_width, petr_height))

        surface.blit(scaled_petr, petr_rect)
    

    def _update_velocity(self) -> None:
        change = 2 * (random.random() - 0.5)

        if -2 <= self._xv + change <= 2:
            self._xv += change
        
        change = 2 * (random.random() - 0.5)

        if -2 <= self._yv + change <= 2:
            self._yv += change
    

    def _draw_buttons(self) -> None:
        surface = pygame.display.get_surface()

        feed_width = _round(surface.get_width() / 12)
        feed_height = _round(surface.get_height() / 12)
        feed_topleft_x = _round(surface.get_width() / 3) - feed_width // 2
        feed_topleft_y = _round(surface.get_width() / 1.125)
        feed_rect = pygame.Rect(feed_topleft_x, feed_topleft_y, feed_width, feed_height)
        scaled_feed = pygame.transform.scale(self._feed, (feed_width, feed_height))
        surface.blit(scaled_feed, feed_rect)

        play_width = _round(surface.get_width() / 12)
        play_height = _round(surface.get_height() / 12)
        play_topleft_x = _round(surface.get_width() / 2) - play_width // 2
        play_topleft_y = _round(surface.get_width() / 1.125)
        play_rect = pygame.Rect(play_topleft_x, play_topleft_y, play_width, play_height)
        scaled_play = pygame.transform.scale(self._play, (play_width, play_height))
        surface.blit(scaled_play, play_rect)

        clean_width = _round(surface.get_width() / 12)
        clean_height = _round(surface.get_height() / 12)
        clean_topleft_x = _round(surface.get_width() / (3/2)) - clean_width // 2
        clean_topleft_y = _round(surface.get_width() / 1.125)
        clean_rect = pygame.Rect(clean_topleft_x, clean_topleft_y, clean_width, clean_height)
        scaled_clean = pygame.transform.scale(self._clean, (clean_width, clean_height))
        surface.blit(scaled_clean, clean_rect)
    

    def _display_hunger(self) -> None:
        surface = pygame.display.get_surface()
        font = pygame.font.SysFont('georgia', _round(surface.get_width() * 0.032))
        text = 'Hunger'
        
        text_image = font.render(text, True, pygame.Color(0, 0, 0))

        text_topleft_x = _round(surface.get_width() * 0.135)
        text_topleft_y = _round(surface.get_height() * 0.04)
        
        surface.blit(text_image, (text_topleft_x, text_topleft_y))

        bar_width = _round(surface.get_width() * 0.5) - (0.5 * surface.get_width() * self._petrgotchi.hunger())
        bar_height = _round(surface.get_height() * 0.04)
        bar_topleft_x = _round(surface.get_width() * 0.27)
        bar_topleft_y = _round(surface.get_width() * 0.04)
        bar = pygame.Rect(bar_topleft_x, bar_topleft_y, bar_width, bar_height)
        pygame.draw.rect(surface, pygame.Color(0, 0, 0), bar)

    
    def _display_entertainment(self) -> None:
        surface = pygame.display.get_surface()
        font = pygame.font.SysFont('georgia', _round(surface.get_width() * 0.032))
        text = 'Entertainment'
        
        text_image = font.render(text, True, pygame.Color(0, 0, 0))

        text_topleft_x = _round(surface.get_width() * 0.04)
        text_topleft_y = _round(surface.get_height() * 0.09)
        
        surface.blit(text_image, (text_topleft_x, text_topleft_y))

        bar_width = _round(surface.get_width() * 0.5) - (0.5 * surface.get_width() * self._petrgotchi.entertainment())
        bar_height = _round(surface.get_height() * 0.04)
        bar_topleft_x = _round(surface.get_width() * 0.27)
        bar_topleft_y = _round(surface.get_width() * 0.09)
        bar = pygame.Rect(bar_topleft_x, bar_topleft_y, bar_width, bar_height)
        pygame.draw.rect(surface, pygame.Color(0, 0, 0), bar)

    
    def _display_cleanliness(self) -> None:
        surface = pygame.display.get_surface()
        font = pygame.font.SysFont('georgia', _round(surface.get_width() * 0.032))
        text = 'Cleanliness'
        
        text_image = font.render(text, True, pygame.Color(0, 0, 0))

        text_topleft_x = _round(surface.get_width() * 0.085)
        text_topleft_y = _round(surface.get_height() * 0.14)
        
        surface.blit(text_image, (text_topleft_x, text_topleft_y))

        bar_width = _round(surface.get_width() * 0.5) - (0.5 * surface.get_width() * self._petrgotchi.cleanliness())
        bar_height = _round(surface.get_height() * 0.04)
        bar_topleft_x = _round(surface.get_width() * 0.27)
        bar_topleft_y = _round(surface.get_width() * 0.14)
        bar = pygame.Rect(bar_topleft_x, bar_topleft_y, bar_width, bar_height)
        pygame.draw.rect(surface, pygame.Color(0, 0, 0), bar)


def _round(number: float) -> int:
    return int(number + 0.5)


if __name__ == '__main__':
    PetrTamagotchi().run()