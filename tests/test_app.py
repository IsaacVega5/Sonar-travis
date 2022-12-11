import unittest
import numpy as np


import app.fun as fn

class test_calculadora(unittest.TestCase):
    def test_transpose(self):
        x=np.array([[1,4,7],[2,5,8],[3,6,9]])
        result = fn.transpose_np(x)
        correcto = np.array([[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(result.tolist(), correcto.tolist(), "El resultado debería ser [1, 2, 3] [4, 5, 6] [7, 8, 9]")
    
    def test_transpose_no_np(self):
        x=np.array([[1,4,7],[2,5,8],[3,6,9]])
        result = fn.transpose_no_np(x)
        correcto = np.array([[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(result, correcto.tolist(), "El resultado debería ser: [1, 2, 3] [4, 5, 6] [7, 8, 9] ")

    def test_create_mx(self):
        result =fn.create_mx(1,2,3,4,5,6,7,8,9)
        correcto = np.array([[1,2,3],[4,5,6],[7,8,9]])
        self.assertEqual(result.tolist(), correcto.tolist(), "El resultado debería ser: [1, 2, 3] [4, 5, 6] [7, 8, 9] ")



if __name__ == "__main__":
    unittest.main()