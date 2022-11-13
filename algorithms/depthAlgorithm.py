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
        depth = 0
        while not (stack[0].isGoal()):
            print("---")
            print(stack[0].getMarioPos())

            stack.pop(0)
            expandedNodes += 1
            # Check if right side is free
            if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1):
                if (currentNode.compareCicles("right")):
                    # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "right") and currentNode.compareFatherAll(marioPos, marioPos0, "right")):
                    son = Node(currentNode.getState(), currentNode,
                               "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                    son.setNewCost(son.rightMovement(marioPos))
                    son.setMarioPos(son.rightMovement(marioPos))
                    son.moveRight(marioPos)
                    stack.insert(0, son)
                    
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos())

            # Check if left side is free
            # if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1 and currentNode.getFather().getOperator() != "right"):
            if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1):
                if (currentNode.compareCicles("left")):
                    # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "left") and currentNode.compareFatherAll(marioPos, marioPos0, "left")):
                    son = Node(currentNode.getState(), currentNode,
                               "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                    son.setNewCost(son.leftMovement(marioPos))
                    son.setMarioPos(son.leftMovement(marioPos))
                    son.moveLeft(marioPos)
                    stack.insert(0, son)
                    
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos())

            # Check if down side is free
            # if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "up"):
            if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1):
                if (currentNode.compareCicles("down")):
                    # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "down") and currentNode.compareFatherAll(marioPos, marioPos0, "down")):
                    son = Node(currentNode.getState(), currentNode,
                               "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                    son.setNewCost(son.downMovement(marioPos))
                    son.setMarioPos(son.downMovement(marioPos))
                    son.moveDown(marioPos)
                    stack.insert(0, son)
                    
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos())

            # Check if up side is free
            # if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "down"):
            if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1):
                if (currentNode.compareCicles("up")):
                    # if (currentNode.compareStateCicle(currentNode.getFather(), marioPos, "up") and currentNode.compareFatherAll(marioPos, marioPos0, "up")):
                    son = Node(currentNode.getState(), currentNode,
                               "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                    son.setNewCost(son.upMovement(marioPos))
                    son.setMarioPos(son.upMovement(marioPos))
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
