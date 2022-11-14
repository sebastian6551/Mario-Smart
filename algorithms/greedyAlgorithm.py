from node import Node
from time import process_time
import heapq


class GreedyAlgorithm:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.marioPos = self.firstNode.searchForMario()
        self.princessPos = self.searchForPrincess(world)
        self.stack = [self.firstNode]
        self.computingTime = ""

    def getNodeMinHeuristic(self, stack):
        minNode = min(stack, key=lambda node: node.getHeuristic())
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
        starts = currentNode.searchForStart()
        start1 = starts[0]
        start2 = starts[1]
        flowers = currentNode.searchForFlower()
        flower1 = flowers[0]
        flower2 = flowers[1]
        while not (currentNode.isGoal()):
            # Check if right side is free
            # if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1 and currentNode.getFather().getOperator() != "left"):
            print("---")
            print(currentNode.getMarioPos())
            if (not (marioPos[1]+1 > 9) and currentNode.getState()[marioPos[0], marioPos[1]+1] != 1):
                # if (currentNode.compareCicles("right")):
                son = Node(currentNode.getState(), currentNode,
                           "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setNewCost(son.rightMovement(marioPos))
                son.setMarioPos(son.rightMovement(marioPos))
                #son.setMarioPos([marioPos[0], marioPos[1]+1])
                son.moveRight(marioPos)
                # son.searchForMario()
                sonManhattanDistance = son.calculateManhattanDistance(
                    self.princessPos)
                sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                son.setHeuristic(sonHeuristic)
                if (son.compareCicles2("right", start1, start2, flower1, flower2)):
                    stack.append(son)
                    son.searchForMario()
                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            # Check if left side is free
            # if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1 and currentNode.getFather().getOperator() != "right"):
            if (not (marioPos[1]-1 < 0) and currentNode.getState()[marioPos[0], marioPos[1]-1] != 1):
               # if (currentNode.compareCicles("left")):
                son = Node(currentNode.getState(), currentNode,
                           "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setMarioPos([marioPos[0], marioPos[1]-1])
                son.setNewCost(son.leftMovement(marioPos))
                son.moveLeft(marioPos)
                # son.searchForMario()
                sonManhattanDistance = son.calculateManhattanDistance(
                    self.princessPos)
                sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                son.setHeuristic(sonHeuristic)
                if (son.compareCicles2("left", start1, start2, flower1, flower2)):
                    stack.append(son)
                    son.searchForMario()
                    if (son.getDepth() > depth):
                        depth = son.getDepth()
                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            # Check if down side is free
            # if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "up"):
            if (not (marioPos[0]+1 > 9) and currentNode.getState()[marioPos[0]+1, marioPos[1]] != 1):
               # if (currentNode.compareCicles("down")):
                son = Node(currentNode.getState(), currentNode,
                           "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setMarioPos([marioPos[0]+1, marioPos[1]])
                son.setNewCost(son.downMovement(marioPos))
                son.moveDown(marioPos)
                # son.searchForMario()
                sonManhattanDistance = son.calculateManhattanDistance(
                    self.princessPos)
                sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                son.setHeuristic(sonHeuristic)
                if (son.compareCicles2("down", start1, start2, flower1, flower2)):
                    stack.append(son)
                    son.searchForMario()
                    if (son.getDepth() > depth):
                        depth = son.getDepth()
                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            # Check if up side is free
            # if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1 and currentNode.getFather().getOperator() != "down"):
            if (not (marioPos[0]-1 < 0) and currentNode.getState()[marioPos[0]-1, marioPos[1]] != 1):
                # if (currentNode.compareCicles("up")):
                son = Node(currentNode.getState(), currentNode,
                           "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                son.setMarioPos([marioPos[0]-1, marioPos[1]])
                son.setNewCost(son.upMovement(marioPos))
                son.moveUp(marioPos)
                # son.searchForMario()
                sonManhattanDistance = son.calculateManhattanDistance(
                    self.princessPos)
                sonHeuristic = son.calculateHeuristic(sonManhattanDistance)
                son.setHeuristic(sonHeuristic)
                if (son.compareCicles2("up", start1, start2, flower1, flower2)):
                    stack.append(son)
                    son.searchForMario()
                    if (son.getDepth() > depth):
                        depth = son.getDepth()
                    print(son.getMarioPos(), "heurística: ", son.getHeuristic())

            stack.remove(currentNode)
            expandedNodes += 1
            currentNode = self.getNodeMinHeuristic(stack)
            starts = currentNode.searchForStart()
            start1 = starts[0]
            start2 = starts[1]
            flowers = currentNode.searchForFlower()
            flower1 = flowers[0]
            flower2 = flowers[1]
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
