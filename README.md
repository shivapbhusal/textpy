# TextPy
## Introduction
TextPy is a Python package that helps in extracting contents such as words, sentences, dates, numbers, telephone,
urls, and mispelled words from a given text. 
 
![alt text](docs/images/logo_transparent.png "Logo Title Text 1")

## System Requirements
You need a Python 2.7+ interpreter to run install and run TextPy.

## Platform Support:
Currently, TextPy is supported only in Linux and Mac.

## Getting TextPy
Open your terminal and clone the repository using the command below:
```Bash
git clone https://github.com/shivapbhusal/textpy.git
```

or download the source code from the link and unzip it.
```Bash
https://github.com/shivapbhusal/textpy
```

Navigate to the root of the project directory, and enter the command below.
```Bash
sudo python setup.py install
```

Test and validate the installation using your Python terminal.

```python
import textpy
```

```python
print(textpy.words('Hello World !'))
```

Output
```Bash
['Hello','World']
```

## Function References
### textpy.words(text)
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A list of all the words in the text.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_words = textpy.words('Hello World !') # Returns ['Hello','World']
```

### textpy.sentences(text):
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A list of all the sentences in the text.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_sentences = textpy.sentences('Hello World !') # Returns ['Hello World!']
```

### textpy.dates(text):
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A list of all the dates in the text.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_dates = textpy.dates(My name is John Doe. Today's date is 05/20/2019') # Returns ['05/20/2019']
```

### textpy.numbers(text):
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A list of all the numbers in the text.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_numbers = textpy.numbers('Hello World 123!') # Returns ['123']
```

### textpy.telephone(text):
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A list all the telephone numbers in the text.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_words = textpy.telephone('My number is 319-378-8183') # Returns ['319-378-8183']
```

### textpy.urls(text):
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A List of all the urls in the text.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_words = textpy.urls('Explore https://github.com/.') # Returns 'https://github.com/'
```

## Example Usage
### Finding out the average length of sentences
First, get all the sentences from the text using textpy. 
```python
import textpy
text = 'It was the best of the times, it was the worst of the times.'
sentences = textpy.sentences(text) # Getting all the sentences in the form of list.
```

Then compute the length of all the sentences and take the average.
```python
total = 0
for sen in sentences:
	total = total + len(sen)
avg_length = total/len(sentences)
```

Full working code
```python
"""
This program the average length of sentences using textpy.
"""
import textpy
text = 'It was the best of the times, it was the worst of the times.'
sentences = textpy.sentences(text)

total = 0
for sen in sentences:
	total = total + len(sen)
avg_length = total/len(sentences)

```

### Computing Spelling Accuracy
First get all the words from the text in a list.
```python
import textpy
text = 'It was the best of the times, it was the worst of the times.'
sentences = textpy.words(text) #Getting all the words in the form of list.
```

Then, get the list of misspelled words.
```python
misspelled = textpy.misspelled_words(text) #Getting all the words in the form of list.
```

Finally, compute the the spelling accuracy.
```python
spelling_accuracy = (len(sentences)-len(misspelled))/len(sentences) #Getting all the words in the form of list.
```

Full working code:
```python
"""
This program computes the spelling accuracy of a text using TextPy.
"""
import textpy
text = 'It was the best of the times, it was the worst of the times.'
sentences = textpy.words(text) #Getting all the words in the form of list.
misspelled = textpy.misspelled_words(text)
spelling_accuracy = (len(sentences)-len(misspelled))/len(sentences)

```











