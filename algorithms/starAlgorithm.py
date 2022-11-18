from node import Node
from time import process_time


class StarAlgorithm:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.marioPos = self.firstNode.searchForMario()
        self.princessPos = self.searchForPrincess(world)
        self.stack = [self.firstNode]
        self.computingTime = ""

    def getNodeMinSumCostHeuristic(self, stack):
        minNode = min(stack, key=lambda node: node.getSumCostHeuristic())
        return minNode

    def getComputingTime(self):
        return self.computingTime

    def setComputingTime(self, computingTime):
        self.computingTime = computingTime

    def searchForPrincess(self, world):
        princessPos = []
        for i in range(10):
            for j in range(10):
                if (world[i, j] == self.firstNode.PRINCESS):
                    princessPos.append(i)
                    princessPos.append(j)
        return princessPos

    def start(self):
        startTime = process_time()

        stack = self.stack
        marioPos = self.marioPos
        currentNode = stack[0]
        expandedNodes = 0
        depth = 0

        while not (currentNode.isGoal()):
            # Check if right side is free
            print("---")
            print(currentNode.getMarioPos())
            if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1):
                # if (currentNode.compareCicles("right")):
                son = Node(currentNode.getState(), currentNode,
                           "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                right = son.rightMovement(marioPos)
                son.setNewCost(right)
                son.setMarioPos(right)
                sonManhattanDistance = son.calculateManhattanDistance(
                    self.princessPos)
                sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                son.setHeuristic(sonHeuristic)
                son.setSumCostHeuristic(son.getHeuristic() + son.getCost())
                son.moveRight(marioPos)
                if (son.avoidGoBack2(right)):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            # Check if left side is free
            if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1):
               # if (currentNode.compareCicles("left")):
                son = Node(currentNode.getState(), currentNode,
                           "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                left = son.leftMovement(marioPos)
                son.setNewCost(left)
                son.setMarioPos(left)
                sonManhattanDistance = son.calculateManhattanDistance(
                    self.princessPos)
                sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                son.setHeuristic(sonHeuristic)
                son.setSumCostHeuristic(son.getHeuristic() + son.getCost())
                son.moveLeft(marioPos)
                if (son.avoidGoBack2(left)):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            # Check if down side is free
            if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1):
               # if (currentNode.compareCicles("down")):
                son = Node(currentNode.getState(), currentNode,
                           "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                down = son.downMovement(marioPos)
                son.setNewCost(down)
                son.setMarioPos(down)
                sonManhattanDistance = son.calculateManhattanDistance(
                    self.princessPos)
                sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                son.setHeuristic(sonHeuristic)
                son.setSumCostHeuristic(son.getHeuristic() + son.getCost())
                son.moveDown(marioPos)
                if (son.avoidGoBack2(down)):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            # Check if up side is free
            if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1):
                # if (currentNode.compareCicles("up")):
                son = Node(currentNode.getState(), currentNode,
                           "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())

                up = son.upMovement(marioPos)
                son.setNewCost(up)
                son.setMarioPos(up)
                sonManhattanDistance = son.calculateManhattanDistance(
                    self.princessPos)
                sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                son.setHeuristic(sonHeuristic)
                son.setSumCostHeuristic(son.getHeuristic() + son.getCost())
                son.moveUp(marioPos)
                if (son.avoidGoBack2(up)):
                    stack.append(son)
                    if (son.getDepth() > depth):
                        depth = son.getDepth()

                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            stack.remove(currentNode)

            currentNode = self.getNodeMinSumCostHeuristic(stack)
            expandedNodes += 1
            marioPos = currentNode.getMarioPos()
            print("Mario pos:", marioPos)

        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        print("Heurística meta: ", currentNode.getHeuristic())
        print(currentNode.recreateSolution())
        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("expandido", expandedNodes+1)  # Good
        print("profundidad", depth)
        print("El costo final de la solución es: " + str(currentNode.getCost()))
        return [solutionWorld, expandedNodes+1, depth]
