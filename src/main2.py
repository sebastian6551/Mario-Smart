import pygame
import sys
import numpy as np
from game import *


class Main:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Mario Smart")  # Window tittle
        self.game = Game()

    def mainloop(self, fileName, height):

        screen = self.screen
        game = self.game

        board = Main.importBoard(fileName)

        while True:
            game.showBoard(screen, board)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.update()
            screen.fill((255, 255, 255))

    # Function that imports the board from a txt file.
    @staticmethod
    def importBoard(fileName):

        with open(fileName, 'r') as f:
            content = f.read().split('\n')

        lines = []
        for i in range(len(content)):
            lines.append(list(map(lambda x: int(x), content[i].split(" "))))

        board = np.array(lines)
        return board


main = Main()
main.mainloop('matriz2.txt', rows)
