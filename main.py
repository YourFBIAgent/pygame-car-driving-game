import pygame
from sys import exit

class Game:
    def __init__(self, width, height, title) -> None:
        pygame.init()

        self.WIDTH = width
        self.HEIGHT = height
        self.SCREEN = pygame.display.set_mode((width, height))
        
        pygame.display.set_caption(title)

    def quit(self) -> None:
        pygame.quit()
        exit()
    
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            pygame.display.update()
            

if __name__ == '__main__':
    game = Game(600, 800, 'Point Collector')
    game.run()
