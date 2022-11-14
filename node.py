class Node:

    EMPTY = 0
    BLOCK = 1
    MARIO = 2
    STAR = 3
    KOOPA = 5
    FLOWER = 4
    PRINCESS = 6
    RESCUED_PRINCESS = 8

    def __init__(self, state, father, operator, depth, cost, star, flower):
        self.__state = state
        self.__father = father
        self.__operator = operator
        self.__depth = depth
        self.__cost = cost
        self.__star = star  # It lasts 6 grids - cost 1/2 and they accumulate
        self.__flower = flower  # Cost to go through a koopa when having a flower comes down to 1
        self.__marioPos = []
        self.__heuristic = 0  # The correct value is given only when the greedy algorithm is used
        self.__awaitingCharacter = 0

    def getState(self):
        return self.__state

    def getFather(self):
        return self.__father

    def getOperator(self):
        return self.__operator

    def getDepth(self):
        return self.__depth

    def getCost(self):
        return self.__cost

    def getHeuristic(self):
        return self.__heuristic

    def getMarioPos(self):
        return self.__marioPos

    def getStar(self):
        return self.__star

    def getFlower(self):
        return self.__flower

    def getState(self):
        return self.__state.copy()

    def getAwaitingCharacter(self):
        return self.__awaitingCharacter

    def setState(self, newState):
        self.__state = newState

    def setFather(self, newFather):
        self.__father = newFather

    def setOperator(self, newOperator):
        self.__operator = newOperator

    def setDepth(self, newDepth):
        self.__depth = newDepth

    def setCost(self, newCost):
        self.__cost = newCost

    def setHeuristic(self, newHeuristic):
        self.__heuristic = newHeuristic

    def setMarioPos(self, newMarioPos):
        self.__marioPos = newMarioPos

    def setStar(self, newStarValue):
        self.__star = newStarValue

    def setFlower(self, newFlowerValue):
        self.__flower = newFlowerValue

    def setAwaitingCharacter(self, awaitingCharacter):
        self.__awaitingCharacter = awaitingCharacter

    def calculateManhattanDistance(self, princessPos):
        iDistance = princessPos[0] - self.getMarioPos()[0]
        jDistance = princessPos[1] - self.getMarioPos()[1]
        manhattanDistance = abs(iDistance) + abs(jDistance)
        return manhattanDistance

    def calculateHeuristic(self, manhattanDistance):
        heuristic = 0
        # assuming Mario has both stars, only a max. of 12 squares would cost half as much.
        if (manhattanDistance > 12):
            heuristic = manhattanDistance - 6
        else:
            heuristic = manhattanDistance / 2
        return heuristic

    def compareState(self, father, marioPos, operator):  # True: The state changed
        fatherNode = father
        if (fatherNode.getOperator() != "first father"):
            if (operator == "right"):
                if (marioPos[1]+1 == fatherNode.getMarioPos()[1] and marioPos[0] == fatherNode.getMarioPos()[0]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        return True
                    else:
                        return False
                else:
                    return True
            if (operator == "left"):
                if (marioPos[1]-1 == fatherNode.getMarioPos()[1] and marioPos[0] == fatherNode.getMarioPos()[0]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        return True
                    else:
                        return False
                else:
                    return True
            if (operator == "down"):
                if (marioPos[0]+1 == fatherNode.getMarioPos()[0] and marioPos[1] == fatherNode.getMarioPos()[1]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        return True
                    else:
                        return False
                else:
                    return True
            if (operator == "up"):
                if (marioPos[0]-1 == fatherNode.getMarioPos()[0] and marioPos[1] == fatherNode.getMarioPos()[1]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        return True
                    else:
                        return False
                else:
                    return True
        return True

        """ def compareState(self, father, marioPos, operator):  # True: The state changed
        fatherNode = father
        if (self.getOperator() != "first father"):
            if (operator == "right"):
                if (marioPos[1]+1 == fatherNode.getMarioPos()[1] and marioPos[0] == fatherNode.getMarioPos()[0]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        return True
                    else:
                        return False
                else:
                    return True
            if (operator == "left"):
                if (marioPos[1]-1 == fatherNode.getMarioPos()[1] and marioPos[0] == fatherNode.getMarioPos()[0]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        return True
                    else:
                        return False
                else:
                    return True
            if (operator == "down"):
                if (marioPos[0]+1 == fatherNode.getMarioPos()[0] and marioPos[1] == fatherNode.getMarioPos()[1]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        return True
                    else:
                        return False
                else:
                    return True
            if (operator == "up"):
                if (marioPos[0]-1 == fatherNode.getMarioPos()[0] and marioPos[1] == fatherNode.getMarioPos()[1]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        return True
                    else:
                        return False
                else:
                    return True
return True"""

    # True: The state changed

    def rightMovement(self, marioPos):
        return [marioPos[0], marioPos[1] + 1 if marioPos[1] < 9 else False]

    def leftMovement(self, marioPos):
        return [marioPos[0], marioPos[1] - 1 if marioPos[1] > 0 else False]

    def upMovement(self, marioPos):
        return [marioPos[0] - 1 if marioPos[0] > 0 else False, marioPos[1]]

    def downMovement(self, marioPos):
        return [marioPos[0] + 1 if marioPos[0] < 9 else False, marioPos[1]]

    # True means that the node can expand their sons, false means it can't
    def compareCicles(self, operator, start1, start2, flower1, flower2):
        currentNode = self
        fatherNode = self.getFather()
        marioPos = self.getMarioPos()
        while fatherNode.getOperator() != "first father":
            if operator == "right":
                futureMarioPos = self.rightMovement(marioPos)
                if fatherNode.getMarioPos() == futureMarioPos:
                    if ((fatherNode.getStar() > 0 and currentNode.getStar() == 1) or (fatherNode.getFlower() > 0 and self.getFlower() == 1)
                            or (currentNode.getStar() == 0 and (futureMarioPos == start1 or futureMarioPos == start2)) or (currentNode.getFlower() == 0 and (futureMarioPos == flower1 or futureMarioPos == flower2))
                            or (currentNode.getStar() > 0 and fatherNode.getStar() == 0) or (currentNode.getFlower() > 0 and fatherNode.getFlower() == 0)):
                        fatherNode = fatherNode.getFather()
                    else:
                        return False
                else:
                    fatherNode = fatherNode.getFather()
            elif operator == "left":
                futureMarioPos = self.leftMovement(marioPos)
                if fatherNode.getMarioPos() == futureMarioPos:
                    if ((fatherNode.getStar() > 0 and currentNode.getStar() == 1) or (fatherNode.getFlower() > 0 and self.getFlower() == 1)
                            or (currentNode.getStar() == 0 and (futureMarioPos == start1 or futureMarioPos == start2)) or (currentNode.getFlower() == 0 and (futureMarioPos == flower1 or futureMarioPos == flower2))
                            or (currentNode.getStar() > 0 and fatherNode.getStar() == 0) or (currentNode.getFlower() > 0 and fatherNode.getFlower() == 0)):
                        fatherNode = fatherNode.getFather()
                    else:
                        return False
                else:
                    fatherNode = fatherNode.getFather()
            elif operator == "up":
                futureMarioPos = self.upMovement(marioPos)
                if fatherNode.getMarioPos() == futureMarioPos:
                    if ((fatherNode.getStar() > 0 and currentNode.getStar() == 1) or (fatherNode.getFlower() > 0 and self.getFlower() == 1)
                            or (currentNode.getStar() == 0 and (futureMarioPos == start1 or futureMarioPos == start2)) or (currentNode.getFlower() == 0 and (futureMarioPos == flower1 or futureMarioPos == flower2))
                            or (currentNode.getStar() > 0 and fatherNode.getStar() == 0) or (currentNode.getFlower() > 0 and fatherNode.getFlower() == 0)):
                        fatherNode = fatherNode.getFather()
                    else:
                        return False
                else:
                    fatherNode = fatherNode.getFather()
            elif operator == "down":
                futureMarioPos = self.downMovement(marioPos)
                if fatherNode.getMarioPos() == futureMarioPos:
                    if ((fatherNode.getStar() > 0 and currentNode.getStar() == 1) or (fatherNode.getFlower() > 0 and self.getFlower() == 1)
                            or (currentNode.getStar() == 0 and (futureMarioPos == start1 or futureMarioPos == start2)) or (currentNode.getFlower() == 0 and (futureMarioPos == flower1 or futureMarioPos == flower2))
                            or (currentNode.getStar() > 0 and fatherNode.getStar() == 0) or (currentNode.getFlower() > 0 and fatherNode.getFlower() == 0)):
                        fatherNode = fatherNode.getFather()
                    else:
                        return False
                else:
                    fatherNode = fatherNode.getFather()
        return True

    def avoidGoBack(self, operator, start1, start2, flower1, flower2):
        currentNode = self
        fatherNode = self.getFather()
        marioPos = self.getMarioPos()
        if fatherNode.getOperator() != "first father":
            if operator == "right":
                futureMarioPos = self.rightMovement(marioPos)
                if fatherNode.getMarioPos() == futureMarioPos:
                    if ((fatherNode.getStar() >= 0 and (futureMarioPos == start1 or futureMarioPos == start2))
                        or not (fatherNode.getStar() == 0 and currentNode.getStar()-1 <= 0)
                            or (fatherNode.getStar() > 0 and currentNode.getStar()-1 >= 1)
                            or (fatherNode.getStar() == 0 and currentNode.getStar() > 0) and
                            (fatherNode.getFlower() >= 0 and (
                                futureMarioPos == flower1 or futureMarioPos == flower2))
                        or not (fatherNode.getFlower() == 0 and currentNode.getFlower() == 0)
                            or (fatherNode.getFlower() > 0 and currentNode.getFlower() == 0)
                            or (fatherNode.getFlower() == 0 and currentNode.getFlower() > 0)):
                        return True
                    else:
                        return False

                    """ if ((fatherNode.getStar() > 0 and currentNode.getStar() == 1) or (fatherNode.getFlower() > 0 and self.getFlower() == 0)
                            or (currentNode.getStar() == 0 and (futureMarioPos == start1 or futureMarioPos == start2)) or (currentNode.getFlower() == 0 and (futureMarioPos == flower1 or futureMarioPos == flower2))
                            or (currentNode.getStar() > 0 and fatherNode.getStar() == 0) or (currentNode.getFlower() > 0 and fatherNode.getFlower() == 0)):
                        return True
                    else:
                        return False"""
                else:
                    return True
            elif operator == "left":
                futureMarioPos = self.leftMovement(marioPos)
                if fatherNode.getMarioPos() == futureMarioPos:
                    if ((fatherNode.getStar() >= 0 and (futureMarioPos == start1 or futureMarioPos == start2))
                        or not (fatherNode.getStar() == 0 and currentNode.getStar()-1 <= 0)
                            or (fatherNode.getStar() > 0 and currentNode.getStar()-1 >= 1)
                            or (fatherNode.getStar() == 0 and currentNode.getStar() > 0) and
                            (fatherNode.getFlower() >= 0 and (
                                futureMarioPos == flower1 or futureMarioPos == flower2))
                        or not (fatherNode.getFlower() == 0 and currentNode.getFlower() == 0)
                            or (fatherNode.getFlower() > 0 and currentNode.getFlower() == 0)
                            or (fatherNode.getFlower() == 0 and currentNode.getFlower() > 0)):
                        return True
                    else:
                        return False
                    """ if ((fatherNode.getStar() > 0 and currentNode.getStar() == 1) or (fatherNode.getFlower() > 0 and self.getFlower() == 1)
                            or (currentNode.getStar() == 0 and (futureMarioPos == start1 or futureMarioPos == start2)) or (currentNode.getFlower() == 0 and (futureMarioPos == flower1 or futureMarioPos == flower2))
                            or (currentNode.getStar() > 0 and fatherNode.getStar() == 0) or (currentNode.getFlower() > 0 and fatherNode.getFlower() == 0)):
                        return True
                    else:
                        return False"""
                else:
                    return True
            elif operator == "up":
                futureMarioPos = self.upMovement(marioPos)
                if fatherNode.getMarioPos() == futureMarioPos:
                    if (((fatherNode.getStar() >= 0 and (futureMarioPos == start1 or futureMarioPos == start2))
                        or not (fatherNode.getStar() == 0 and currentNode.getStar()-1 <= 0)
                            or (fatherNode.getStar() > 0 and currentNode.getStar()-1 >= 1)
                            or (fatherNode.getStar() == 0 and currentNode.getStar() > 0)) or
                            (fatherNode.getFlower() >= 0 and (
                                futureMarioPos == flower1 or futureMarioPos == flower2))
                       # review
                        or not (fatherNode.getFlower() == 0 and currentNode.getFlower() == 0)
                            or (fatherNode.getFlower() > 0 and currentNode.getFlower() == 0)
                            or (fatherNode.getFlower() == 0 and currentNode.getFlower() > 0)):
                        print("up flower", fatherNode.getFlower(), currentNode.getFlower(
                        ), futureMarioPos, flower1, flower2)
                        print("up star", fatherNode.getStar(
                        ), currentNode.getStar(), futureMarioPos, start1, start2)
                        return True
                    else:
                        return False
                    """if ((fatherNode.getStar() > 0 and currentNode.getStar() == 1) or (fatherNode.getFlower() > 0 and self.getFlower() == 1)
                            or (currentNode.getStar() == 0 and (futureMarioPos == start1 or futureMarioPos == start2)) or (currentNode.getFlower() == 0 and (futureMarioPos == flower1 or futureMarioPos == flower2))
                            or (currentNode.getStar() > 0 and fatherNode.getStar() == 0) or (currentNode.getFlower() > 0 and fatherNode.getFlower() == 0)):
                        return True
                    else:
                        return False"""
                else:
                    return True
            elif operator == "down":
                futureMarioPos = self.downMovement(marioPos)
                if fatherNode.getMarioPos() == futureMarioPos:
                    if ((fatherNode.getStar() >= 0 and (futureMarioPos == start1 or futureMarioPos == start2))
                        or not (fatherNode.getStar() == 0 and currentNode.getStar()-1 <= 0)
                            or (fatherNode.getStar() > 0 and currentNode.getStar()-1 >= 1)
                            or (fatherNode.getStar() == 0 and currentNode.getStar() > 0) and
                            (fatherNode.getFlower() >= 0 and (
                                futureMarioPos == flower1 or futureMarioPos == flower2))
                        or not (fatherNode.getFlower() == 0 and currentNode.getFlower() == 0)
                            or (fatherNode.getFlower() > 0 and currentNode.getFlower() == 0)
                            or (fatherNode.getFlower() == 0 and currentNode.getFlower() > 0)):
                        print("down flower", fatherNode.getFlower(), currentNode.getFlower(
                        ), futureMarioPos, flower1, flower2)
                        print("down star", fatherNode.getStar(
                        ), currentNode.getStar(), futureMarioPos, start1, start2)
                        return True
                    else:
                        return False
                    """if ((fatherNode.getStar() > 0 and currentNode.getStar() == 1) or (fatherNode.getFlower() > 0 and self.getFlower() == 1)
                            or (currentNode.getStar() == 0 and (futureMarioPos == start1 or futureMarioPos == start2)) or (currentNode.getFlower() == 0 and (futureMarioPos == flower1 or futureMarioPos == flower2))
                            or (currentNode.getStar() > 0 and fatherNode.getStar() == 0) or (currentNode.getFlower() > 0 and fatherNode.getFlower() == 0)):
                        return True
                    else:
                        return False"""
                else:
                    return True
        return True

    def avoidGoBack2(self, operator, start1, start2, flower1, flower2):
        currentNode = self
        fatherNode = self.getFather()
        grandFatherNode = fatherNode.getFather()
        marioPos = self.getMarioPos()
        currentNodePosition = currentNode.searchForMario()
        if grandFatherNode.getOperator() != "first father":
            if (grandFatherNode.getMarioPos() == currentNodePosition):
                print("flowercant", grandFatherNode.getFlower(),
                      currentNode.getFlower())
                if (grandFatherNode.getStar() != currentNode.getStar() or grandFatherNode.getFlower() != currentNode.getFlower() or (fatherNode.getFlower() == 1 and currentNode.getFlower() == 0)):
                    print("flowercantIf", grandFatherNode.getFlower(),
                          currentNode.getFlower())
                    return True
                else:
                    return False
        return True

    def compareCicles2(self, operator, start1, start2, flower1, flower2):
        currentNode = self
        fatherNode = self.getFather()
        grandFatherNode = fatherNode.getFather()
        marioPos = self.getMarioPos()
        currentNodePosition = currentNode.searchForMario()
        while grandFatherNode.getOperator() != "first father":
            print("father", grandFatherNode.getMarioPos(),
                  "mia", currentNodePosition)
            if (grandFatherNode.getMarioPos() == currentNodePosition):
                print("flowercant", grandFatherNode.getFlower(),
                      currentNode.getFlower())
                if (grandFatherNode.getStar() != currentNode.getStar() or grandFatherNode.getFlower() != currentNode.getFlower() or (fatherNode.getFlower() == 1 and currentNode.getFlower() == 0)):
                    print("flowercantIf", grandFatherNode.getFlower(),
                          currentNode.getFlower())
                    grandFatherNode = grandFatherNode.getFather()
                else:
                    return False
            else:
                grandFatherNode = grandFatherNode.getFather()
        return True

    def moveRight(self, posMario):
        i = posMario[0]
        j = posMario[1]
        self.__state[i, j] = self.getFather().getAwaitingCharacter()
        # print("[ " + str(i) + " ] [ " + str(j + 1) + " ]") if i == 6 else 0
        self.takeDecision([i, j+1])
        return self

    def moveLeft(self, posMario):
        i = posMario[0]
        j = posMario[1]
        self.__state[i, j] = self.getFather().getAwaitingCharacter()
        self.takeDecision([i, j-1])
        return self

    def moveDown(self, posMario):
        i = posMario[0]
        j = posMario[1]
        self.__state[i, j] = self.getFather().getAwaitingCharacter()
        self.takeDecision([i+1, j])
        return self

    def moveUp(self, posMario):
        i = posMario[0]
        j = posMario[1]
        self.__state[i, j] = self.getFather().getAwaitingCharacter()
        self.takeDecision([i-1, j])
        return self

    def setNewCost(self, pos):
        i = pos[0]
        j = pos[1]
        state = self.getState()
        currentCost = self.getCost()  # Current cost is the one from the father
        # If the position where Mario will move into has a Koopa inside then:
        if state[i, j] == self.KOOPA:
            if self.getStar() > 0:  # If true, Koopa will not affect Mario
                self.setCost(currentCost + 0.5)
            elif self.getFlower() > 0:  # If true, Mario can use the flower to kill Koopa
                self.setCost(currentCost + 1)
            else:  # If all of the cases above did not meet, Mario is affected by Koopa
                self.setCost(currentCost + 6)
        elif state[i, j] == self.FLOWER:
            if self.getStar() > 0:
                self.setCost(currentCost + 0.5)
            else:
                self.setCost(currentCost + 1)
        # If it is not a Koopa, I still need to check whether Mario has a star or not,
        # if so Mario needs 0.5 of effort to move across the grid
        else:
            if self.getStar() > 0:
                self.setCost(currentCost + 0.5)
            else:
                self.setCost(currentCost + 1)

    # pos is the future position of Mario
    def takeDecision(self, pos):
        i = pos[0]
        j = pos[1]
        # print("Pos: " + str(i) + " and " + str(j))
        # self.setNewCost(pos)
        if self.__state[i, j] == self.PRINCESS:
            self.setAwaitingCharacter(self.EMPTY)
            self.setStar(self.getStar() - 1 if self.getStar() > 0 else 0)
            self.__state[i, j] = self.RESCUED_PRINCESS
        elif self.__state[i, j] == self.KOOPA:
            if self.getFlower() > 0 or self.getStar() > 0:
                self.setAwaitingCharacter(self.EMPTY)
                self.setFlower(self.getFlower() -
                               1 if self.getFlower() > 0 else 0)
                self.setStar(self.getStar() - 1 if self.getStar() > 0 else 0)
            else:
                self.setAwaitingCharacter(self.KOOPA)
        elif self.__state[i, j] == self.FLOWER:
            if self.getStar() == 0:  # Mario can get the flower
                self.setFlower(self.getFlower() + 1)
                print("cantidad flowers", self.getFlower())
                self.setAwaitingCharacter(self.EMPTY)
            else:
                self.setStar(self.getStar() - 1 if self.getStar() > 0 else 0)
                self.setAwaitingCharacter(self.FLOWER)
        elif self.__state[i, j] == self.STAR:
            if self.getFlower() == 0:  # Mario can get the star
                self.setStar(self.getStar() - 1 if self.getStar() > 0 else 0)
                self.setStar(self.getStar() + 6)
                self.setAwaitingCharacter(self.EMPTY)
            else:
                self.setAwaitingCharacter(self.STAR)
        else:
            self.setStar(self.getStar() - 1 if self.getStar() > 0 else 0)
            self.setAwaitingCharacter(self.EMPTY)

        if self.__state[i, j] != self.RESCUED_PRINCESS:
            self.__state[i, j] = self.MARIO

        # print("DESPUÉS DE TAKE DECISION: " + str(i) + " " + str(j))
        # print("Estado después de rake decision:")
        # print(self.getState())

    def showDepth(self):
        print("The node's depth is: " + str(self.__depth))

    def showOperator(self):
        print("The operator used to get to this node was: " + self.__operator)

    def recreateSolution(self):
        directions = []
        currentNode = self
        while currentNode.getOperator() != "first father":
            directions.append(
                str(currentNode.getOperator() + " " + str(currentNode.getCost()) + " Star: " + str(currentNode.getStar())))
            currentNode = currentNode.getFather()
        return directions

    def recreateSolutionWorld(self):
        directions = []
        currentNode = self
        while currentNode.getOperator() != "first father":
            directions.append(currentNode.getState())
            currentNode = currentNode.getFather()
        return directions

    def searchForMario(self):
        marioPos = [-1, -1]  # Mario position [x,y]
        state = self.__state
        for i in range(10):
            for j in range(10):
                if (state[i, j] == self.MARIO):
                    marioPos[0] = i
                    marioPos[1] = j

        self.setMarioPos(marioPos)
        # print("DESPUES DE SEARCH FOR MARIO: " +
        #      str(marioPos[0]) + " " + str(marioPos[1]))
        return marioPos

    def searchForMario(self):
        marioPos = [-1, -1]  # Mario position [x,y]
        state = self.__state
        for i in range(10):
            for j in range(10):
                if (state[i, j] == self.MARIO):
                    marioPos[0] = i
                    marioPos[1] = j

        self.setMarioPos(marioPos)
        # print("DESPUES DE SEARCH FOR MARIO: " +
        #      str(marioPos[0]) + " " + str(marioPos[1]))
        return marioPos

    def searchForStart(self):
        start1 = [-2, -2]  # Mario position [x,y]
        start2 = [-2, -2]
        cont = 0
        state = self.__state
        for i in range(10):
            for j in range(10):
                if (state[i, j] == self.STAR and cont == 0):
                    start1[0] = i
                    start1[1] = j
                    cont += 1
                elif (state[i, j] == self.STAR and cont == 1):
                    start2[0] = i
                    start2[1] = j
        return [start1, start2]

    def searchForFlower(self):
        flower1 = [-2, -2]  # Mario position [x,y]
        flower2 = [-2, -2]
        cont = 0
        state = self.__state
        for i in range(10):
            for j in range(10):
                if (state[i, j] == self.FLOWER and cont == 0):
                    flower1[0] = i
                    flower1[1] = j
                    cont += 1
                elif (state[i, j] == self.FLOWER and cont == 1):
                    flower2[0] = i
                    flower2[1] = j
        return [flower1, flower2]

    def isGoal(self):
        state = self.__state
        for i in range(10):
            for j in range(10):
                if (state[i, j] == self.RESCUED_PRINCESS):
                    return True
        return False
