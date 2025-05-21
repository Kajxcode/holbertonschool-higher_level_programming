import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    
    def test_mixed_integers(self):
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)
    
    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)
    
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    
    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)
    
    def test_strings(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
    
    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])
    
    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

if __name__ == "__main__":
    unittest.main()
