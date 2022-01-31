import unittest
from project.cubePieces import Cube


class MyTestCase(unittest.TestCase):
    def setUp(self):
        cube = Cube.Cube()

    def tearDown(self):
        cube = Cube.Cube()
