import numpy as np
from node import Node

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

print(currentNode.getFather().getDepth())
print(currentNode.getState())
print(currentNode.recreateSolution())
