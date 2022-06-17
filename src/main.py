import pygame
import sys
from level import Level

import settings

class Game:
    """Main Game Class"""
    def __init__(self) -> None:
        # General Setup
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))

        pygame.display.set_caption(settings.GAME_TITLE)
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        """PyGame Game Loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                              
            self.screen.fill(settings.BG_COLOUR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(settings.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
    