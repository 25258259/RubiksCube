class MiddleTile:
    '''
    Representation of the one color tile in cube
    :color: color of the tile
    '''
    def __init__(self, color: str = 'red'):
        self.color = color

    def flip(self) -> None:
        '''
        Function to flip colors depending on the rotation
        '''
        pass

    def __eq__(self, other) -> bool:
        '''
        Function to check if this and other are same
        :param other: other middle tile
        :return: True of False if they are same or not
        '''
        if self.color == other.color:
            return True
        return False


class BorderTile:
    '''
    Representation of the border tile in cube. The order of sides is:
        left/right before front/back,
        up/bottom before left/right,
        front/back before up/bottom

    :firstColor: color of the first side
    :secondColor: color of the second side
    '''
    def __init__(self, firstColor: str = 'red', secondColor: str = 'green'):
        """Order is left/right, front/back and up/bottom, left/right and front/back, up/bottom"""
        self.firstColor = firstColor
        self.secondColor = secondColor

    def flip(self) -> None:
        '''
        Function to flip colors depending on the rotation
        '''
        self.firstColor, self.secondColor = self.secondColor, self.firstColor

    def __eq__(self, other) -> bool:
        '''
        Function to check if this and other are same
        :param other: other border tile
        :return: True or False if they are the same or not
        '''
        if self.firstColor == other.firstColor:
            if self.secondColor == other.secondColor:
                return True
        if self.firstColor == other.secondColor:
            if self.secondColor == other.firstColor:
                return True

        return False


class CornerTile:
    '''
    Representation of the corner tile in cube. Sides colors in order up/bottom, left/right,
    front/back.
    :firstColor: color of the first side
    :secondColor: color of the second side
    :thirdColor: color of the third side
    '''
    def __init__(self, firstColor: str = 'red', secondColor: str = 'green', thirdColor: str =
    'yellow'):
        """Order is up/bottom, left/right, front/back"""
        self.firstColor = firstColor
        """up/bottom"""
        self.secondColor = secondColor
        """left/right"""
        self.thirdColor = thirdColor
        """front/back"""

    def flip(self, rotation) -> None:
        '''
        Function to flip colors depending on the rotation
        :rotation: which rotation type you performed
        '''
        if rotation == '1':  # 1
            self.firstColor, self.secondColor = self.secondColor, self.firstColor
        elif rotation == '2':  # 2
            self.secondColor, self.thirdColor = self.thirdColor, self.secondColor
        elif rotation == '3':  # 3
            self.firstColor, self.thirdColor = self.thirdColor, self.firstColor
        else:
            print('unknown rotation')

    def __eq__(self, other) -> bool:
        '''
        Function to check if self and other are the same
        :param other: other corner tile
        :return: True or False if they are the same or not
        '''
        colors1 = [self.firstColor, self.secondColor, self.thirdColor]
        colors2 = [other.firstColor, other.secondColor, other.thirdColor]

        if sorted(colors1) == sorted(colors2):
            return True
        return False
