import unittest
from lr3 import gen_bin_tree  # Предполагается, что функция в файле lr3.py

class TestGenBinTree(unittest.TestCase):
    
    def test_default_parameters_full_tree(self):
        #Полное дерево с параметрами по умолчанию (height=4, root=8)
        result = gen_bin_tree()
        
        self.assertEqual(result['root'], 8)
        
        self.assertEqual(result['left']['root'], 12.0)  # 8 + (8/2) = 12
        self.assertEqual(result['right']['root'], 64)   # 8 * 8 = 64
        

        self.assertEqual(result['left']['left']['root'], 18.0)   # 12 + 6 = 18
        self.assertEqual(result['left']['right']['root'], 144.0) # 12 * 12 = 144
        
        self.assertEqual(result['right']['left']['root'], 96.0)   # 64 + 32 = 96
        self.assertEqual(result['right']['right']['root'], 4096)  # 64 * 64 = 4096
        

        self.assertIsNotNone(result['left']['left']['left'])
        self.assertIsNotNone(result['right']['right']['right'])
    
    def test_height_1_tree(self):
        #Дерево высотой 1
        result = gen_bin_tree(height=1, root=10)
        expected = {'root': 10, 'left': None, 'right': None}
        self.assertEqual(result, expected)
    
    def test_custom_root_value(self):
        #Дерево с пользовательским корнем
        result = gen_bin_tree(height=2, root=5)
        
        self.assertEqual(result['root'], 5)
        self.assertEqual(result['left']['root'], 7.5)  # 5 + 2.5 = 7.5
        self.assertEqual(result['right']['root'], 25)  # 5 * 5 = 25
        
        self.assertIsNone(result['left']['left'])
        self.assertIsNone(result['left']['right'])
        self.assertIsNone(result['right']['left'])
        self.assertIsNone(result['right']['right'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
