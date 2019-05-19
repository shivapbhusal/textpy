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
    def get_english_words(self):
        """
        Takes the English dictionary from the unix system and returns the list of words.
        """
        english_word_set = set()
        with open('/usr/share/dict/words', 'r') as english_dict:
            for english_word in english_dict:
                english_word = english_word.strip()
                english_word_set.add(english_word)
            english_dict.close()
        return english_word_set

    def words(self, text):
        """Parses the text and gets the list of words."""
        word_seperator = set(['\t', ' ', '?', '.', ',', '!', ':', ';'])
        words = []
        word_queue = []
        for i in range(len(text)):
            if text[i] in word_seperator:
                if word_queue:
                    current_word = ''.join(word_queue)
                    words.append(current_word)
                    word_queue = []
            else:
                word_queue.append(text[i])
        if word_queue:
            words.append(''.join(word_queue))

        return words

    def punc_frequency(self, text):
        """Returns the frequency of the punctuations used"""
        punc_list = ['?', ',', ':', ';', ',']
        punc = dict()
        for i in range(len(text)):
            if text[i] in punc_list:
                if text[i] in punc:
                    punc[text[i]] += 1
                else:
                    punc[text[i]] = 1
        return punc

    def sentences(self, text):
        """Parses the text and gets the list of sentences."""
        sen_seperator = set(['.', '?', '!'])
        sentences = []
        sen_queue = []
        for i in range(len(text)):
            if text[i] in sen_seperator:
                if sen_queue:
                    sentences.append(''.join(sen_queue)+text[i])
                    sen_queue = []
            else:
                sen_queue.append(text[i])
        if sen_queue:
            sentences.append(''.join(sen_queue))
        return sentences

    def dates(self, text):
        """Parses the text and gets all the dates present in the text."""
        pattern = re.compile(r'(\d+/\d+/\d+)|(\d+-\d+-\d+)')
        dates = re.findall(pattern, text)
        return dates

    def numbers(self, text):
        """Parses the text and gets the list of all the numbers."""
        pattern = re.compile(r'\d+')
        numbers = re.findall(pattern, text)
        return numbers

    def telephone(self, text):
        """Parses the text and gets the list of all the telephone numbers."""
        pattern = re.compile(r'^(?:\+?1[-.*]?)?\(?([0-9]{3})\)?[-.*]?([0-9]{3})[-.*]?([0-9]{4})$')
        telephone_nums = re.findall(pattern, text)
        return telephone_nums

    def urls(self, text):
        """Gets the list of all the Urls in the text."""
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        urls = re.findall(pattern, text)
        return urls

    def misspelled_words(self, text):
        """Returns the list of mispelled English words"""
        misspelled_list = []
        english_word_set = self.get_english_words()
        all_words = self.words(text)
        for word in all_words:
            lower_case_word = word.lower()
            if lower_case_word not in english_word_set:
                misspelled_list.append(word)
        return misspelled_list
