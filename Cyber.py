"""
Created on Thurs May 12 3.09 PM

@author: James Tietcheu

"""
import inspect
import keyword
import math
import re
import csv
import sys
import os
import glob
from csv import reader

import pdb

class website_check():

    def __init__(self, path):
        # pdb.set_trace()
        self.path = path
        f = open(path, 'r')
        self.lines = f.read()
        self.lines_words = re.sub(r"[^0-9A-Za-z_]", " ", self.lines)  # getting non-whitespace characters
        self.lines_characters = re.sub(r"[0-9A-Za-z_]", " ", self.lines)  # getting special characters
        f.close()

    def word_unigram(self):

        count = {}
        words = self.lines_words.split()
        for w in words:
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
        return count



    def keyword_count(self):
        keyword_list = ['break', 'case', 'catch', 'continue', 'debugger', 'default', 'delete', 'do', 'else', 'finally',
                       'for', 'function', 'if', 'in', 'instanceof', 'new', 'return', 'switch', 'this', 'throw', 'try',
                       'typeof', 'var', 'void', 'while', 'with']
        count = {}
        unique_keyword = []
        for keywords in keyword_list:
            count[keywords] = self.lines.count(keywords)

        # finding unique keyword option 1
        for key, value in count.items():
            if value == 1:
                unique_keyword.append(key)

        return count

    def token_count(self):
        token_list = ['!', '!=', '!==', '%', '%=', '&', '&&', '&=', '(', ')', '*', '*=', '+', '++', '+=', ',', '-', '--',
                      '-=', '.', '..', '...', '/', '/=', ':', '::', ';', '<', '<<', '<<=', '<=', '=', '==', '===', '>',
                      '>=', '>>', '>>=', '>>>', '>>>=', '?', '[', ']', '^', '^=', '{', '|', '|=', '||', '}', '~']
        count = {}
        words = self.lines_characters.split()
        for token in token_list:
            if token in words:
                count[token] = self.lines_characters.count(token)

        return count

    # finding unique keywords option 2
    def unique_keywords(self):
        keyword_list = ['break', 'case', 'catch', 'continue', 'debugger', 'default', 'delete', 'do', 'else', 'finally',
                       'for', 'function', 'if', 'in', 'instanceof', 'new', 'return', 'switch', 'this', 'throw', 'try',
                       'typeof', 'var', 'void', 'while', 'with']

        count = {}
        result = []
        for keywords in keyword_list:
            count[keywords] = self.lines_words.count(keywords)
        for key, values in count.items():
            if values == 1:
                result.append(key)
        return result

    # finding the the length of each line
    def line_average(self):
        count = {}
        lines = open(self.path, 'r').readlines()
        for line in lines:
            count[line] = len(line)
        return count

    # counting the number of comment symbols
    def comment_count(self):
        comment_list = ['//', '#', '/*', '*/']
        count = {}
        symbols = self.lines_characters.split()
        for comment in comment_list:
            count[comment] = symbols.count(comment)
        return count

    # counting the number of arguments per function
    def parameter_per_function(self):
        count = {}
        lines = open(self.path, 'r').readlines()
        for line in lines:
            if 'function' in line:
                element = line.index('function') + 8    # getting the first element after the word 'function'
                line_updated = line[element:]   # getting the remaining line after the word 'function'
                l_words = re.sub(r"[^0-9A-Za-z_]", " ", line_updated)   # filtering for all non words and numbers
                words = l_words.split()
                count[line] = len(words)    # getting line as a key and the number of arguments of the function as value
        return count

    # determining whether each line start with a whitespace or non-whitespace
    def whitespace_check(self):
        result = []
        row = open(self.path, 'r').readlines()
        for line in row:
            if re.match(r"[0-9A-Za-z_]", line):
                result.append('non-whitespace')
            if re.match(r'[^0-9A-Za-z_]', line):
                result.append('whitespace')
        return result

    # determining whether each line start with a whitespace, tab or new line symbol
    def start_line(self):
        result = []
        counting_newline = 0
        lines = open(self.path, 'r').readlines()
        for line in lines:
            if re.match(r' ', line):
                result.append('whitespace')
            if re.match(r'\t', line):
                result.append('tab')
            if re.match(r'\n', line):
                result.append('new line')

        #counting the number of empty lines option 1
        for element in result:
            if element == 'new line':
                counting_newline += 1

        return result

    # counting the number of empty lines option 2
    def empty_line(self):
        lines = open(self.path, 'r').readlines()
        count = {}
        for line in lines:
            if re.match(r"\n", line):
                count[line] = lines.count(line)
        return count

    def empty_character(self):
        lines = open(self.path, 'r').readlines()
        print(lines)
        i = 0
        word = []
        c = []
        while i < len(lines)-1:
            if lines[i].startswith('\n') and lines[i+1].startswith('}') or lines[i+1].startswith('('):
                c.append('new line')
            i += 1
        print(len(c))
        return len(c)

    # calculating the average length of each line
    def avg_calc(self):
        line_length = 0
        line = self.line_average()
        for key, value in line.items():
            line_length += value
        total_lines = len(line.keys())
        mean = line_length / total_lines
        return mean

    def sd_calc(self):
        data = self.line_average()

        mean, stdev = self.avg_calc(), 0.0
        for key, value in data.items():
            stdev += (float(value) - mean) ** 2
        total_item = len(data.keys())
        stdDev = math.sqrt(stdev / float(total_item - 1))
        print(stdDev)
        return stdDev


def main():
    if len(sys.argv) != 2:
        print('usage: python lexical_feature.py <path-for-search>')
        path = '/Users/jamestietcheu/Downloads/tutoring/Hw7/'
        return path
    path = sys.argv[1]  # user entering the desired path
    return path


if __name__ == '__main__':
    dir_path = main()
    mode = 'r'  # specify the a mode
    directory = os.path.normpath(dir_path)
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".js"):
                my_web = website_check(os.path.join(subdir, file))

    # unigram = my_web.word_unigram()

    # unigram = my_web.keyword_count()
    unigram = my_web.line_average()
    # unigram = my_web.unique_keywords()
    # unigram = my_web.token_count()
    # unigram = my_web.comment_count()
    # unigram = my_web.empty_character()
    # unigram = my_web.start_line()
    # unigram = my_web.empty_line()
    # unigram = my_web.whitespace_check()
    # unigram = my_web.avg_calc()
    # unigram = my_web.sd_calc()
    # unigram = my_web.parameter_per_function()
    # lines.close()  # Close file
    filename = 'result.csv'
    print('hi: ', unigram)
    result = open(filename, 'w')
    for key, value in unigram.items():
        fieldnames = [key, value]
        writer = csv.DictWriter(result, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({key : value})
    #     print(word)
    #     result.writelines()
    file = open(filename, 'r').readlines()
    # print(file)
    # print(unigram)