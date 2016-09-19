from collections import OrderedDict

from utils import parse_text


class NgramParser(object):
    def __init__(self, file_pool):
        self.file_pool = file_pool
        self.words_list = set()
        self.unigram = OrderedDict()
        self.bigram = OrderedDict()
        self.trigram = OrderedDict()

    def get_words_list(self):
        return self.words_list

    def parser(self):
        last_one = ''
        last_two = ''
        for filename in self.file_pool:
            with open(filename) as file:
                text = file.read()
                words = parse_text(text)
                self.words_list |= set(words)
                for word in words:
                    bigram_key = last_one + ' ' + word
                    trigram_key = last_two + ' ' + last_one + ' ' + word
                    self.bigram[bigram_key] = self.bigram[bigram_key] + 1 if bigram_key in self.bigram else 1
                    self.trigram[trigram_key] = self.trigram[trigram_key] + 1 if trigram_key in self.trigram else 1
                    self.unigram[word] = self.unigram[word] + 1 if word in self.unigram else 1

                    last_two = last_one
                    last_one = word

    def calc_bigram_probability(self, phrase, word):
        return self.calc_probability(phrase=phrase, word=word,
                                     ngram=self.unigram, n_plus_gram=self.bigram)

    def calc_trigram_probability(self, phrase, word):
        return self.calc_probability(phrase=phrase, word=word,
                                     ngram=self.bigram, n_plus_gram=self.trigram)

    def calc_probability(self, phrase, word, ngram, n_plus_gram):
        try:
            return n_plus_gram[phrase + ' ' + word] / ngram[phrase]
        except KeyError:
            return 0
