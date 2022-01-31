import math

from project.cubePieces import Cube
import json
from project.cubeFixer.CubeSolver import CubeSolver


if __name__ == '__main__':
    cube = Cube.Cube()

    cube.rotation('R')
    cube.rotation('L')
    cube.moreThenOneSideRotation('u')
    cube.rotation('R')

    solve = CubeSolver(cube)
    solve.findWhiteCross()
