"""
TextPy  is a class that consists of methods to parse a text and get the list of sentences, words,
frequency of words,frequency of punctuations, prepositions, pronouns, articles, abbreviations etc.
In other words, TextPy helps in the structure analysis of a given text.
"""
import re

class TextPy:
    """TextPy consists of methods that help parse Urls, sentences, words, dates,
    and numbers from a given text.
    """
    def __init__(self, text):
        """initializes a tokenizer"""
        self.text = text
        self.words = []
        self.sentences = []
        self.url = []
        self.punc = dict()
        self.word_seperator = set(['\t', ' ', '?', '.', ',', '!', ':', ';'])
        self.sen_seperator = set(['.', '?', '!'])
        self.parse_words()
        self.parse_sentences()
        self.parse_dates()
        self.parse_numbers()
        self.parse_telephone()
        self.parse_url()
        self.parse_filenames()

    def parse_words(self):
        """Parses the text and gets the list of words."""
        word_queue = []
        for i in range(len(self.text)):
            if self.text[i] in self.word_seperator:
                if word_queue:
                    current_word = ''.join(word_queue)
                    self.words.append(current_word)
                    word_queue = []
                if self.text[i] in self.punc:
                    self.punc[self.text[i]] += 1
                else:
                    self.punc[self.text[i]] = 1
            else:
                word_queue.append(self.text[i])
        if word_queue:
            self.words.append(''.join(word_queue))

    def parse_sentences(self):
        """Parses the text and gets the list of sentences."""
        sen_queue = []
        for i in range(len(self.text)):
            if self.text[i] in self.sen_seperator:
                if sen_queue:
                    self.sentences.append(''.join(sen_queue)+self.text[i])
                    sen_queue = []
            else:
                sen_queue.append(self.text[i])
        if sen_queue:
            self.sentences.append(''.join(sen_queue))

    def parse_dates(self):
        """Parses the text and gets the frequency of punctuations."""
        pattern = re.compile(r'(\d+/\d+/\d+)|(\d+-\d+-\d+)')
        self.dates = re.findall(pattern, self.text)
    
    def parse_numbers(self):
        """Parses the text and gets the list of all the numbers."""
        pattern = re.compile(r'\d+')
        self.numbers = re.findall(pattern, self.text)
    
    def parse_url(self):
        """Gets the list of all the Urls in the text."""
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        self.urls = re.findall(pattern, self.text)

    def parse_telephone(self):
        """Parses the text and gets the list of all the telephone numbers."""
        pattern = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
        self.telephone = re.findall(pattern, self.text)
    
    def get_words(self):
        """Returns all the words in the text"""
        return self.words

    def get_sentences(self):
        """Returns all the sentences in the text"""
        return self.sentences

    def get_dates(self):
        """Returns all the dates in the text"""
        return self.dates

    def get_url(self):
        """Returns all the list of Urls in the text"""
        return self.url

    def word_frequency(self):
        """Returns the five most frequent words"""
        word_dict = dict()
        for word in self.words:
            word = word.lower()
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        return word_dict

T = TextPy('Hello World, It was the best of the times, it was the worst of the times, It was the\
        epoch of the past.In 2011/12/30, What does it mean ? What a great man ! Where are the types of people ?\
           Test string 2010-10-20 Hello World 419-377-4183')

print(T.get_words())
print(T.get_sentences())
print(T.get_dates())
print(T.word_frequency())
print(T.get_telephone())
print(T.get_url())
