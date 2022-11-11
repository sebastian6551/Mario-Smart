from node import Node
from time import process_time


class DepthAlgorithm:

    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        #marioPos0 = firstNode.searchForMario()
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
        #marioPos0 = self.marioPos0

        currentNode = stack[0]
        expandedNodes = 0
        while not (stack[0].isGoal()):
            print("---")
            print(stack[0].getMarioPos())

            stack.pop(0)
            expandedNodes += 1
            # Check if right side is free
            if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1):
                if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "right")):
                    # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "right") and currentNode.compareFatherAll(marioPos, marioPos0, "right")):
                    son = Node(currentNode.getState(), currentNode,
                               "right", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
                    son.moveRight(marioPos)
                    stack.insert(0, son)
                    son.searchForMario()
                    print(son.getMarioPos())

            # Check if left side is free
            # if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1 and currentNode.getFather().getOperator() != "right"):
            if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1):
                if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "left")):
                    # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "left") and currentNode.compareFatherAll(marioPos, marioPos0, "left")):
                    son = Node(currentNode.getState(), currentNode,
                               "left", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
                    son.moveLeft(marioPos)
                    stack.insert(0, son)
                    son.searchForMario()
                    print(son.getMarioPos())

            # Check if down side is free
            # if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "up"):
            if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1):
                if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "down")):
                    # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "down") and currentNode.compareFatherAll(marioPos, marioPos0, "down")):
                    son = Node(currentNode.getState(), currentNode,
                               "down", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
                    son.moveDown(marioPos)
                    stack.insert(0, son)
                    son.searchForMario()
                    print(son.getMarioPos())

            # Check if up side is free
            # if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "down"):
            if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1):
                if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "up")):
                    # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "up") and currentNode.compareFatherAll(marioPos, marioPos0, "up")):
                    son = Node(currentNode.getState(), currentNode,
                               "up", currentNode.getDepth() + 1, currentNode.getCost() + 1, currentNode.getStar(), currentNode.getFlower())
                    son.moveUp(marioPos)
                    stack.insert(0, son)
                    son.searchForMario()
                    print(son.getMarioPos())
            currentNode = stack[0]
            marioPos = currentNode.searchForMario()

        # print(currentNode.getFather().getDepth())
        # print(currentNode.getState())
        # print(currentNode.recreateSolution())
        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print(expandedNodes+1)  # Good
        print(stack[0].recreateSolution())
        return [solutionWorld, expandedNodes+1]
