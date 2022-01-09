from project.cubePieces import Cube
from project.cubePieces.Tiles import middleTile, borderTile, cornerTile


if __name__ == '__main__':
    cube = Cube.Cube([cornerTile('yellow', 'blue', 'red'), borderTile('red', 'yellow'),
                      cornerTile('yellow', 'green', 'red'), borderTile('blue', 'red'),
                      middleTile('red'), borderTile('green', 'red'),
                      cornerTile('white', 'blue', 'red'), borderTile('red', 'white'),
                      cornerTile('white', 'green', 'red'),
                      borderTile('yellow', 'blue'), middleTile('yellow'),
                      borderTile('yellow','green'), middleTile('blue'),
                      None, middleTile('green'), borderTile('white', 'blue'), middleTile('white'),
                      borderTile('white', 'green'),
                      cornerTile('yellow', 'blue', 'orange'), borderTile('orange', 'yellow'),
                      cornerTile('yellow', 'green', 'orange'), borderTile('blue', 'orange'),
                      middleTile('orange'), borderTile('green', 'orange'),
                      cornerTile('white', 'blue', 'orange'), borderTile('orange', 'white'),
                      cornerTile('white', 'green', 'orange')
                    ,])

    cube2 = Cube.Cube()

    cube2.oneSideRotation('F')
    print(cube2)