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
        self.assertEqual(1,1)

    def test_sentences(self):
    	T = tp.TextPy()
    	result = T.sentences("Hello World.My name is Pablo.")
    	self.assertEqual(result[0],"Hello World.")
    	self.assertEqual(result[1],"My name is Pablo.")
        self.assertRaises(TypeError,T.words(12345))
    
    def test_dates(self):
    	T=tp.TextPy()
    	result = T.dates("My name is John Doe. Today's date is 05/20/2019")
    	self.assertEqual(result[0],'05/20/2019')

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

    def test_telephone(self):
        T = tp.TextPy()
        result = T.telephone("Hello World My number is 319-378-8183")
        self.assertEqual(result[0],'319-378-8183')


if __name__ == '__main__':
    unittest.main()
