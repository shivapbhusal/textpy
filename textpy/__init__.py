"""
An interface to call the public methods of the TextPy Class.
"""

__author__ = 'Shiva Bhusal'

import textpy

def words(text):
    '''
    It is an interface to call the public method of the TextPy Class.
    It returns list of all the words in a text.
    '''
    T = textpy.TextPy()
    return T.words(text)

def sentences(text):
    '''
    Returns all the sentences from the text in the form of list.
    '''
    T = textpy.TextPy()
    return T.sentences(text)

def dates(text):
    '''
    Retuns all the dates from the text in the form of list.
    '''
    T = textpy.TextPy()
    return T.dates(text)

def numbers(text):
    '''
    Retuns all the dates from the text in the form of list.
    '''
    T = textpy.TextPy()
    return T.numbers(text)

def telephone(text):
    '''
    Retuns all the dates from the text in the form of list.
    '''
    T = textpy.TextPy()
    return T.telephone(text)

def urls(text):
    '''
    Returns all the urls from the text in the form of list.
    '''
    T = textpy.TextPy()
    return T.urls(text)

def misspelled_words(text):
    '''
    Retuns all the dates from the text in the form of list.
    '''
    T = textpy.TextPy()
    return T.misspelled_words(text)
