import math

from project.cubePieces import Cube
import json
from project.cubeFixer.CubeSolver import CubeSolver


if __name__ == '__main__':
    cube =  Cube.Cube()

    cube.rotation("B")
    cube.rotation("S'")

    with open('../CubeTest/Helpers/Json/small_b.json', 'w') as data:
     #json.dump(cube2.toJson(), data, indent=2, separators=(",",':'))
        data.write(str(cube.toJson()).replace("'", '"').replace('], "', '],\n  "').replace("[[", "[\n    [").replace(", [", ",\n    [").replace('{"', '{\n  "').replace("]]", "]\n  ]").replace("]}", "]\n}"))