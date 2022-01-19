class MiddleTile:
    def __init__(self, color: str = 'red'):
        """Input is color in str"""
        self.color = color

    def flip(self):
        pass

    def __eq__(self, other):
        if self.color == other.color:
            return True
        return False


class BorderTile:
    def __init__(self, firstColor: str = 'red', secondColor: str = 'green'):
        """Order is left/right, front/back and up/bottom, left/right and front/back, up/bottom"""
        self.firstColor = firstColor
        self.secondColor = secondColor

    def flip(self):
        self.firstColor, self.secondColor = self.secondColor, self.firstColor

    def __eq__(self, other):
        if self.firstColor == other.firstColor:
            if self.secondColor == other.secondColor:
                return True
        if self.firstColor == other.secondColor:
            if self.secondColor == other.firstColor:
                return True

        return False


class CornerTile:
    def __init__(self, firstColor: str = 'red', secondColor: str = 'green', thirdColor: str =
    'blue'):
        """Order is up/bottom, left/right, front/back"""
        self.firstColor = firstColor
        """up/bottom"""
        self.secondColor = secondColor
        """left/right"""
        self.thirdColor = thirdColor
        """front/back"""

    def flip(self, rotation):
        if rotation == '1':  # 1
            self.firstColor, self.secondColor = self.secondColor, self.firstColor
        elif rotation == '2':  # 2
            self.secondColor, self.thirdColor = self.thirdColor, self.secondColor
        elif rotation == '3':  # 3
            self.firstColor, self.thirdColor = self.thirdColor, self.firstColor
        else:
            print('unknown rotation')

    def __eq__(self, other):
        colors1 = [self.firstColor, self.secondColor, self.thirdColor]
        colors2 = [other.firstColor, other.secondColor, other.thirdColor]

        if sorted(colors1) == sorted(colors2):
            return True
        return False
