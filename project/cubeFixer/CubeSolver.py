from project.cubePieces.Cube import Cube


class CubeSolver:
    '''
    Class which is solving the cube using various algorithms
    :cube: cube object you want to solve
    '''
    algorithms = {}

    solvedCube = Cube()

    def __init__(self, cube: Cube):
        self.cube = cube
        self.solvedCube = Cube
        self.combination = []

    def choosingBestSide(self) -> str:
        '''
        Choosing the best side to start solving. It finds the easiest side to get starting cross
        position
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
            name = 'cross'
            for i in range(1, 8, 2):
                if colors[i] == mainColor:
                    name += str(i)
            marks[mainColor][0] = len(name)

            if len(name) > maxLen:
                maxLen = len(name)

        for color in marks:
            if marks.get(color)[0] == maxLen:
                return color

    def setBestSide(self) -> None:
        '''
        Function that rotates depending on the color we want to start.
        While rotating it's saving used rotations to self.combination
        '''
        color = self.choosingBestSide()
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

        colors = {
            "green": "yellow",
            "red": "yellow",
            "orange": "yellow",
            "blue": "yellow",
            "white": "red",
            "yellow": "orange"
        }

        upColor = self.cube.upToColor()[4]
        counter = 0
        while upColor != colors.get(color):
            self.cube.moreThenOneSideRotation('z')
            self.combination.append("z")
            upColor = self.cube.upToColor()[4]
            counter += 1

    def findWhiteCross(self) -> None:
        '''
        Sets the cross in best color
        '''
        # mark each side
        # choose the closest to the cross
        self.setBestSide()
        # base on the position choose the best solution

        # find right borderTile
        # move it to right place
        # check if the cross is achieved
