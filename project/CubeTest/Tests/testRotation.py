import unittest
import json
from project.cubePieces import Cube


class TestRotation(unittest.TestCase):

    def setUp(self):
        self.cube = Cube.Cube()

    def test_B_Rotation(self):
        with open('project/CubeTest/Helpers/Json/B.json') as data:
            correctRotation = json.load(data)

        self.cube.rotation('B')
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation,  correctRotation, 'Wrong Rotation')

    def test_B_prim_Rotation(self):
        with open("project/CubeTest/Helpers/Json/B'.json") as data:
            correctRotation = json.load(data)

        self.cube.rotation("B'")
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation,  correctRotation, 'Wrong Rotation')

    def test_D_Rotation(self):
        with open('project/CubeTest/Helpers/Json/D.json') as data:
            correctRotation = json.load(data)

        self.cube.rotation('D')
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation,  correctRotation, 'Wrong Rotation')

    def test_D_prim_Rotation(self):
        with open("project/CubeTest/Helpers/Json/D'.json") as data:
            correctRotation = json.load(data)

        self.cube.rotation("D'")
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation, correctRotation, 'Wrong Rotation')

    def test_E_Rotation(self):
        with open('project/CubeTest/Helpers/Json/E.json') as data:
            correctRotation = json.load(data)

        self.cube.rotation('E')
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation,  correctRotation, 'Wrong Rotation')

    def test_E_prim_Rotation(self):
        with open("project/CubeTest/Helpers/Json/E'.json") as data:
            correctRotation = json.load(data)

        self.cube.rotation("E'")
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation, correctRotation, 'Wrong Rotation')

    def test_F_Rotation(self):
        with open('project/CubeTest/Helpers/Json/F.json') as data:
            correctRotation = json.load(data)

        self.cube.rotation('F')
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation,  correctRotation, 'Wrong Rotation')

    def test_F_prim_Rotation(self):
        with open("project/CubeTest/Helpers/Json/F'.json") as data:
            correctRotation = json.load(data)

        self.cube.rotation("F'")
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation, correctRotation, 'Wrong Rotation')

    def test_L_Rotation(self):
        with open('project/CubeTest/Helpers/Json/L.json') as data:
            correctRotation = json.load(data)

        self.cube.rotation('L')
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation,  correctRotation, 'Wrong Rotation')

    def test_L_prim_Rotation(self):
        with open("project/CubeTest/Helpers/Json/L'.json") as data:
            correctRotation = json.load(data)

        self.cube.rotation("L'")
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation, correctRotation, 'Wrong Rotation')

    def test_M_Rotation(self):
        with open('project/CubeTest/Helpers/Json/M.json') as data:
            correctRotation = json.load(data)

        self.cube.rotation('M')
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation,  correctRotation, 'Wrong Rotation')

    def test_M_prim_Rotation(self):
        with open("project/CubeTest/Helpers/Json/M'.json") as data:
            correctRotation = json.load(data)

        self.cube.rotation("M'")
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation, correctRotation, 'Wrong Rotation')

    def test_R_Rotation(self):
        with open('project/CubeTest/Helpers/Json/R.json') as data:
            correctRotation = json.load(data)

        self.cube.rotation('R')
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation,  correctRotation, 'Wrong Rotation')

    def test_R_prim_Rotation(self):
        with open("project/CubeTest/Helpers/Json/R'.json") as data:
            correctRotation = json.load(data)

        self.cube.rotation("R'")
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation, correctRotation, 'Wrong Rotation')

    def test_S_Rotation(self):
        with open('project/CubeTest/Helpers/Json/S.json') as data:
            correctRotation = json.load(data)

        self.cube.rotation('S')
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation,  correctRotation, 'Wrong Rotation')

    def test_S_prim_Rotation(self):
        with open("project/CubeTest/Helpers/Json/S'.json") as data:
            correctRotation = json.load(data)

        self.cube.rotation("S'")
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation, correctRotation, 'Wrong Rotation')

    def test_U_Rotation(self):
        with open('project/CubeTest/Helpers/Json/U.json') as data:
            correctRotation = json.load(data)

        self.cube.rotation('U')
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation, correctRotation, 'Wrong Rotation')

    def test_U_prim_Rotation(self):
        with open("project/CubeTest/Helpers/Json/U'.json") as data:
            correctRotation = json.load(data)

        self.cube.rotation("U'")
        currentRotation = self.cube.toJson()

        self.assertEqual(currentRotation,  correctRotation, 'Wrong Rotation')

    def tearDown(self):
        self.cube.setDefault()

if __name__ == '__main__':
    unittest.main()
