import numpy as np
from node import Node

with open('matriz.txt', 'r') as f:
    board_txt = ''.join(f.readlines()).replace('\n', ';')

world = np.matrix(board_txt)


currentNode = Node(world, None, " ", 0, 0)
marioPos = currentNode.searchForMario()
stack = []
stack.append(currentNode)


while (not (stack[0].isGoal(marioPos[0], marioPos[1]))):
    # Check if right side is free
    if (not (marioPos[1]+1 > 9) and stack[0].getState()[marioPos[0], marioPos[1]+1] != 1):
        son = Node(stack[0].getState(), stack[0],
                   "right", stack[0].getDepth() + 1, stack[0].getCost() + 1)
        son.moveRight(marioPos)
        stack.append(son)

    # Check if left side is free
    if (not (marioPos[1]-1 < 0) and stack[0].getState()[marioPos[0], marioPos[1]-1] != 1):
        son = Node(stack[0].getState(), stack[0],
                   "left", stack[0].getDepth() + 1, stack[0].getCost() + 1)
        son.moveLeft(marioPos)
        stack.append(son)

    # Check if down side is free
    if (not (marioPos[0]+1 > 9) and stack[0].getState()[marioPos[0]+1, marioPos[1]] != 1):
        son = Node(stack[0].getState(), stack[0],
                   "down", stack[0].getDepth() + 1, stack[0].getCost() + 1)
        son.moveDown(marioPos)
        stack.append(son)

    # Check if up side is free
    if (not (marioPos[0]-1 < 0) and stack[0].getState()[marioPos[0]-1, marioPos[1]] != 1):
        son = Node(stack[0].getState(), stack[0],
                   "up", stack[0].getDepth() + 1, stack[0].getCost() + 1)
        son.moveUp(marioPos)
        stack.append(son)
    stack.pop(0)
    newNode = stack[0]
    marioPos = newNode.searchForMario()

print(stack[0].getFather().getDepth())
print(stack[0].getState())
