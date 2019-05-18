import sys
sys.path.append('/Users/shivabhusal/Documents/research/textpy/src')

import textpy as tp
import unittest

class TestMethods(unittest.TestCase):

    def test_words(self):
    	T = tp.TextPy('Hello World, It was the best of the times3')
        result=T.words()
        self.assertEqual(result[0],"Hello")
        self.assertEqual(len(result),9)
if __name__ == '__main__':
    unittest.main()