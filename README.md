# textpy
TextPy is a Python package which helps in extracting the structural features from the text such as the frequency of the words,
avearge length of sentences, average length of words, frequency of punctuations etc. 

# System Requirements
You need a Python 2.7+ interpreter to run textpy

# Platform Support:
Currently textpy is supported only in Linux and Mac. The windows version will be released soon.

# Getting textpy
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

# Public Methods
## words
Words is a public method that returns all the words from the given text.

Example:

## sentences:
Returns all the sentences from the text.

## dates:
Returns all the dates from the text. 

## numbers:
Returns all the numbers from the text. 

## telephone:
Returns all the telephone numbers from the given text. 

## urls:
Returns all the urls from the given text.

# Some example usage of textpy
## Finding out the average length of sentences
Let's first get all the sentences from the text using textpy. 
```python
import textpy
text = 'It was the best of the times, it was the worst of the times.'
sentences = textpy.sentences(text) #Getting all the sentences in the form of list.
```

Then let's compute the length of all the sentences and take the average.
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

## Computing Spelling Accuracy
Let's first get all the words from the text in a list.
```python
import textpy
text = 'It was the best of the times, it was the worst of the times.'
sentences = textpy.words(text) #Getting all the words in the form of list.
```

Then let's get the list of misspelled words.
```python
misspelled = textpy.misspelled_words(text) #Getting all the words in the form of list.
```

Finally, get the spelling accuracy.
Then let's get the list of misspelled words.
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











