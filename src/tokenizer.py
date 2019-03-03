"""
Tokenizer is a class that consists of methods to tokenize a text.
"""
class Tokenize:
    """ Tokenizer"""
    def __init__(self, text):
        """initializes a tokenizer"""
        self.text = text
        self.words = []
        self.word_seperator = set(['\t', ' ', '?', '.', ',', '!', ':', ';'])
        self.sen_separators = set(['.', ';', '?'])
        self.parse_text()

    def get_punc(self):
        """Returns the list of punctuations in the text"""
        return self.text

    def get_dates(self):
        """Returns the list of dates in the text"""
        return self.text

    def get_sentences(self):
        """Returns the list of sentences in the text"""
        return self.text

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
        return self.text

    def get_questions(self):
        """Returns the questions in the text"""
        return self.text

    def get_words(self):
        """Returns all the words in the text"""
        return self.words

    def parse_text(self):
        """returns all the words in a text"""
        word_queue = []
        for i in range(len(self.text)):
            if self.text[i] in self.word_seperator:
                if word_queue:
                    current_word = ''.join(word_queue)
                    self.words.append(current_word)
                    word_queue = []
            else:
                word_queue.append(self.text[i])
        if word_queue:
            self.words.append(''.join(word_queue))

T = Tokenize('Hello World, It was the best of the times, it was the worst of the times, It was the\
        epoch of the past. What does it mean ?')

print(T.get_words())
