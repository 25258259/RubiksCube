from BorderTreeNode import BorderTreeNode


class BorderTree:
    def __init__(self, nodes: list):
        if len(nodes) == 0:
            self.nodes = []
        else:
            self.nodes = nodes
        self.rotations = []

    def appendNode(self, node: BorderTreeNode):
        self.nodes.append(node)

    @staticmethod
    def resolvePosition(index):
        '''
        Returns border tree index equivalent to index in cube tiles
        :param index: index in cube tiles
        :return: index in border tree nodes
        '''
        if index > 13:
            return index // 2
        return index // 2 - 1

    def searchProperRotations(self, startingPosition: int, targetPosition: int, oddNumber: bool =
    True):
        startingIndex = self.resolvePosition(startingPosition)
        targetIndex = self.resolvePosition(targetPosition)

    #1. check if on good squere
    #2. check if in children; depth += 1;
    #3.
    #NOT READY BEST NOT TO PUSH
    def searchTree(self, startingNode: BorderTreeNode, targetPosition: BorderTreeNode, deep: int,
                   isOdd: bool = True):
        if deep >= 6:
            return
        else:
            for rotation in startingNode.rotations:
                for index in startingNode.rotations.get(rotation):
                    if targetPosition == index:
                        output = rotation
                        if index == 1:
                            output += "'"
                        self.rotations.append(output)






class BorderTreeNode:
    def __init__(self, firstRotationName: str, firstDestination: BorderTreeNode,
                 secondDestination: BorderTreeNode, secondRotationName: str, thirdDestination:
            BorderTreeNode, fourthDestination: BorderTreeNode):

        self.rotations = {
            firstRotationName: [
                firstDestination,
                secondDestination
            ],
            secondRotationName: [
                thirdDestination,
                fourthDestination
            ]
        }
