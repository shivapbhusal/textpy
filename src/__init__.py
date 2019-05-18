__author__ = 'Shiva Bhusal'

import textpy as tp

def get_words(text):
    '''
    Converts roman number to Integer.
    '''
    T = tp.TextPy()
    parsed_text = T.get_words(text)
    return parsed_text

def get_sentences(num):
    '''
    Converts integer to roman num.
    '''
    return 'Hello World'