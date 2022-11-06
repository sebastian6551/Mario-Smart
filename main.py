import numpy as np
from algorithms.depthAlgorithm import DepthAlgorithm
from algorithms.amplitudeAlgorithm import AmplitudeAlgorithm
from algorithms.costAlgorithm import CostAlgorithm
from interface import Interface

with open('matriz.txt', 'r') as f:
    board_txt = ''.join(f.readlines()).replace('\n', ';')

world = np.matrix(board_txt)


"""
CHOSEN_ALGORITHM = 6
algorithm = None
title = ""

if CHOSEN_ALGORITHM == 0:
    algorithm = AmplitudeAlgorithm(world)
    tittle = "Mario smart amplitud"
elif CHOSEN_ALGORITHM == 1:
    algorithm = DepthAlgorithm(world)
    tittle = "Mario smart profundidad"
elif CHOSEN_ALGORITHM == 2:
    algorithm = CostAlgorithm(world)
    tittle = "Mario smart costo"

solutionWorld = algorithm.start()
interface = Interface(solutionWorld)
interface.showInterface(tittle)"""

interface = Interface(world)
interface.showInterface()
