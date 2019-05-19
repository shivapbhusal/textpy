import sys
sys.path.append('/Users/shivabhusal/Documents/research/textpy/textpy')

import textpy as tp
import unittest

class TestMethods(unittest.TestCase):

    def test_words(self):
    	T = tp.TextPy()
    	result=T.words('Hello World, It was the best of the times3')
    	self.assertEqual(result[0],"Hello")
    	self.assertEqual(len(result),9)
    
    def test_sentences(self):
    	T = tp.TextPy()
    	result = T.sentences("Hello World.My name is Pablo.")
    	self.assertEqual(result[0],"Hello World.")
    	self.assertEqual(result[1],"My name is Pablo.")
    
    def test_dates(self):
    	T=tp.TextPy()
    	result = T.dates("Hello World. 2015-01-30")
    	self.assertEqual(result[0],'2015-01-30')

    def test_numbers(self):
    	T=tp.TextPy()
    	result = T.numbers("Hello World. 2015-01-30")
    	self.assertEqual(result[0],'2015')

    def test_misspelled_words(self):
    	T = tp.TextPy()
    	result = T.misspelled_words("Hellow World. Porgraming in Python.")
    	self.assertEqual(result[0],'Hellow')

    def test_urls(self):
    	T = tp.TextPy()
    	result = T.urls("The CNN url is https://www.cnn.com/")
    	self.assertEqual(result[0],'https://www.cnn.com/')


if __name__ == '__main__':
    unittest.main()