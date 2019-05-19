__author__ = 'Shiva Bhusal'

import textpy

def get_words(text):
    '''
    Converts roman number to Integer.
    '''
    T = textpy.TextPy()
    parsed_text = T.words(text)
    return parsed_text

def get_sentences(num):
    '''
    Converts integer to roman num.
    '''
    return 'Hello World'