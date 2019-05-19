"""
This is an example module to test textpy
"""

import textpy

print(textpy.words('hello World. This is a great idea.'))
print(textpy.sentences('hello World.'))
print(textpy.numbers('hello World123 Hello World 345'))
print(textpy.telephone('Hello World My number is 319-378-8183'))
print(textpy.urls('hello World https://github.com/shivapbhusal/textpy'))
print(textpy.misspelled_words('hello World teetetttte'))

#Example for exception
print(textpy.words(123))

