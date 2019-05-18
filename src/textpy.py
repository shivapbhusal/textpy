"""
TextPy  is a class that consists of methods to parse a text and get the list of sentences, words,
frequency of words,frequency of punctuations, prepositions, pronouns, articles, abbreviations etc.
In other words, TextPy helps in the structure analysis of a given text.
"""
import re

class TextPy:
    """TextPy consists of methods that parse Urls, sentences, words, dates,
    and numbers from a given text.
    """
    def __init__(self, text):
        """initializes a tokenizer"""
        self.text = text
        self.punc = dict()
        self.word_seperator = set(['\t', ' ', '?', '.', ',', '!', ':', ';'])
        self.sen_seperator = set(['.', '?', '!'])

    def words(self):
        """Parses the text and gets the list of words."""
        words =[]
        word_queue = []
        for i in range(len(self.text)):
            if self.text[i] in self.word_seperator:
                if word_queue:
                    current_word = ''.join(word_queue)
                    words.append(current_word)
                    word_queue = []
                if self.text[i] in self.punc:
                    self.punc[self.text[i]] += 1
                else:
                    self.punc[self.text[i]] = 1
            else:
                word_queue.append(self.text[i])
        if word_queue:
            words.append(''.join(word_queue))

        return words

    def punc_frequency(self):
        """Returns the frequency of the punctuations used"""
        return self.punc

    def sentences(self):
        """Parses the text and gets the list of sentences."""
        sentences=[]
        sen_queue = []
        for i in range(len(self.text)):
            if self.text[i] in self.sen_seperator:
                if sen_queue:
                    sentences.append(''.join(sen_queue)+self.text[i])
                    sen_queue = []
            else:
                sen_queue.append(self.text[i])
        if sen_queue:
            sentences.append(''.join(sen_queue))
        return sentences

    def dates(self):
        """Parses the text and gets the frequency of punctuations."""
        pattern = re.compile(r'(\d+/\d+/\d+)|(\d+-\d+-\d+)')
        dates = re.findall(pattern, self.text)
        return dates

    def numbers(self):
        """Parses the text and gets the list of all the numbers."""
        pattern = re.compile(r'\d+')
        numbers = re.findall(pattern, self.text)
        return numbers

    def telephone(self):
        """Parses the text and gets the list of all the telephone numbers."""
        pattern = re.compile(r'^(?:\+?1[-.*]?)?\(?([0-9]{3})\)?[-.*]?([0-9]{3})[-.*]?([0-9]{4})$')
        telephone_nums = re.findall(pattern, self.text)
        return telephone_nums

    def urls(self):
        """Gets the list of all the Urls in the text."""
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        urls = re.findall(pattern, self.text)
        return urls

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

    def get_telephone(self):
        """Returns the telephone numbers from the text"""
        return self.telephone

    def get_numbers(self):
        """Returns all the numbers from the text"""
        return self.numbers

    def misspelled(self):
        """Returns the list of mispelled English words"""
        raise NotImplementedError()