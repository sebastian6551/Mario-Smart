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
        marioPos0 = self.marioPos
        currentNode = stack[0]
        expandedNodes = 0
        depth = 0
        starts = currentNode.searchForStart()
        start1 = starts[0]
        start2 = starts[1]
        flowers = currentNode.searchForFlower()
        flower1 = flowers[0]
        flower2 = flowers[1]
        while not (stack[0].isGoal()):
            # Check if right side is free
            # if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1 and currentNode.getFather().getOperator() != "left"):
            print("---")
            print(stack[0].getMarioPos())
            if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1):
                # if (currentNode.avoidGoBack("right", start1, start2, flower1, flower2)):

                son = Node(currentNode.getState(), currentNode,
                           "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setNewCost(son.rightMovement(marioPos))
                son.moveRight(marioPos)
                if (son.avoidGoBack2("right", start1, start2, flower1, flower2)):
                    stack.append(son)
                    son.searchForMario()
                    if (son.getDepth() > depth):
                        depth = son.getDepth()
                    print(son.getMarioPos())

            # Check if left side is free
            # if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1 and currentNode.getFather().getOperator() != "right"):
            if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1):
               # if (currentNode.avoidGoBack("left", start1, start2, flower1, flower2)):
                son = Node(currentNode.getState(), currentNode,
                           "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setNewCost(son.leftMovement(marioPos))
                son.moveLeft(marioPos)
                if (son.avoidGoBack2("left", start1, start2, flower1, flower2)):
                    stack.append(son)
                    son.searchForMario()
                    if (son.getDepth() > depth):
                        depth = son.getDepth()
                    print(son.getMarioPos())

            # Check if down side is free
            # if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "up"):
            if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1):
               # if (currentNode.avoidGoBack("down", start1, start2, flower1, flower2)):
                son = Node(currentNode.getState(), currentNode,
                           "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setNewCost(son.downMovement(marioPos))
                son.moveDown(marioPos)
                if (son.avoidGoBack2("down", start1, start2, flower1, flower2)):
                    stack.append(son)
                    son.searchForMario()
                    if (son.getDepth() > depth):
                        depth = son.getDepth()
                    print(son.getMarioPos())

            # Check if up side is free
            # if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "down"):
            if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1):
                # if (currentNode.avoidGoBack("up", start1, start2, flower1, flower2)):
                son = Node(currentNode.getState(), currentNode,
                           "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setNewCost(son.upMovement(marioPos))
                son.moveUp(marioPos)
                if (son.avoidGoBack2("up", start1, start2, flower1, flower2)):
                    stack.append(son)
                    son.searchForMario()
                    if (son.getDepth() > depth):
                        depth = son.getDepth()
                    print(son.getMarioPos())
            stack.pop(0)

            currentNode = stack[0]
            expandedNodes += 1
            starts = currentNode.searchForStart()
            start1 = starts[0]
            start2 = starts[1]
            flowers = currentNode.searchForFlower()
            flower1 = flowers[0]
            flower2 = flowers[1]
            marioPos = currentNode.searchForMario()

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
