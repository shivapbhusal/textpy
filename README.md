# TextPy
## Introduction
TextPy is a Python package which can be used in extracting contents such as words, sentences, dates, numbers, telephone,
urls, and misspelled words from a given text. 
 
![alt text | 10%](docs/images/logo_transparent.png "Logo Title Text 1")

## System Requirement
You need a Python 2.7+ interpreter to install and run TextPy.

## Platform Support
Currently, TextPy is supported only in Linux and Mac.

## Installation Guidelines
### Download TextPy
Open your terminal and clone the repository using the command below.
```Bash
git clone https://github.com/shivapbhusal/textpy.git
```

Alternatively, you can also download the project from the link below.
```Bash
https://github.com/shivapbhusal/textpy
```

### Install TextPy
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

**Output**
```Bash
['Hello','World']
```

## Function References
### textpy.words(text)
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A list of all the words in the text.
* ***Exception***: Throws *TypeError* exception if the argument is not a string.

```python
import textpy
all_words = textpy.words('Hello World !') # Returns ['Hello','World']
```

### textpy.sentences(text):
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A list of all the sentences in the text.
* ***Exception***: Throws *TypeError* exception if the argument is not a string.

```python
import textpy
all_sentences = textpy.sentences('Hello World.I am using TextPy.') # Returns ['Hello World.','I am using TextPy.']
```

### textpy.dates(text):
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A list of all the dates in the text.
* ***Exception***: Throws *TypeError* exception if the argument is not a string.

```python
import textpy
all_dates = textpy.dates(My name is John Doe. Today's date is 05/20/2019') # Returns ['05/20/2019']
```

### textpy.numbers(text):
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A list of all the numbers in the text.
* ***Exception***: Throws *TypeError* exception if the argument is not a string.

```python
import textpy
all_numbers = textpy.numbers('Hello World 123!') # Returns ['123']
```

### textpy.telephone(text):
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A list of all the telephone numbers in the text.
* ***Exception***: Throws *TypeError* exception if the argument is not a string.

```python
import textpy
all_words = textpy.telephone('My number is 319-378-8183') # Returns ['319-378-8183']
```

### textpy.urls(text):
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A List of all the urls in the text.
* ***Exception***: Throws *TypeError* exception if the argument is not a string.

```python
import textpy
all_words = textpy.urls('Explore https://github.com/.') # Returns 'https://github.com/'
```

### textpy.misspelled_words(text):
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: A List of all the misspelled words in the text.
* ***Exception***: Throws *TypeError* exception if the argument is not a string.

```python
import textpy
all_words = textpy.misspelled_words('Hello Worrlld') # Returns ['Worrlld']
```

## Example Usage
### Finding out the average length of sentences
First, get all the sentences from the text using TextPy. 
```python
import textpy

text = "Marley was dead: to begin with. There is no doubt whatever about that."\ 
"The register of his burial was signed by the clergyman, the clerk, the undertaker,"\ 
"and the chief mourner.Scrooge signed it: and Scrooge’s name was good upon ’Change,"\ 
"for anything he chose to put his hand to. Old Marley was as dead as a door-nail." #Borrowed from A Chrismas Carrol

sentences = textpy.sentences(text)
```

Then, compute the length of all the sentences and take the average.
```python
total = 0
for sen in sentences:
	total += len(sen)
avg_length = total/len(sentences)
```

**Complete Code**
```python
"""
This program computes the average length of sentences using TextPy.
"""
import textpy

text = "Hello World.I am using TextPy."

sentences = textpy.sentences(text)

total = 0
for sen in sentences:
	total += len(sen)
avg_length = total/len(sentences) # avg_length = 15

```

### Computing Spelling Accuracy
First, get all the words from the text in a list.
```python
import textpy
text = 'It was the best of the times, it was the worrrst of the times.'
sentences = textpy.words(text)
```

Then, get the list of misspelled words.
```python
misspelled = textpy.misspelled_words(text)
```

Finally, compute the the spelling accuracy.
```python
spelling_accuracy = float(len(sentences)-len(misspelled))/float(len(sentences))
```

**Complete Code**
```python
"""
This program computes the spelling accuracy of a text using TextPy.
"""
import textpy
text = 'It was the best of the times, it was the worst of the times.'
sentences = textpy.words(text) 
misspelled = textpy.misspelled_words(text)
spelling_accuracy = float(len(sentences)-len(misspelled))/float(len(sentences)) # spelling_accuracy = 0.928

```











