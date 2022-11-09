from node import Node
from time import process_time

class GreedyAlgorithm:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.marioPos = self.firstNode.searchForMario()
        self.princessPos = self.searchForPrincess(world) 
        self.stack = [self.firstNode]
        self.computingTime = ""

    def getNodeMinCost(self, stack):
        minNode = min(stack, key=lambda node: node.getCost())
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

        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)
