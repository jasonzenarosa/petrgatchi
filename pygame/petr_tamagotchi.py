import pygame
import random


_FRAME_RATE = 30
_INITIAL_WIDTH = 700
_INITIAL_HEIGHT = 700
_BACKGROUND_COLOR = pygame.Color(255, 255, 255)


class PetrTamagotchi:
    def __init__(self):
        self._running = True
        self._xv = 1
        self._yv = 1
    

    def run(self) -> None:
        pygame.init()

        try:
            clock = pygame.time.Clock()

            self._petr = pygame.image.load('petr.png')

            self._create_display((_INITIAL_WIDTH, _INITIAL_HEIGHT))

            while self._running:
                clock.tick(_FRAME_RATE)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self._running = False
                
                if random.random() > 0.5:
                    self.x += self.
                else:
                    self.x -= 1
                
                self._redraw()
        finally:
            pygame.quit()
    

    def _create_display(self, dimensions) -> None:
        pygame.display.set_mode(dimensions, pygame.RESIZABLE)
    

    def _redraw(self) -> None:
        surface = pygame.display.get_surface()
        surface.fill(_BACKGROUND_COLOR)
        self._draw_petr()

        pygame.display.flip()
    

    def _draw_petr(self) -> None:
        surface = pygame.display.get_surface()

        petr_width = _round(surface.get_width() / 3)
        petr_height = _round(surface.get_height() / 3)
        topleft_x = _round(surface.get_width() / 3)
        topleft_y = _round(surface.get_height() / 3)

        petr_rect = pygame.Rect(topleft_x, topleft_y, petr_width, petr_height)
        scaled_petr = pygame.transform.scale(self._petr, (petr_width, petr_height))

        surface.blit(scaled_petr, petr_rect)


def _round(number: float) -> int:
    return int(number + 0.5)


if __name__ == '__main__':
    PetrTamagotchi().run()