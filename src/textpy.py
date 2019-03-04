"""
TextPy  is a class that consists of methods to parse a text and get the list of sentences, words,
frequency of words,frequency of punctuations, prepositions, pronouns, articles, abbreviations etc.
In other words, TextPy helps in the structure analysis of a given text.
"""
class TextPy:
    """TextPy consists of methods that help parse Urls, sentences, words, dates,
    and numbers from a given text.
    """
    def __init__(self, text):
        """initializes a tokenizer"""
        self.text = text
        self.words = []
        self.sentences = []
        self.punc = dict()
        self.word_seperator = set(['\t', ' ', '?', '.', ',', '!', ':', ';'])
        self.sen_seperator = set(['.', '?'])
        self.articles = set(['a', 'an', 'the'])
        self.parse_text()

    def parse_text(self):
        """returns all the words in a text"""
        word_queue = []
        sen_queue = []
        for i in range(len(self.text)):
            if self.text[i] in self.sen_seperator:
                if sen_queue:
                    self.sentences.append(''.join(sen_queue))
                    sen_queue = []
            else:
                sen_queue.append(self.text[i])

            if self.text[i] in self.word_seperator:
                if word_queue:
                    current_word = ''.join(word_queue)
                    self.words.append(current_word)
                    word_queue = []
                if self.text[i] in self.punc:
                    self.punc[self.text[i]].append(i)
                else:
                    self.punc[self.text[i]] = [i]
            else:
                word_queue.append(self.text[i])
        if word_queue:
            self.words.append(''.join(word_queue))

    def get_articles(self):
        """Returns the article and the respective frequencies. """
        article_frequency = dict()
        for word in self.words:
            word = word.lower()
            if word in self.articles:
                if word in article_frequency:
                    article_frequency[word] += 1
                else:
                    article_frequency[word] = 1
        return article_frequency

    def get_preps(self):
        """Returns the prepositions and the respective frequencies."""
        prepositions = set(['on', 'in', 'of', 'from', 'under', 'aboard', 'about', 'above',
                            'across', 'after', 'against', 'along', 'amid', 'among', 'anti',
                            'around', 'as', 'at', 'before', 'behind', 'below', 'beneath',
                            'beside', 'besides', 'between', 'beyond', 'but', 'by', 'concerning',
                            'considering', 'despite', 'down', 'during', 'except', 'excepting',
                            'excluding', 'following', 'for', 'from', 'in', 'inside', 'into',
                            'like', 'minus', 'near', 'off', 'on', 'onto', 'opposite',
                            'outside', 'over', 'past', 'per', 'plus', 'regarding', 'round',
                            'save', 'since', 'than', 'through', 'to', 'toward', 'towards',
                            'under', 'underneath', 'unlike', 'until', 'up', 'upon', 'versus',
                            'via', 'with', 'within', 'without'])
        prep_frequency = dict()
        for word in self.words:
            word = word.lower()
            if word in prepositions:
                if word in prep_frequency:
                    prep_frequency[word] += 1
                else:
                    prep_frequency[word] = 1
        return prep_frequency

    def get_punc(self):
        """Returns the punctuations and the list of their occurances by position"""
        return self.punc

    def get_dates(self):
        """Returns the list of dates in the text"""
        return self.text

    def get_sentences(self):
        """Returns the list of sentences in the text"""
        return self.sentences

    def get_numbers(self):
        """Returns the numbers in the text"""
        return self.text

    def get_telephone(self):
        """Returns the telephone numbers in the text"""
        return self.text

    def get_url(self):
        """Returns the URLs in the given text"""
        return self.text

    def get_filenames(self):
        """Returns the filenames from the text"""
        return self.text

    def get_punctuations(self):
        """Returns the list of punctuations"""
        return self.punc

    def get_questions(self):
        """Returns the questions in the text"""
        return self.text

    def get_words(self):
        """Returns all the words in the text"""
        return self.words

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
        epoch of the past. What does it mean ? What a great man !')

print(T.get_words())
print(T.get_punc())
print(T.get_sentences())
print(T.word_frequency())
print(T.get_articles())
print(T.get_preps())
