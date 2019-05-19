"""
This is an example module to test textpy
"""

import textpy

print(textpy.words('hello World.'))
print(textpy.sentences('hello World.'))
print(textpy.numbers('hello World123 Hello World 345'))
print(textpy.telephone('hello World 419-378-4172'))
print(textpy.urls('hello World https://github.com/shivapbhusal/textpy'))
print(textpy.misspelled_words('hello World teetetttte'))
