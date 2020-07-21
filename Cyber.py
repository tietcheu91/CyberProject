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
import pandas as pd
import time
import concurrent.futures
from multiprocessing import Pool

start = time.perf_counter()



class website_check():

    def __init__(self, path):
        # pdb.set_trace()
        m = 'r' # mode
        self.fname = fname
        self.path = path
        self.final_result = {}
        f = open(path, m)
        self.lines = f.read()
        self.file_length = 0
        for element in self.lines:
            self.file_length += 1
        self.lines_words = re.sub(r"[^0-9A-Za-z_]", " ", self.lines)  # getting non-whitespace characters
        self.lines_characters = re.sub(r"[0-9A-Za-z_]", " ", self.lines)  # getting special characters
        f.close()


    def word_unigram(self):
        unigram = 0
        count = {}
        words = self.lines_words.split()
        for w in words:
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
        for key, value in count.items():
            unigram += value
        final_unigram = unigram/self.file_length
        self.final_result['word_unigram'] = final_unigram
        return count

    def keyword_count(self):
        element = 0
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

        for key, value in count.items():
            element += value
        final_element = element/self.file_length
        self.final_result['keyword_count'] = final_element

        return count

    def token_count(self):
        element = 0
        token_list = ['!', '!=', '!==', '%', '%=', '&', '&&', '&=', '(', ')', '*', '*=', '+', '++', '+=', ',', '-', '--',
                      '-=', '.', '..', '...', '/', '/=', ':', '::', ';', '<', '<<', '<<=', '<=', '=', '==', '===', '>',
                      '>=', '>>', '>>=', '>>>', '>>>=', '?', '[', ']', '^', '^=', '{', '|', '|=', '||', '}', '~']
        count = {}
        words = self.lines_characters.split()
        for token in token_list:
            if token in words:
                count[token] = self.lines_characters.count(token)

        for key, value in count.items():
            element += value
        final_element = element/self.file_length
        self.final_result['token_count'] = final_element

        return count

    # finding unique keywords option 2
    def unique_keywords(self):
        element = 0
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

        for value in result:
            element += 1
        final_element = element/self.file_length
        self.final_result['unique_keyword'] = final_element

        return result

    # finding the the length of each line
    def line_average(self):
        element = 0
        count = {}
        lines = open(self.path, 'r').readlines()
        for line in lines:
            count[line] = len(line)

        for key, value in count.items():
            element += value
        final_element = element/self.file_length
        self.final_result['line_average'] = final_element

        return count

    # counting the number of comment symbols
    def comment_count(self):
        element = 0
        comment_list = ['//', '#', '/*', '*/']
        count = {}
        symbols = self.lines_characters.split()
        for comment in comment_list:
            count[comment] = symbols.count(comment)

        for key, value in count.items():
            element += value
        final_element = element/self.file_length
        self.final_result['comment_count'] = final_element

        return count

    # counting the number of arguments per function
    def parameter_per_function(self):
        element = 0
        count = {}
        lines = open(self.path, 'r').readlines()
        for line in lines:
            if 'function' in line:
                element = line.index('function') + 8    # getting the first element after the word 'function'
                line_updated = line[element:]   # getting the remaining line after the word 'function'
                l_words = re.sub(r"[^0-9A-Za-z_]", " ", line_updated)   # filtering for all non words and numbers
                words = l_words.split()
                count[line] = len(words)    # getting line as a key and the number of arguments of the function as value

        for key, value in count.items():
            element += value
        final_element = element/self.file_length
        self.final_result['parameter_per_function'] = final_element

        return count

    # determining whether each line start with a whitespace or non-whitespace
    def whitespace_check(self):
        element = 0
        data = 0
        result = []
        row = open(self.path, 'r').readlines()
        for line in row:
            if re.match(r"[0-9A-Za-z_]", line):
                result.append('non-whitespace')
            if re.match(r'[^0-9A-Za-z_]', line):
                result.append('whitespace')

        for value in result:
            if value == 'whitespace':
                element += 1
            else:
                data += 1
        final_element = element/self.file_length
        final_data = data/self.file_length
        self.final_result['whitespace_check'] = final_element
        self.final_result['non-whitespace_check'] = final_data

        return result

    # determining whether each line start with a whitespace, tab or new line symbol
    def start_line(self):
        element = 0
        data = 0
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

        for value in result:
            if value == 'new line':
                element += 1
            elif value == 'tab':
                data += 1
        final_element = element/self.file_length
        final_data = data/self.file_length
        self.final_result['new line_check'] = final_element
        self.final_result['tab_check'] = final_data

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
        i = 0
        word = []
        c = []
        while i < len(lines)-1:
            if lines[i].startswith('\n') and lines[i+1].startswith('}') or lines[i+1].startswith('('):
                c.append('new line')
            i += 1
        element = len(c)
        final_element = element / self.file_length
        self.final_result['empty_character'] = final_element
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

        self.final_result['Standard_deviation'] = stdDev

        return stdDev

    def output_data(self):

        output = pd.DataFrame(self.final_result, index=self.fname)
        filename = 'result.csv'
        output.to_csv(filename)
        result = open(filename, 'r').read()
        print(result)

    def gettingJsFile(self):
        list_of_files = []
        dir_path = self.folder()
        directory = os.path.normpath(dir_path)  # getting the di
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".js"):
                    list_of_files.append(file)
        return list_of_files

    def file_Execution(self, file):
        my_web = website_check(file)
        my_web.word_unigram()
        my_web.keyword_count()
        my_web.line_average()
        my_web.unique_keywords()
        my_web.token_count()
        my_web.comment_count()
        my_web.empty_character()
        my_web.start_line()
        my_web.empty_line()
        my_web.whitespace_check()
        my_web.avg_calc()
        my_web.sd_calc()
        my_web.parameter_per_function()
        output = my_web.output_data()
        return output


    def folder(self):
        if len(sys.argv) != 2:
            print('usage: python lexical_feature.py <path-for-search>')
            path = '/Users/jamestietcheu/Downloads/tutoring/Hw7/'
            return path
        path = sys.argv[1]  # user entering the desired path
        return path

def main():
    a = website_check()
    with Pool(processes=4) as pool:
        executing_code = a.file_Execution()
        # list_of_files = a.gettingJsFile()
        c = pool.map(executing_code, a.gettingJsFile())
        print(c)


if __name__ == '__main__':

    main()
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')
