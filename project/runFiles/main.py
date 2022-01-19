
from project.cubePieces import Cube
import json
from project.cubeFixer.cubeSolver import CubeSolver


if __name__ == '__main__':

    solve = CubeSolver(Cube.Cube())
    solve.cube.rotation('F')
    solve.cube.rotation('B')
    solve.cube.rotation('U')

    solve.findWhiteCross()
    print(solve.cube)
    print(solve.combination)
