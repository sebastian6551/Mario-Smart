class Node:

    EMPTY = 0
    BLOCK = 1
    MARIO = 2
    STAR = 3
    KOOPA = 5
    FLOWER = 4

    def __init__(self, state, father, operator, depth, cost, star, flower):
        self.__state = state
        self.__father = father
        self.__operator = operator
        self.__depth = depth
        self.__cost = cost
        self.__star = star  # It lasts 6 grids - cost 1/2 and they accumulate
        self.__flower = flower  # Cost to go through a koopa when having a flower comes down to 1
        self.__marioPos = []
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

    def setMarioPos(self, newMarioPos):
        self.__marioPos = newMarioPos

    def setStar(self, newStarValue):
        self.__star = newStarValue

    def setFlower(self, newFlowerValue):
        self.__flower = newFlowerValue

    def setAwaitingCharacter(self, awaitingCharacter):
        self.__awaitingCharacter = awaitingCharacter

    def compareState(self, father, marioPos, operator):  # True: The state changed
        fatherNode = father
        if (father.getOperator() != "first father"):
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

    # True: The state changed

    def compareFatherAll(self, marioPos, marioPos0, operator):
        if (operator == "right"):
            if (marioPos[1]+1 == marioPos0[1] and marioPos[0] == marioPos[0]):
                if (self.getStar() > 0 or self.getFlower() > 0):
                    return True
                else:
                    return False
            else:
                return True
        if (operator == "left"):
            if (marioPos[1]-1 == marioPos0[1] and marioPos[0] == marioPos0[0]):
                if (self.getStar() > 0 or self.getFlower() > 0):
                    return True
                else:
                    return False
            else:
                return True
        if (operator == "down"):
            if (marioPos[0]+1 == marioPos0[0] and marioPos[1] == marioPos0[1]):
                if (self.getStar() > 0 or self.getFlower() > 0):
                    return True
                else:
                    return False
            else:
                return True
        if (operator == "up"):
            if (marioPos[0]-1 == marioPos0[0] and marioPos[1] == marioPos0[1]):
                if (self.getStar() > 0 or self.getFlower() > 0):
                    return True
                else:
                    return False
            else:
                return True

    def compareStateCicle(self, father, marioPos, operator):
        currentNode = self
        fatherNode = father
        while (fatherNode.getOperator() != "first father"):
            if (operator == "right"):
                if (marioPos[1]+1 == fatherNode.searchForMario()[1] and marioPos[0] == fatherNode.searchForMario()[0]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        currentNode = currentNode.getFather()
                        fatherNode = fatherNode.getFather()
                    else:
                        return False
                else:
                    currentNode = currentNode.getFather()
                    fatherNode = fatherNode.getFather()
            if (operator == "left"):
                if (marioPos[1]-1 == fatherNode.searchForMario()[1] and marioPos[0] == fatherNode.searchForMario()[0]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        currentNode = currentNode.getFather()
                        fatherNode = fatherNode.getFather()
                    else:
                        return False
                else:
                    currentNode = currentNode.getFather()
                    fatherNode = fatherNode.getFather()
            if (operator == "down"):
                if (marioPos[0]+1 == fatherNode.searchForMario()[0] and marioPos[1] == fatherNode.searchForMario()[1]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        currentNode = currentNode.getFather()
                        fatherNode = fatherNode.getFather()
                    else:
                        return False
                else:
                    currentNode = currentNode.getFather()
                    fatherNode = fatherNode.getFather()
            if (operator == "up"):
                if (marioPos[0]-1 == fatherNode.searchForMario()[0] and marioPos[1] == fatherNode.searchForMario()[1]):
                    if ((fatherNode.getStar() > 0 and self.getStar() <= 0) or (fatherNode.getFlower() > 0 and self.getFlower() <= 0)):
                        currentNode = currentNode.getFather()
                        fatherNode = fatherNode.getFather()
                    else:
                        return False
                else:
                    currentNode = currentNode.getFather()
                    fatherNode = fatherNode.getFather()
        return True

    def moveRight(self, posMario):
        i = posMario[0]
        j = posMario[1]
        self.__state[i, j] = self.getFather().getAwaitingCharacter()
        # print("[ " + str(i) + " ] [ " + str(j + 1) + " ]") if i == 6 else 0
        self.takeDecision([i, j+1])
        self.__state[i, j+1] = self.MARIO
        return self

    def moveLeft(self, posMario):
        i = posMario[0]
        j = posMario[1]
        self.__state[i, j] = self.getFather().getAwaitingCharacter()
        self.takeDecision([i, j-1])
        self.__state[i, j-1] = self.MARIO
        return self

    def moveDown(self, posMario):
        i = posMario[0]
        j = posMario[1]
        self.__state[i, j] = self.getFather().getAwaitingCharacter()
        self.takeDecision([i+1, j])
        self.__state[i+1, j] = self.MARIO
        return self

    def moveUp(self, posMario):
        i = posMario[0]
        j = posMario[1]
        self.__state[i, j] = self.getFather().getAwaitingCharacter()
        self.takeDecision([i-1, j])
        self.__state[i-1, j] = self.MARIO
        return self

    # pos is the future position of Mario
    def takeDecision(self, pos):
        i = pos[0]
        j = pos[1]
        if self.__state[i, j] == self.KOOPA:
            if self.getFlower() > 0 or self.getStar() > 0:
                self.getFather().setAwaitingCharacter(self.EMPTY)
                self.setFlower(self.getFlower() -
                               1 if self.getFlower() > 0 else 0)
                self.setStar(self.getStar() - 1 if self.getStar() > 0 else 0)
            else:
                self.setAwaitingCharacter(self.KOOPA)
        elif self.__state[i, j] == self.FLOWER:
            if self.getStar() == 0:  # Mario can get the flower
                self.setFlower(self.getFlower() + 1)
            else:
                self.setAwaitingCharacter(self.FLOWER)
        elif self.__state[i, j] == self.STAR:
            if self.getFlower() == 0:  # Mario can get the star
                self.setStar(self.getStar() + 6)
            else:
                self.setAwaitingCharacter(self.STAR)
        else:
            self.setStar(self.getStar() - 1 if self.getStar() > 0 else 0)
            self.setAwaitingCharacter(self.EMPTY)

    def showDepth(self):
        print("The node's depth is: " + str(self.__depth))

    def showOperator(self):
        print("The operator used to get to this node was: " + self.__operator)

    def recreateSolution(self):
        directions = []
        currentNode = self
        while currentNode.getOperator() != "first father":
            directions.append(str(currentNode.getOperator(
            )) + " " + str(currentNode.getFlower()) + " " + str(currentNode.getStar()))
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
        marioPos = []  # Mario position [x,y]
        arr3 = self.__state
        for i in range(10):
            for j in range(10):
                if (arr3[i, j] == 2):
                    marioPos.append(i)
                    marioPos.append(j)
        self.setMarioPos(marioPos)
        return marioPos

    def isGoal(self, i, j):
        if (j+1 <= 9):
            if (self.__state[i, j+1] == 6):
                return True
        if (i-1 >= 0):
            if (self.__state[i-1, j] == 6):
                return True
        if (i+1 <= 9):
            if (self.__state[i+1, j] == 6):
                return True
        if (j-1 >= 0):
            if (self.__state[i, j-1] == 6):
                return True
            # if(self.state[i,j+1]==6 or self.state[i-1,j]==6 or self.state[i+1,j]==6 or self.state[i,j-1]==6):
            #    return True
        else:
            return False
