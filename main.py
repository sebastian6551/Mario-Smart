import numpy as np
from node import Node
import pygame
WIDTH = 10
HEIGHT = 10

with open('matriz.txt', 'r') as f:
    board_txt = ''.join(f.readlines()).replace('\n', ';')

world = np.matrix(board_txt)

emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
firstNode = Node(world, emptyNode, " ", 0, 0, 0, 0)
marioPos = firstNode.searchForMario()
stack = []
stack.append(firstNode)

currentNode = stack[0]
while (not (stack[0].isGoal(marioPos[0], marioPos[1]))):
    # Check if right side is free
    # if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1 and currentNode.getFather().getOperator() != "left"):
    if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1):
        if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "right")):
            son = Node(currentNode.getState(), currentNode,
                       "right", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
            son.moveRight(marioPos)
            stack.append(son)

    # Check if left side is free
    # if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1 and currentNode.getFather().getOperator() != "right"):
    if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1):
        if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "left")):
            son = Node(currentNode.getState(), currentNode,
                       "left", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
            son.moveLeft(marioPos)
            stack.append(son)

    # Check if down side is free
    # if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "up"):
    if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1):
        if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "down")):
            son = Node(currentNode.getState(), currentNode,
                       "down", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
            son.moveDown(marioPos)
            stack.append(son)

    # Check if up side is free
    # if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "down"):
    if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1):
        if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "up")):
            son = Node(currentNode.getState(), currentNode,
                       "up", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
            son.moveUp(marioPos)
            stack.append(son)
    print(len(stack))
    stack.pop(0)
    currentNode = stack[0]
    marioPos = currentNode.searchForMario()

# print(currentNode.getFather().getDepth())
# print(currentNode.getState())
# print(currentNode.recreateSolution())
solution = currentNode.recreateSolutionWorld()
solutionWorld = solution[::-1]


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)  # BLOCK 1

# Set the length and width of each grid cell.
LENGTHCELL = 45
HIGHCELL = 45

# Set the margin between the cells.
MARGIN = 5

grid = solutionWorld[0]

# Initialize pygame
pygame.init()

# Set the length and width of the screen
WINDOW_DIMENSION = [510, 510]  # 255,255
screen = pygame.display.set_mode(WINDOW_DIMENSION)

# Set the title of the screen.
pygame.display.set_caption("Mario smart amplitud")

# iterate until the user presses the exit button.
press = False

# use it to set how fast the screen refreshes.
clock = pygame.time.Clock()

i = 1
imgMario = pygame.image.load("mario.jpg").convert()
imgKoopa = pygame.image.load("koopa.jpg").convert()
imgPrincess = pygame.image.load("princess2.jpg").convert()
imgStart = pygame.image.load("start.jpg").convert()
imgFlower = pygame.image.load("flower.jpg").convert()


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
                    imgMario, (45, 45))
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
                    imgKoopa, (45, 45))
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
                    imgStart, (45, 45))
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
                    imgFlower, (45, 45))
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
                    imgPrincess, (45, 45))
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
    grid = solutionWorld[i]
    # check that the length is not exceeded
    if (not (i+1 >= len(solutionWorld))):
        i += 1

    # advance and update the screen with what we have drawn.
    pygame.display.flip()

# Close
# pygame.quit()
