import json


from project.cubePieces.Tiles import middleTile, borderTile, cornerTile


class Cube:
    # Blocks numbers are front left to right, up to bottom, front to back
    rotations = {
        'F': [[0, 2, 6, 8, 6, 0, 8, 2], [1, 3, 5, 7, 3, 7, 1, 5], '1'],
        "F'": [[0, 2, 6, 8, 2, 8, 0, 6], [1, 3, 5, 7, 5, 1, 7, 3], '1'],
        "U": [[0, 2, 18, 20, 2, 20, 0, 18], [1, 9, 11, 19, 11, 1, 19, 9], '2'],
        "U'": [[0, 2, 18, 20, 18, 0, 20, 2], [1, 9, 11, 19, 11, 19, 1, 9], '2'],
        "D": [[6, 8, 24, 26, 24, 6, 26, 8], [7, 15, 17, 25, 15, 25, 7, 17], '2'],
        "D'": [[6, 8, 24, 26, 8, 26, 6, 24], [7, 15, 17, 25, 17, 7, 25, 15], '2'],
        "R": [[2, 8, 20, 26, 8, 26, 2, 20], [5, 11, 17, 23, 17, 5, 23, 11], '3'],
        "R'": [[2, 8, 20, 26, 20, 2, 26, 8], [5, 11, 17, 23, 11, 23, 5, 17], '3'],
        "L": [[0, 6, 18, 24, 18, 0, 24, 6], [3, 9, 15, 21, 9, 21, 3, 15], '3'],
        "L'": [[0, 6, 18, 24, 6, 24, 18, 0], [3, 9, 15, 21, 15, 3, 9, 21], '3'],
        "B": [[18, 20, 24, 26, 20, 26, 18, 24], [19, 21, 23, 25, 23, 19, 25, 21], '1'],
        "B'": [[18, 20, 24, 26, 24, 18, 26, 20], [19, 21, 23, 25, 21, 25, 19, 23], '1'],
        "M": [[1, 7, 19, 25, 19, 1, 25, 7], [4, 10, 16, 22, 10, 22, 4, 16], []],
        "M'": [[1, 7, 19, 25, 7, 25, 1, 19], [4, 10, 16, 22, 16, 4, 22, 10], []],
        "E": [[3, 5, 15, 17, 15, 3, 17, 5], [4, 12, 14, 16, 12, 16, 4, 14], []],
        "E'": [[3, 5, 21, 23, 5, 23, 3, 21], [4, 12, 14, 22, 14, 4, 22, 12], []],
        "S": [[9, 11, 15, 17, 15, 9, 17, 11], [10, 12, 14, 16, 12, 16, 10, 14], []],
        "S'": [[9, 11, 15, 17, 11, 17, 9, 15], [10, 12, 14, 16, 14, 10, 16, 12], []],
    }

    def __str__(self):
        frontSide = 'Front side:\n'
        frontSide += f"['{self.tiles[0].thirdColor}', '{self.tiles[1].firstColor}', '" \
                     f"{self.tiles[2].thirdColor}'],\n['{self.tiles[3].secondColor}', " \
                     f"'{self.tiles[4].color}', '{self.tiles[5].secondColor}'],\n['" \
                     f"{self.tiles[6].thirdColor}', '{self.tiles[7].firstColor}', '" \
                     f"{self.tiles[8].thirdColor}']"

        backSide = 'Back side:\n'
        backSide += f"['{self.tiles[20].thirdColor}', '{self.tiles[19].firstColor}', '" \
                     f"{self.tiles[18].thirdColor}'],\n['{self.tiles[23].secondColor}', " \
                     f"'{self.tiles[22].color}', '{self.tiles[21].secondColor}'],\n['" \
                     f"{self.tiles[26].thirdColor}', '{self.tiles[25].firstColor}', '" \
                     f"{self.tiles[24].thirdColor}']"

        upSide = 'Up side:\n'
        upSide += f"['{self.tiles[18].firstColor}', '{self.tiles[19].secondColor}', '" \
                     f"{self.tiles[20].firstColor}'],\n['{self.tiles[9].firstColor}', " \
                     f"'{self.tiles[10].color}', '{self.tiles[11].firstColor}'],\n['" \
                     f"{self.tiles[0].firstColor}', '{self.tiles[1].secondColor}', '" \
                     f"{self.tiles[2].firstColor}']"

        bottomSide = 'Bottom side:\n'
        bottomSide += f"['{self.tiles[6].firstColor}', '{self.tiles[7].secondColor}', '" \
                  f"{self.tiles[8].firstColor}'],\n['{self.tiles[15].firstColor}', " \
                  f"'{self.tiles[16].color}', '{self.tiles[17].firstColor}'],\n['" \
                  f"{self.tiles[24].firstColor}', '{self.tiles[25].secondColor}', '" \
                  f"{self.tiles[26].firstColor}']"

        leftSide = 'Left side:\n'
        leftSide += f"['{self.tiles[18].secondColor}', '{self.tiles[9].secondColor}', '" \
                     f"{self.tiles[0].secondColor}'],\n['{self.tiles[21].firstColor}', " \
                     f"'{self.tiles[12].color}', '{self.tiles[3].firstColor}'],\n['" \
                     f"{self.tiles[24].secondColor}', '{self.tiles[15].secondColor}', '" \
                     f"{self.tiles[6].secondColor}']"

        rightSide = 'Right side:\n'
        rightSide += f"['{self.tiles[2].secondColor}', '{self.tiles[11].secondColor}', '" \
                    f"{self.tiles[20].secondColor}'],\n['{self.tiles[5].firstColor}', " \
                    f"'{self.tiles[14].color}', '{self.tiles[23].firstColor}'],\n['" \
                    f"{self.tiles[8].secondColor}', '{self.tiles[17].secondColor}', '" \
                    f"{self.tiles[26].secondColor}']"

        return "\n".join([frontSide, upSide, leftSide, rightSide, bottomSide, backSide])


    def __init__(self, tiles: list = (), path: str = ''):
        """Enter list of cubes"""
        if len(tiles) == 27:
            self.tiles = tiles
        elif len(path) != 0:
            self.fromJson(path)
        else:
            self.setDefault()


    def fromJson(self, jsonFile: str):
        """Takes path to json file and makes cube from it"""
        with open(f"{jsonFile}", 'r') as file:
            data = json.load(file)

            frontArrays = data.get('front')
            backArrays = data.get('back')
            upArrays = data.get('up')
            bottomArrays = data.get('bottom')
            rightArrays = data.get('right')
            leftArrays = data.get('left')

        self.tiles = [
            cornerTile(upArrays[2][0], leftArrays[0][2], frontArrays[0][0]),
            borderTile(frontArrays[0][1], upArrays[2][1]),
            cornerTile(upArrays[2][2], rightArrays[0][0], frontArrays[0][2]),
            borderTile(leftArrays[1][2], frontArrays[1][0]),
            middleTile(frontArrays[1][1]),
            borderTile(rightArrays[1][0], frontArrays[1][2]),
            cornerTile(bottomArrays[0][0], leftArrays[2][2], frontArrays[2][0]),
            borderTile(frontArrays[2][1], bottomArrays[0][1]),
            cornerTile(bottomArrays[0][2], rightArrays[2][0], frontArrays[2][2]),
            borderTile(upArrays[1][0], leftArrays[0][1]),
            middleTile(upArrays[1][1]),
            borderTile(upArrays[1][2], rightArrays[0][1]),
            middleTile(leftArrays[1][1]),
            None,
            middleTile(rightArrays[1][1]),
            borderTile(bottomArrays[1][0], leftArrays[2][1]),
            middleTile(bottomArrays[1][1]),
            borderTile(bottomArrays[1][2], rightArrays[2][1]),
            cornerTile(upArrays[0][0], leftArrays[0][0], backArrays[0][2]),
            borderTile(backArrays[0][1], upArrays[0][1]),
            cornerTile(upArrays[0][2], rightArrays[0][2], backArrays[0][0]),
            borderTile(leftArrays[1][0], backArrays[1][2]),
            middleTile(backArrays[1][1]),
            borderTile(rightArrays[1][2], backArrays[1][0]),
            cornerTile(bottomArrays[2][0], leftArrays[2][0], backArrays[2][2]),
            borderTile(backArrays[2][1], bottomArrays[2][1]),
            cornerTile(bottomArrays[2][2], rightArrays[2][2], backArrays[2][0])
        , ]

    def toJson(self):
        """Returns object with each side colors"""
        frontSide = [[f"{self.tiles[0].thirdColor}", f"{self.tiles[1].firstColor}",
                     f"{self.tiles[2].thirdColor}"],[f"{self.tiles[3].secondColor}",
                     f"{self.tiles[4].color}", f"{self.tiles[5].secondColor}"],
                    [f"{self.tiles[6].thirdColor}", f"{self.tiles[7].firstColor}",
                     f"{self.tiles[8].thirdColor}"]]
        
        backSide = [[f"{self.tiles[20].thirdColor}", f"{self.tiles[19].firstColor}",
                    f"{self.tiles[18].thirdColor}"], [f"{self.tiles[23].secondColor}",
                    f"{self.tiles[22].color}", f"{self.tiles[21].secondColor}"],
                    [f"{self.tiles[26].thirdColor}", f"{self.tiles[25].firstColor}",
                    f"{self.tiles[24].thirdColor}"]]

        upSide = [[f"{self.tiles[18].firstColor}", f"{self.tiles[19].secondColor}",
                  f"{self.tiles[20].firstColor}"],[f"{self.tiles[9].firstColor}",
                  f"{self.tiles[10].color}", f"{self.tiles[11].firstColor}"],
                  [f"{self.tiles[0].firstColor}", f"{self.tiles[1].secondColor}",
                  f"{self.tiles[2].firstColor}"]]

        bottomSide = [[f"{self.tiles[6].firstColor}", f"{self.tiles[7].secondColor}",
                      f"{self.tiles[8].firstColor}"],[f"{self.tiles[15].firstColor}",
                      f"{self.tiles[16].color}", f"{self.tiles[17].firstColor}"],
                      [f"{self.tiles[24].firstColor}", f"{self.tiles[25].secondColor}",
                      f"{self.tiles[26].firstColor}"]]

        leftSide = [[f"{self.tiles[18].secondColor}", f"{self.tiles[9].secondColor}",
                    f"{self.tiles[0].secondColor}"], [f"{self.tiles[21].firstColor}",
                    f"{self.tiles[12].color}", f"{self.tiles[3].firstColor}"],
                    [f"{self.tiles[24].secondColor}", f"{self.tiles[15].secondColor}",
                    f"{self.tiles[6].secondColor}"]]

        rightSide = [[f"{self.tiles[2].secondColor}", f"{self.tiles[11].secondColor}",
                     f"{self.tiles[20].secondColor}"],[f"{self.tiles[5].firstColor}",
                     f"{self.tiles[14].color}", f"{self.tiles[23].firstColor}"],
                     [f"{self.tiles[8].secondColor}", f"{self.tiles[17].secondColor}",
                     f"{self.tiles[26].secondColor}"]]

        cube = {
            "front": frontSide,
            "back": backSide,
            "right": rightSide,
            "left": leftSide,
            "up": upSide,
            "bottom": bottomSide
        }

        return cube

    def setDefault(self):
        self.fromJson('project/basicJsons/normalSet.json')


    def rotation(self, rotationType: str):
        """Rotation type from Cube.rotations"""
        cornerNumbers, borderNumbers, cornerRotations = Cube.rotations.get(rotationType)

        self.tiles[cornerNumbers[0]], self.tiles[cornerNumbers[1]], self.tiles[cornerNumbers[2]], \
        self.tiles[cornerNumbers[3]] = self.tiles[cornerNumbers[4]], self.tiles[cornerNumbers[5]], \
                                       self.tiles[cornerNumbers[6]], self.tiles[cornerNumbers[7]]

        self.tiles[borderNumbers[0]], self.tiles[borderNumbers[1]], self.tiles[borderNumbers[2]], \
        self.tiles[borderNumbers[3]] = self.tiles[borderNumbers[4]], self.tiles[borderNumbers[5]], \
                                       self.tiles[borderNumbers[6]], self.tiles[borderNumbers[7]]

        if len(cornerRotations) == 0:
            for i in cornerNumbers[:4]:
                self.tiles[i].flip()
        else:
            for i in borderNumbers[:4]:
                self.tiles[i].flip()

            for i in cornerNumbers[:4]:
                self.tiles[i].flip(cornerRotations)
