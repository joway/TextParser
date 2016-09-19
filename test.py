from parser import NgramParser
from utils import list_filenames

FILE_QUERY = 'data/bookList/*.txt'

file_pool = list_filenames(FILE_QUERY)
parser = NgramParser(file_pool=file_pool)
parser.parser()
while True:
    phrase = input('Enter : \n')
    if not phrase:
        break
    matched_list = {}
    for w in parser.get_words_list():
        if len(phrase.split(' ')) == 1:
            matched_list[w] = parser.calc_bigram_probability(phrase, w)
        elif len(phrase.split(' ')) == 2:
            matched_list[w] = parser.calc_trigram_probability(phrase, w)
        else:
            raise Exception('%s is illegal' % phrase)

    matched_list = sorted(matched_list.items(), key=lambda d: d[1], reverse=True)
    for i in range(10):
        print(matched_list[i])

    phrase = ''
