import unittest

from codigos.naive_algorithm import naive_algorithm

class TestCase(unittest.TestCase):
    def test(self):
        text = "banana"
        pattern = "ana"
        index = [1,3]
        self.assertEqual(naive_algorithm(pattern,text),index)


if __name__ == '__main__':
    unittest.main()
