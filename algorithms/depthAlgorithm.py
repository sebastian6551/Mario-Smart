from node import Node
from time import process_time


class DepthAlgorithm:
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
            print("---")
            print(currentNode.getMarioPos())

            stack.pop(0)
            expandedNodes += 1
            # Check if right side is free
            if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1):
                # if (currentNode.compareCicles("right", start1, start2, flower1, flower2)):
                # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "right") and currentNode.compareFatherAll(marioPos, marioPos0, "right")):
                son = Node(currentNode.getState(), currentNode,
                           "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                right = son.rightMovement(marioPos)

                if (son.compareCicles2(right)):
                    son.setNewCost(right)
                    son.setMarioPos(right)

                    son.moveRight(marioPos)
                    stack.insert(0, son)

                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos())

            # Check if left side is free
            # if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1 and currentNode.getFather().getOperator() != "right"):
            if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1):
                # if (currentNode.compareCicles("left", start1, start2, flower1, flower2)):
                # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "left") and currentNode.compareFatherAll(marioPos, marioPos0, "left")):
                son = Node(currentNode.getState(), currentNode,
                           "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                left = son.leftMovement(marioPos)

                if (son.compareCicles2(left)):
                    son.setNewCost(left)
                    son.setMarioPos(left)

                    son.moveLeft(marioPos)
                    stack.insert(0, son)

                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos())

            # Check if down side is free
            # if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "up"):
            if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1):
                # if (currentNode.compareCicles("down", start1, start2, flower1, flower2)):
                # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "down") and currentNode.compareFatherAll(marioPos, marioPos0, "down")):
                son = Node(currentNode.getState(), currentNode,
                           "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                down = son.downMovement(marioPos)

                if (son.compareCicles2(down)):
                    son.setNewCost(down)
                    son.setMarioPos(down)

                    son.moveDown(marioPos)
                    stack.insert(0, son)

                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos())

            # Check if up side is free
            # if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "down"):
            if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1):
                # if (currentNode.compareCicles("up", start1, start2, flower1, flower2)):
                # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "up") and currentNode.compareFatherAll(marioPos, marioPos0, "up")):
                son = Node(currentNode.getState(), currentNode,
                           "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                up = son.upMovement(marioPos)

                if (son.compareCicles2(up)):
                    son.setNewCost(up)
                    son.setMarioPos(up)

                    son.moveUp(marioPos)
                    stack.insert(0, son)

                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos())

            currentNode = stack[0]
            marioPos = currentNode.getMarioPos()

        # print(currentNode.getFather().getDepth())
        # print(currentNode.getState())
        # print(currentNode.recreateSolution())
        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("expandido", expandedNodes+1)  # Good
        print("profundidad", depth)
        print("El costo final de la solución es: " + str(currentNode.getCost()))
        print(stack[0].recreateSolution())
        return [solutionWorld, expandedNodes+1, depth]
