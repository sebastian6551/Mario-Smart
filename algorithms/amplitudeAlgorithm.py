from node import Node
from time import process_time


class AmplitudeAlgorithm:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.marioPos = self.firstNode.searchForMario()
        self.stack = [self.firstNode]
        self.computingTime = ""

    def getComputingTime(self):
        return self.computingTime

    def setComputingTime(self, computingTime):
        self.computingTime = computingTime

    def start(self):
        startTime = process_time()

        stack = self.stack
        marioPos = self.marioPos
        currentNode = stack[0]
        expandedNodes = 0
        depth = 0

        while not (currentNode.isGoal()):
            # Check if right side is free
            # print("---")
            # print(currentNode.getMarioPos())
            if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1):
                son = Node(currentNode.getState(), currentNode,
                           "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                right = son.rightMovement(marioPos)
                son.setNewCost(right)
                son.setMarioPos(right)
                son.moveRight(marioPos)
                if (son.avoidGoBack2(right)):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    # print(son.getMarioPos())

            # Check if left side is free
            if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1):
                son = Node(currentNode.getState(), currentNode,
                           "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                left = son.leftMovement(marioPos)
                son.setNewCost(left)
                son.setMarioPos(left)
                son.moveLeft(marioPos)
                if (son.avoidGoBack2(left)):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    # print(son.getMarioPos())

            # Check if down side is free
            if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1):
                son = Node(currentNode.getState(), currentNode,
                           "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                down = son.downMovement(marioPos)
                son.setNewCost(down)
                son.setMarioPos(down)
                son.moveDown(marioPos)
                if (son.avoidGoBack2(down)):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    # print(son.getMarioPos())

            # Check if up side is free
            if not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1:
                son = Node(currentNode.getState(), currentNode,
                           "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                up = son.upMovement(marioPos)
                son.setNewCost(up)
                son.setMarioPos(up)
                son.moveUp(marioPos)
                if son.avoidGoBack2(up):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()
                    # print(son.getMarioPos())

            stack.pop(0)

            currentNode = stack[0]
            expandedNodes += 1
            marioPos = currentNode.getMarioPos()

        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("Nodos expandidos: ", expandedNodes+1)  # Good
        print("Profundidad: ", depth)
        print("El costo final de la solución es: " + str(currentNode.getCost()))
        print(currentNode.recreateSolution())
        return [solutionWorld, expandedNodes + 1, depth]
