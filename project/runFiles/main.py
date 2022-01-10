from project.cubePieces import Cube
import json

if __name__ == '__main__':
    cube2 = Cube.Cube()

    cube2.rotation('U')
    print(cube2)

    # for key in cube2.rotations:
    #     cube2.rotation(key)
    #     print(cube2.toJson())
    #
    #     with open(f'../CubeTest/Helpers/Json/{key}.json', 'w') as data:
    #         # json.dump(cube2.toJson(), data, indent=2, separators=(",",':'))
    #         data.write(str(cube2.toJson()).replace("'",'"').replace('], "','],\n  "').replace("[[","[\n    [").replace(", [",",\n    [").replace('{"','{\n  "').replace("]]","]\n  ]").replace("]}","]\n}"))
