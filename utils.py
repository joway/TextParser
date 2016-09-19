import glob
import re


def list_filenames(query):
    return [filename for filename in glob.iglob(query, recursive=True)]


def parse_text(text):
    regex = re.compile('[^a-zA-Z ]')
    return [x for x in regex.sub('', text).lower().split(' ') if x != '']


def write_to_file(msg):
    with open('log.txt', 'a+') as file:
        file.write(msg + '\n')


