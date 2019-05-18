# textpy
TextPy is a Python package which helps in extracting the structural features from the text such as the frequency of the words,
avearge length of sentences, average length of words, frequency of punctuations etc. 

# Getting textpy
```pip install textpy```

#System Requirements
You need a Python 3.5+ interpreter to run PyText. 

Platform Support:
Currently TextPy is supported only in Linux and Mac. The windows version will be released soon.


# Examples:
```python
import textpy
T = TextPy('Hello World, It was the best of the times, it was the worst of the times, It was the\
        epoch of the past.In 2011/12/30, What does it mean ? What a great man ! Where are the types of people ?\
           Test string 2010-10-20 Hello World 419-377-4183')
print(T.words)
```

# Public Methods
## words():
Words is a public method that returns all the words from the given text.

Example:

## word_frequency():
Returns the frequency of all the words.

## punc_frequency():
Returns the frequency of all the punctuations.

## sentences():
Returns all the sentences from the text.

## dates():
Returns all the dates from the text. 

## numbers():
Returns all the numbers from the text. 

## telephone():
Returns all the telephone numbers from the given text. 

## urls():
Returns all the urls from the given text.


