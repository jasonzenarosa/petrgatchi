import pygame
import random


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
        

    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()
            second_counter = 0

            self._petr = pygame.image.load('petr.png')
            self._feed = pygame.image.load('feed.svg')

            self._create_display((_INITIAL_WIDTH, _INITIAL_HEIGHT))

            while self._running:
                second_counter += 1
                clock.tick(_FRAME_RATE)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self._running = False
                
                if second_counter == 30:
                    self._update_velocity()
                    second_counter = 0
                
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
        
        if 0 <= self._topleft_y + self._yv <= surface.get_height() - petr_height:
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
        feed_topleft_x = _round(surface.get_width() / 3)
        feed_topleft_y = _round(surface.get_width() / 1.1)
        feed_rect = pygame.Rect(feed_topleft_x, feed_topleft_y, feed_width, feed_height)
        scaled_feed = pygame.transform.scale(self._feed, (feed_width, feed_height))
        surface.blit(scaled_feed, feed_rect)


def _round(number: float) -> int:
    return int(number + 0.5)


if __name__ == '__main__':
    PetrTamagotchi().run()