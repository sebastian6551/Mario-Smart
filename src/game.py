import pygame

# Initial settings
# Screen
width = 600
height = 600

# Board
rows = 10
columns = 10
squareSize = width // columns


class Game:

    def __init__(self):
        pass

    def showBoard(self, surface, world):
        for i in range(rows):
            for j in range(columns):

                # Free squares
                if (world[j][i] == 0):
                    color = (255, 255, 255) if (
                        i + j) % 2 == 0 else (255, 230, 230)

                    square = (i * squareSize, j * squareSize,
                              squareSize, squareSize)

                    pygame.draw.rect(surface, color, square)

                # Walls
                elif (world[j][i] == 1):
                    img = pygame.image.load("./assets/block.webp")
                    self.setSquare(surface, squareSize, img, i, j)

                # Start
                elif (world[j][i] == 2):
                    img = pygame.image.load("./assets/superMarioBros.png")
                    self.setSquare(surface, squareSize-10, img, i, j)

                # Super star
                elif (world[j][i] == 3):
                    img = pygame.image.load("./assets/superStar.webp")
                    self.setSquare(surface, squareSize-10, img, i, j)

                # Fire flower
                elif (world[j][i] == 4):
                    img = pygame.image.load("./assets/fireFlower.png")
                    self.setSquare(surface, squareSize-10, img, i, j)

                # Koopa
                elif (world[j][i] == 5):
                    img = pygame.image.load("./assets/bowser.png")
                    self.setSquare(surface, squareSize-10, img, i, j)

                # Princess Peach
                elif (world[j][i] == 6):
                    img = pygame.image.load("./assets/peach.png")
                    self.setSquare(surface, squareSize-10, img, i, j)

    def setSquare(self, surface, size, imgOriginal, i, j):

        color = (255, 255, 255) if (i + j) % 2 == 0 else (255, 230, 230)

        square = (i * squareSize, j * squareSize, squareSize, squareSize)

        pygame.draw.rect(surface, color, square)

        img = pygame.transform.scale(imgOriginal, (size, size))

        img_center = (i * squareSize + squareSize // 2,
                      j * squareSize + squareSize // 2)

        texture = img.get_rect(center=img_center)

        surface.blit(img, texture)
