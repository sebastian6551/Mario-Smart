import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)  # FREE 0
BROWN = (139, 69, 19)  # BLOCK 1
# Set the length and width of each grid cell.
LENGTHCELL = 45
HIGHCELL = 45
# Set the margin between the cells.
MARGIN = 5


class Interface:

    def __init__(self, solutionWorlds):
        self.__solutionWorlds = solutionWorlds
        self.__imgMario = None
        self.__imgKoopa = None
        self.__imgPrincess = None
        self.__imgStar = None
        self.__imgFlower = None
        self.__imgMarioAndPrincess = None

    def loadImages(self):
        self.__imgMario = pygame.image.load("images/mario.jpg").convert()
        self.__imgKoopa = pygame.image.load("images/koopa.jpg").convert()
        self.__imgPrincess = pygame.image.load(
            "images/princess2.jpg").convert()
        self.__imgStar = pygame.image.load("images/star.jpg").convert()
        self.__imgFlower = pygame.image.load("images/flower.jpg").convert()
        self.__imgMarioAndPrincess = pygame.image.load(
            "images/mario&princess.jpg").convert()

    def showInterface(self):
        # Initialize pygame
        pygame.init()

        # Set the length and width of the screen
        WINDOW_DIMENSION = [510, 510]  # 255,255
        screen = pygame.display.set_mode(WINDOW_DIMENSION)

        # Set the title of the screen.
        pygame.display.set_caption("Mario smart profundidad")

        # iterate until the user presses the exit button.
        press = False

        # use it to set how fast the screen refreshes.
        clock = pygame.time.Clock()

        i = 1
        self.loadImages()
        grid = self.__solutionWorlds[0]

        # -------- Main Program Loop-----------
        while not press:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    press = True

            # Set the screen background.
            screen.fill(BLACK)

            # draw the grid
            for row in range(10):
                for column in range(10):
                    if (grid[row, column] != 1 and grid[row, column] != 2 and grid[row, column] != 5 and grid[row, column] != 3 and grid[row, column] != 4 and grid[row, column] != 6):
                        color = WHITE
                        pygame.draw.rect(screen,
                                         color,
                                         [(MARGIN+LENGTHCELL) * column + MARGIN,
                                          (MARGIN+HIGHCELL) * row + MARGIN,
                                          LENGTHCELL,
                                          HIGHCELL])
                    if grid[row, column] == 1:
                        color = BROWN
                        pygame.draw.rect(screen,
                                         color,
                                         [(MARGIN+LENGTHCELL) * column + MARGIN,
                                          (MARGIN+HIGHCELL) * row + MARGIN,
                                          LENGTHCELL,
                                          HIGHCELL])
                    if grid[row, column] == 2:

                        imagen_redimensionada = pygame.transform.scale(
                            self.__imgMario, (45, 45))
                        screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                            (MARGIN+HIGHCELL) *
                                                            row + MARGIN,
                                                            LENGTHCELL,
                                                            HIGHCELL])
                        """
                        color = ROJO
                        pygame.draw.rect(screen,
                                        color,
                                        [(MARGIN+LENGTHCELL) * column + MARGIN,
                                        (MARGIN+HIGHCELL) * row + MARGIN,
                                            LENGTHCELL,
                                            HIGHCELL])"""
                    if grid[row, column] == 5:

                        imagen_redimensionada = pygame.transform.scale(
                            self.__imgKoopa, (45, 45))
                        screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                            (MARGIN+HIGHCELL) *
                                                            row + MARGIN,
                                                            LENGTHCELL,
                                                            HIGHCELL])
                        """
                        color = VERDE
                        pygame.draw.rect(screen,
                                        color,
                                        [(MARGIN+LENGTHCELL) * column + MARGIN,
                                        (MARGIN+HIGHCELL) * row + MARGIN,
                                        LENGTHCELL,
                                        HIGHCELL])"""
                    if grid[row, column] == 3:

                        imagen_redimensionada = pygame.transform.scale(
                            self.__imgStar, (45, 45))
                        screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                            (MARGIN+HIGHCELL) *
                                                            row + MARGIN,
                                                            LENGTHCELL,
                                                            HIGHCELL])
                        """
                        color = salom
                        pygame.draw.rect(screen,
                                        color,
                                        [(MARGIN+LENGTHCELL) * column + MARGIN,
                                        (MARGIN+HIGHCELL) * row + MARGIN,
                                        LENGTHCELL,
                                        HIGHCELL])"""
                    if grid[row, column] == 4:

                        imagen_redimensionada = pygame.transform.scale(
                            self.__imgFlower, (45, 45))
                        screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                            (MARGIN+HIGHCELL) *
                                                            row + MARGIN,
                                                            LENGTHCELL,
                                                            HIGHCELL])
                        """
                        color = PINK
                        pygame.draw.rect(screen,
                                        color,
                                        [(MARGIN+LENGTHCELL) * column + MARGIN,
                                        (MARGIN+HIGHCELL) * row + MARGIN,
                                        LENGTHCELL,
                                        HIGHCELL])"""
                    if grid[row, column] == 6:

                        imagen_redimensionada = pygame.transform.scale(
                            self.__imgPrincess, (45, 45))
                        screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                            (MARGIN+HIGHCELL) *
                                                            row + MARGIN,
                                                            LENGTHCELL,
                                                            HIGHCELL])
                    if grid[row, column] == 8:
                        imagen_redimensionada = pygame.transform.scale(
                            self.__imgMarioAndPrincess, (45, 45))
                        screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                            (MARGIN+HIGHCELL) *
                                                            row + MARGIN,
                                                            LENGTHCELL,
                                                            HIGHCELL])
                    """ 
                    color = YELLOW
                    pygame.draw.rect(screen,
                                        color,
                                        [(MARGIN+LENGTHCELL) * column + MARGIN,
                                        (MARGIN+HIGHCELL) * row + MARGIN,
                                        LENGTHCELL,
                                        HIGHCELL])"""

            # limit to 1 frames per second.
            clock.tick(1)

            # update world
            grid = self.__solutionWorlds[i]
            # check that the length is not exceeded
            if (not (i+1 >= len(self.__solutionWorlds))):
                i += 1

            # advance and update the screen with what we have drawn.
            pygame.display.flip()

        # Close
        # pygame.quit()
