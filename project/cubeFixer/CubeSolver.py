from project.cubePieces.Cube import Cube
from ..colorsConversions.ColorsOnColors import colorsBorderNumbers, colorsOfBordersColors
from project.cubePieces.Tiles import CornerTile


class CubeSolver:
    '''
    Class which is solving the cube using various algorithms
    :cube: cube object you want to solve
    '''
    cornersIndexInCubeIndex = {
        0: 0,
        1: 2,
        2: 6,
        3: 8
    }

    algorithms = {
        "6to0": ["D", "L", "D'", "L'"],
        "8to2": ["D'", "R'", "D", "R"]
    }

    solvedCube: Cube = Cube()

    def __init__(self, cube: Cube):
        self.cube = cube
        self.combination = []

    def solveTheCube(self, easyWay: bool = True):
        color = self.findWhiteCross("white")
        if easyWay:
            self.endFirstSide()
            self.endSecondLayer()
        else:
            self.endTwoLayers()

    def endFirstSide(self, color: str = "white"):
        corners = [
            CornerTile(colorsOfBordersColors.get(color)[0], colorsOfBordersColors.get(
                color)[1], color),
            CornerTile(colorsOfBordersColors.get(color)[0], colorsOfBordersColors.get(
                color)[2], color),
            CornerTile(colorsOfBordersColors.get(color)[3], colorsOfBordersColors.get(
                color)[1], color),
            CornerTile(colorsOfBordersColors.get(color)[3], colorsOfBordersColors.get(
                color)[2], color)
        ]

        cornersIndexes = [0, 2, 6, 8, 18, 20, 24, 26]
        cornerDestination = {}

        for cornersIndex in cornersIndexes:
            for index, corner in enumerate(corners):
                if self.cube.tiles[cornersIndex] == corner:
                    cornerDestination[cornersIndex] = self.cornersIndexInCubeIndex[index]

        for key in cornerDestination:
            if key == cornerDestination[key]:
                if self.cube.tiles[key].inRightPlace(corners[self.cubeIndexBackToCornerIndex(key)]):
                    del cornerDestination[key]
                elif self.cube.tiles[key].firstColor == corners[self.cubeIndexBackToCornerIndex(
                        key)].thirdColor:
                    pass
                    #TODO: proper cube rotation



    def cubeIndexBackToCornerIndex(self, index: int):
        backIndex = {value : key for (key, value) in self.cornersIndexInCubeIndex.items()}
        return backIndex[index]

    def endSecondLayer(self):
        pass

    def endTwoLayers(self):
        pass

    def choosingBestColor(self) -> str:
        '''
        Choosing the best side to start solving. It finds the easiest side to get starting cross
        position. Default color is white
        :return: color we want to start with
        '''
        marks = {
            "white": [0, "side"],
            "red": [0, "side"],
            "orange": [0, "side"],
            "green": [0, "side"],
            "blue": [0, "side"],
            "yellow": [0, "side"]
        }

        sides = ["front", "left", "right", "up", "bottom", "back"]
        maxLen = 0

        for side in sides:
            colors = self.cube.toColor(side)
            mainColor = colors[4]
            marks.get(mainColor)[1] = side
            points = 0
            for i in range(1, 8, 2):
                if colors[i] == mainColor:
                    points += 1
            marks[mainColor][0] = points

            if points > maxLen:
                maxLen = points

        for color in marks:
            if marks.get(color)[0] == maxLen:
                return color

    def setBestSide(self, color: str) -> None:
        '''
        Function that rotates depending on the color we want to start.
        While rotating it's saving used rotations to self.combination
        :color: color name that should be on the front
        '''
        if color == self.cube.tiles[10].color:
            self.cube.moreThenOneSideRotation("x'")
            self.combination.append("x'")
        elif color == self.cube.tiles[12].color:
            self.cube.moreThenOneSideRotation("y'")
            self.combination.append("y'")
        elif color == self.cube.tiles[14].color:
            self.cube.moreThenOneSideRotation("y")
            self.combination.append("y")
        elif color == self.cube.tiles[16].color:
            self.cube.moreThenOneSideRotation("x")
            self.combination.append("x")
        elif color == self.cube.tiles[22].color:
            self.cube.moreThenOneSideRotation("y")
            self.cube.moreThenOneSideRotation("y")
            self.combination.append("y")
            self.combination.append("y")

        colors = colorsOfBordersColors
        upColor = self.cube.upToColor()[4]
        counter = 0
        while upColor != colors.get(color)[0]:
            self.cube.moreThenOneSideRotation('z')
            self.combination.append("z")
            upColor = self.cube.upToColor()[4]
            counter += 1

    def findWhiteCross(self, color: str = '') -> str:
        '''
        Sets the cross in best color
        '''
        # mark each side
        # choose the closest to the cross
        # find right borderTile
        if len(color) == 0:
            color = self.choosingBestColor()

        self.setBestSide(color)
        unreadyChanges = self.findWhiteCrossPieces(color)
        print(color)
        neededChanges = {}
        #getting the neededChanges numbers to current position
        for key, val in unreadyChanges.items():
            print(f'Key: {key}, Val: {val}')
            newIndex = colorsBorderNumbers[color].index(key) * 2 + 1
            neededChanges[newIndex] = val

        print(neededChanges)
        # TODO find the right rotation algorithm
        # base on the position choose the best solution
        # move it to right place
        # check if the cross is achieved
        return color

    def findWhiteCrossPieces(self, color: str) -> dict:
        '''
        Finds which border tiles are needed to move
        :param color: front color name
        :return: dictionary with needed tiles as keys and their current position
        '''
        indexes = [x for x in range(1, 26, 2)]
        del indexes[6]

        tilesPosition = {}
        rightTiles = colorsBorderNumbers.get(color)
        for tileIndex in indexes:
            if self.solvedCube.tiles[rightTiles[0]] == self.cube.tiles[tileIndex]:
                tilesPosition[rightTiles[0]] = tileIndex
            elif self.solvedCube.tiles[rightTiles[1]] == self.cube.tiles[tileIndex]:
                tilesPosition[rightTiles[1]] = tileIndex
            elif self.solvedCube.tiles[rightTiles[2]] == self.cube.tiles[tileIndex]:
                tilesPosition[rightTiles[2]] = tileIndex
            elif self.solvedCube.tiles[rightTiles[3]] == self.cube.tiles[tileIndex]:
                tilesPosition[rightTiles[3]] = tileIndex

        return tilesPosition


