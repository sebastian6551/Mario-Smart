class Node:

    EMPTY = 0
    BLOCK = 1
    MARIO = 2
    STAR = 3
    KOOPA = 5
    FLOWER = 4

    def __init__(self, state, father, operator, depth, cost):
        self.__state = state
        self.__father = father
        self.__operator = operator
        self.__depth = depth
        self.__cost = cost
        self.__marioPos = []

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

    def getState(self):
        return self.__state.copy()

    def moveRight(self, posMario):
        self.__state[posMario[0], posMario[1]] = 0
        self.__state[posMario[0], posMario[1]+1] = 2
        return self

    def moveLeft(self, posMario):
        self.__state[posMario[0], posMario[1]] = 0
        self.__state[posMario[0], posMario[1]-1] = 2
        return self

    def moveDown(self, posMario):
        self.__state[posMario[0], posMario[1]] = 0
        self.__state[posMario[0]+1, posMario[1]] = 2
        return self

    def moveUp(self, posMario):
        self.__state[posMario[0], posMario[1]] = 0
        self.__state[posMario[0]-1, posMario[1]] = 2
        return self

    def showDepth(self):
        print("The node's depth is: " + str(self.profundidad))

    def showOperator(self):
        print("The operator used to get to this node was: " + self.operador)

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
        if (j+1 < 9):
            if (self.__state[i, j+1] == 6):
                return True
        if (i-1 > 0):
            if (self.__state[i-1, j] == 6):
                return True
        if (i+1 < 9):
            if (self.__state[i+1, j] == 6):
                return True
        if (j-1 > 0):
            if (self.__state[i, j-1] == 6):
                return True
            # if(self.state[i,j+1]==6 or self.state[i-1,j]==6 or self.state[i+1,j]==6 or self.state[i,j-1]==6):
            #    return True
        else:
            return False
