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
    if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1 and currentNode.getFather().getOperator() != "left"):
        son = Node(currentNode.getState(), currentNode,
                   "right", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
        son.moveRight(marioPos)
        stack.append(son)

    # Check if left side is free
    if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1 and currentNode.getFather().getOperator() != "right"):
        son = Node(currentNode.getState(), currentNode,
                   "left", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
        son.moveLeft(marioPos)
        stack.append(son)

    # Check if down side is free
    if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "up"):
        son = Node(currentNode.getState(), currentNode,
                   "down", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
        son.moveDown(marioPos)
        stack.append(son)

    # Check if up side is free
    if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "down"):
        son = Node(currentNode.getState(), currentNode,
                   "up", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
        son.moveUp(marioPos)
        stack.append(son)
    stack.pop(0)

    currentNode = stack[0]
    marioPos = currentNode.searchForMario()

# print(currentNode.getFather().getDepth())
# print(currentNode.getState())
# print(currentNode.recreateSolution())
solution = currentNode.recreateSolutionWorld()
solution2 = solution[::-1]


# Definimos algunos colores
PINK = (255, 0, 255)  # Flower 4
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)  # Empty 0
VERDE = (0, 255, 0)  # Koopa 5
ROJO = (255, 0, 0)  # Mario 2
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)  # princesa 6
salom = (250, 128, 114)  # Start 3
brown = (139, 69, 19)  # Obstaculo 1


# Establecemos el LARGO y ALTO de cada celda de la retícula.
LARGO = 45
ALTO = 45

# Establecemos el margen entre las celdas.
MARGEN = 5

# Creamos un array bidimensional. Un array bidimensional
# no es más que una lista de listas.
grid = solution2[0]

# Inicializamos pygame
pygame.init()

# Establecemos el LARGO y ALTO de la pantalla
DIMENSION_VENTANA = [510, 510]  # 255,255
pantalla = pygame.display.set_mode(DIMENSION_VENTANA)

# Establecemos el título de la pantalla.
pygame.display.set_caption("Mario smart")

# Iteramos hasta que el usuario pulse el botón de salir.
hecho = False

# Lo usamos para establecer cuán rápido de refresca la pantalla.
reloj = pygame.time.Clock()

i = 1
imagen_protagonista = pygame.image.load("mario.jpg").convert()
imagen_koopa = pygame.image.load("koopa.jpg").convert()
imagen_princess = pygame.image.load("princess2.jpg").convert()
imagen_start = pygame.image.load("start.jpg").convert()
imagen_flower = pygame.image.load("flower.jpg").convert()
# -------- Bucle Principal del Programa-----------
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
    # Establecemos el fondo de pantalla.
    pantalla.fill(NEGRO)

    # Dibujamos la retícula
    for fila in range(10):
        for columna in range(10):
            #color = BLANCO
            if (grid[fila, columna] != 1 and grid[fila, columna] != 2 and grid[fila, columna] != 5 and grid[fila, columna] != 3 and grid[fila, columna] != 4 and grid[fila, columna] != 6):
                color = BLANCO
                pygame.draw.rect(pantalla,
                                 color,
                                 [(MARGEN+LARGO) * columna + MARGEN,
                                  (MARGEN+ALTO) * fila + MARGEN,
                                     LARGO,
                                     ALTO])
            if grid[fila, columna] == 1:
                color = brown
                pygame.draw.rect(pantalla,
                                 color,
                                 [(MARGEN+LARGO) * columna + MARGEN,
                                  (MARGEN+ALTO) * fila + MARGEN,
                                     LARGO,
                                     ALTO])
            if grid[fila, columna] == 2:
                color = ROJO
                imagen_redimensionada = pygame.transform.scale(
                    imagen_protagonista, (45, 45))
                pantalla.blit(imagen_redimensionada, [(MARGEN+LARGO) * columna + MARGEN,
                                                      (MARGEN+ALTO) *
                                                      fila + MARGEN,
                                                      LARGO,
                                                      ALTO])
                """pygame.draw.rect(pantalla,
                                 color,
                                 [(MARGEN+LARGO) * columna + MARGEN,
                                  (MARGEN+ALTO) * fila + MARGEN,
                                     LARGO,
                                     ALTO])"""
            if grid[fila, columna] == 5:
                color = VERDE

                imagen_redimensionada = pygame.transform.scale(
                    imagen_koopa, (45, 45))
                pantalla.blit(imagen_redimensionada, [(MARGEN+LARGO) * columna + MARGEN,
                                                      (MARGEN+ALTO) *
                                                      fila + MARGEN,
                                                      LARGO,
                                                      ALTO])
                """pygame.draw.rect(pantalla,
                                 color,
                                 [(MARGEN+LARGO) * columna + MARGEN,
                                  (MARGEN+ALTO) * fila + MARGEN,
                                  LARGO,
                                  ALTO])"""
            if grid[fila, columna] == 3:
                color = salom
                imagen_redimensionada = pygame.transform.scale(
                    imagen_start, (45, 45))
                pantalla.blit(imagen_redimensionada, [(MARGEN+LARGO) * columna + MARGEN,
                                                      (MARGEN+ALTO) *
                                                      fila + MARGEN,
                                                      LARGO,
                                                      ALTO])
                """pygame.draw.rect(pantalla,
                                 color,
                                 [(MARGEN+LARGO) * columna + MARGEN,
                                  (MARGEN+ALTO) * fila + MARGEN,
                                  LARGO,
                                  ALTO])"""
            if grid[fila, columna] == 4:
                color = PINK
                imagen_redimensionada = pygame.transform.scale(
                    imagen_flower, (45, 45))
                pantalla.blit(imagen_redimensionada, [(MARGEN+LARGO) * columna + MARGEN,
                                                      (MARGEN+ALTO) *
                                                      fila + MARGEN,
                                                      LARGO,
                                                      ALTO])
                """pygame.draw.rect(pantalla,
                                 color,
                                 [(MARGEN+LARGO) * columna + MARGEN,
                                  (MARGEN+ALTO) * fila + MARGEN,
                                  LARGO,
                                  ALTO])"""
            if grid[fila, columna] == 6:
                color = YELLOW

                imagen_redimensionada = pygame.transform.scale(
                    imagen_princess, (45, 45))
                pantalla.blit(imagen_redimensionada, [(MARGEN+LARGO) * columna + MARGEN,
                                                      (MARGEN+ALTO) *
                                                      fila + MARGEN,
                                                      LARGO,
                                                      ALTO])
            """ pygame.draw.rect(pantalla,
                                 color,
                                 [(MARGEN+LARGO) * columna + MARGEN,
                                  (MARGEN+ALTO) * fila + MARGEN,
                                  LARGO,
                                  ALTO])"""
            """else:
                color = BLANCO
                pygame.draw.rect(pantalla,
                                 color,
                                 [(MARGEN+LARGO) * columna + MARGEN,
                                  (MARGEN+ALTO) * fila + MARGEN,
                                  LARGO,
                                  ALTO])"""

    # Limitamos a 60 fotogramas por segundo.
    reloj.tick(1)
    grid = solution2[i]
    i += 1

    # Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()

# Pórtate bien con el IDLE.
# pygame.quit()
