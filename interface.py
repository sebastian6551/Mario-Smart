import pygame
from algorithms.depthAlgorithm import DepthAlgorithm
from algorithms.amplitudeAlgorithm import AmplitudeAlgorithm
from algorithms.costAlgorithm import CostAlgorithm

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)  # FREE 0
BROWN = (139, 69, 19)  # BLOCK 1
# Set the length and width of each grid cell.
LENGTHCELL = 45
HIGHCELL = 45
# Set the margin between the cells.
MARGIN = 5
algorithm = None


class Interface:

    def __init__(self, initWorld):
        self.__initWorld = initWorld
        self.__solutionWorlds = None
        self.__imgMario = None
        self.__imgKoopa = None
        self.__imgPrincess = None
        self.__imgStar = None
        self.__imgFlower = None
        self.__imgMarioAndPrincess = None

    def setSolutionWorld(self, newSolutionWorlds):
        self.__solutionWorlds = newSolutionWorlds

    def loadImages(self):
        self.__imgMario = pygame.image.load("images/mario.jpg").convert()
        self.__imgKoopa = pygame.image.load("images/koopa.jpg").convert()
        self.__imgPrincess = pygame.image.load(
            "images/princess2.jpg").convert()
        self.__imgStar = pygame.image.load("images/star.jpg").convert()
        self.__imgFlower = pygame.image.load("images/flower.jpg").convert()
        self.__imgMarioAndPrincess = pygame.image.load(
            "images/mario&princess.jpg").convert()

    def showText(self, pantalla, fuente, texto, color, dimensiones, x, y):
        tipo_letra = pygame.font.Font(fuente, dimensiones)
        superficie = tipo_letra.render(texto, True, color)
        rectangulo = superficie.get_rect()
        rectangulo.center = (x, y)
        pantalla.blit(superficie, rectangulo)

    def interfaceSolution(self, press, grid, i, screen, clock):
        while not press:
            # prueba para boton
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    press = True

                    # draw the grid
            for row in range(10):
                for column in range(10):
                    if (grid[row, column] != 1 and grid[row, column] != 2 and grid[row, column] != 5 and grid[row, column] != 3 and grid[row, column] != 4 and grid[row, column] != 6):
                        color = WHITE
                        pygame.draw.rect(screen,
                                         color,
                                         [(MARGIN+LENGTHCELL) * column + MARGIN,
                                          (MARGIN+HIGHCELL) *
                                          row + MARGIN,
                                          LENGTHCELL,
                                          HIGHCELL])
                    if grid[row, column] == 1:
                        color = BROWN
                        pygame.draw.rect(screen,
                                         color,
                                         [(MARGIN+LENGTHCELL) * column + MARGIN,
                                          (MARGIN+HIGHCELL) *
                                          row + MARGIN,
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
                    if grid[row, column] == 5:

                        imagen_redimensionada = pygame.transform.scale(
                            self.__imgKoopa, (45, 45))
                        screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                            (MARGIN+HIGHCELL) *
                                                            row + MARGIN,
                                                            LENGTHCELL,
                                                            HIGHCELL])
                    if grid[row, column] == 3:

                        imagen_redimensionada = pygame.transform.scale(
                            self.__imgStar, (45, 45))
                        screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                            (MARGIN+HIGHCELL) *
                                                            row + MARGIN,
                                                            LENGTHCELL,
                                                            HIGHCELL])
                    if grid[row, column] == 4:

                        imagen_redimensionada = pygame.transform.scale(
                            self.__imgFlower, (45, 45))
                        screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                            (MARGIN+HIGHCELL) *
                                                            row + MARGIN,
                                                            LENGTHCELL,
                                                            HIGHCELL])
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

    def showInterface(self):
        # Initialize pygame
        pygame.init()

        # Set the length and width of the screen
        WINDOW_DIMENSION = [800, 510]  # 510,510
        screen = pygame.display.set_mode(WINDOW_DIMENSION)

        # iterate until the user presses the exit button.
        press = False

        # use it to set how fast the screen refreshes.
        clock = pygame.time.Clock()

        i = 1
        self.loadImages()
        #grid = self.__solutionWorlds[0]
        grid = self.__initWorld

        # Set the screen background.
        screen.fill(BLACK)

        pygame.display.set_caption("Mario smart")

        self.showText(screen, pygame.font.match_font(
            'arial'), "Amplitud", WHITE, 35, 655, 20)

        self.showText(screen, pygame.font.match_font(
            'arial'), "Profundidad", WHITE, 35, 655, 50)

        self.showText(screen, pygame.font.match_font(
            'arial'), "Costo", WHITE, 35, 655, 80)

        self.showText(screen, pygame.font.match_font(
            'arial'), "Avara", WHITE, 35, 655, 110)

        self.showText(screen, pygame.font.match_font(
            'arial'), "A*", WHITE, 35, 655, 140)

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
                if grid[row, column] == 5:

                    imagen_redimensionada = pygame.transform.scale(
                        self.__imgKoopa, (45, 45))
                    screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                        (MARGIN+HIGHCELL) *
                                                        row + MARGIN,
                                                        LENGTHCELL,
                                                        HIGHCELL])
                if grid[row, column] == 3:

                    imagen_redimensionada = pygame.transform.scale(
                        self.__imgStar, (45, 45))
                    screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                        (MARGIN+HIGHCELL) *
                                                        row + MARGIN,
                                                        LENGTHCELL,
                                                        HIGHCELL])
                if grid[row, column] == 4:

                    imagen_redimensionada = pygame.transform.scale(
                        self.__imgFlower, (45, 45))
                    screen.blit(imagen_redimensionada, [(MARGIN+LENGTHCELL) * column + MARGIN,
                                                        (MARGIN+HIGHCELL) *
                                                        row + MARGIN,
                                                        LENGTHCELL,
                                                        HIGHCELL])
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
        pygame.display.flip()
        # --------Main Program Loop-----------
        while not press:
            # prueba para boton
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    press = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0] > 598 and pos[0] < 713 and pos[1] > 8 and pos[1] < 29:
                        print("Amplitud")
                        # Set the title of the screen.
                        pygame.display.set_caption("Mario smart amplitud")
                        algorithm = AmplitudeAlgorithm(self.__initWorld)
                        solutionWorld = algorithm.start()
                        self.setSolutionWorld(solutionWorld)
                        self.interfaceSolution(press, grid, i, screen, clock)
                    elif pos[0] > 581 and pos[0] < 732 and pos[1] > 42 and pos[1] < 62:
                        print("Profundidad")
                        # Set the title of the screen.
                        pygame.display.set_caption("Mario smart profundidad")
                        algorithm = DepthAlgorithm(self.__initWorld)
                        solutionWorld = algorithm.start()
                        self.setSolutionWorld(solutionWorld)
                        self.interfaceSolution(press, grid, i, screen, clock)
                    elif pos[0] > 618 and pos[0] < 692 and pos[1] > 70 and pos[1] < 90:
                        print("Costo")
                        # Set the title of the screen.
                        pygame.display.set_caption("Mario smart costo")
                        algorithm = CostAlgorithm(self.__initWorld)
                        solutionWorld = algorithm.start()
                        self.setSolutionWorld(solutionWorld)
                        self.interfaceSolution(press, grid, i, screen, clock)
                    elif pos[0] > 619 and pos[0] < 692 and pos[1] > 101 and pos[1] < 123:
                        print("Avara")
                        # Set the title of the screen.
                        """pygame.display.set_caption("Mario smart avara")
                        algorithm = DepthAlgorithm(self.__initWorld)
                        solutionWorld = algorithm.start()
                        self.setSolutionWorld(solutionWorld)
                        self.interfaceSolution(press, grid, i, screen, clock)"""
                    elif pos[0] > 641 and pos[0] < 692 and pos[1] > 130 and pos[1] < 153:
                        print("A*")
                        # Set the title of the screen.
                        """pygame.display.set_caption("Mario smart A*")
                        algorithm = DepthAlgorithm(self.__initWorld)
                        solutionWorld = algorithm.start()
                        self.setSolutionWorld(solutionWorld)
                        self.interfaceSolution(press, grid, i, screen, clock)"""
                    # print(pos[0])
                    # print(pos[1])