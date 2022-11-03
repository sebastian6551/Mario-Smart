import numpy as np
from algorithms.depthAlgorithm import DepthAlgorithm
from algorithms.amplitudeAlgorithm import AmplitudeAlgorithm
from interface import Interface

with open('matriz.txt', 'r') as f:
    board_txt = ''.join(f.readlines()).replace('\n', ';')

world = np.matrix(board_txt)

CHOSEN_ALGORITHM = 1
algorithm = None

if CHOSEN_ALGORITHM == 0:
    algorithm = AmplitudeAlgorithm(world)
elif CHOSEN_ALGORITHM == 1:
    algorithm = DepthAlgorithm(world)

solutionWorld = algorithm.start()
interface = Interface(solutionWorld)

interface.showInterface()
