# TextPy
## Introduction
TextPy is a Python package that helps in extracting contents such as words, sentences, dates, numbers, telephone,
urls etc from a given text. 

## System Requirements
You need a Python 2.7+ interpreter to run textpy

## Platform Support:
Currently, textpy is supported only in Linux and Mac.

## Getting TextPy
Clone the repository from the link below:
```Bash
git clone https://github.com/shivapbhusal/textpy.git
```

or download the source code from the link and unzip it.
```Bash
https://github.com/shivapbhusal/textpy
```

Open your terminal, navigate to the root of the project folder, and enter the command below:
```Bash
sudo python setup.py install
```

Test and validate the installation using your Python terminal.

```python
import textpy
print(textpy.words('Hello World !'))
```

## Method References
### words(text)
* ***Description***: Returns the list of all the words in the text.
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: List of strings representing all the words.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_words = textpy.words('Hello World !')
```

### sentences(text):
* ***Description***: Returns the list of all the sentences in the text.
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: List of strings representing each sentences.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_words = textpy.sentences('Hello World !')
```

### dates(text):
* ***Description***: Returns the list of all the dates in the text.
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: List of strings representing dates in the text.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_words = textpy.dates('Hello World !')
```

### numbers(text):
* ***Description***: Returns the list of all the numbers in the text.
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: List of strings representing numbers in the text.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_words = textpy.numbers('Hello World 123!')
```

### telephone:
* ***Description***: Returns the list of all the telephone numbers in the text.
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: List of strings representing telephone numbers in the text.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_words = textpy.telephone('Hello World 123!')
```

### urls:
Returns all the urls from the given text.
* ***Description***: Returns the list of all the urls in the text.
* ***Parameter***: A string representing the text to be analyzed.
* ***Returns***: List of strings representing urls in the text.
* ***Exception***: Throws an exception if the argument is not a string.

```python
import textpy
all_words = textpy.urls('Hello World 123!')
```

## Example Usage
### Finding out the average length of sentences
First, get all the sentences from the text using textpy. 
```python
import textpy
text = 'It was the best of the times, it was the worst of the times.'
sentences = textpy.sentences(text) #Getting all the sentences in the form of list.
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
import textpy
text = 'It was the best of the times, it was the worst of the times.'
sentences = textpy.words(text) #Getting all the words in the form of list.
misspelled = textpy.misspelled_words(text)
spelling_accuracy = (len(sentences)-len(misspelled))/len(sentences)

```

## License and author info











