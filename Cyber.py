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

def word_unigram(lines):

    count = {}
    words = []
    words = lines.split()
    print(words)
    for w in words:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1
    return count



def keyword_count(lines):
    keywordList = ['break', 'case', 'catch', 'continue', 'debugger', 'default', 'delete', 'do', 'else', 'finally',
                   'for', 'function', 'if', 'in', 'instanceof', 'new', 'return', 'switch', 'this', 'throw', 'try',
                   'typeof', 'var', 'void', 'while', 'with']
    count = {}
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', 'r').read()
    for keywords in keywordList:
        count[keywords] = lines.count(keywords)
    return count

def token_count(lines):
    token_list = ['!', '!=', '!==', '%', '%=', '&', '&&', '&=', '(', ')', '*', '*=', '+', '++', '+=', ',', '-', '--',
                  '-=', '.', '..', '...', '/', '/=', ':', '::', ';', '<', '<<', '<<=', '<=', '=', '==', '===', '>',
                  '>=', '>>', '>>=', '>>>', '>>>=', '?', '[', ']', '^', '^=', '{', '|', '|=', '||', '}', '~']
    words = []
    count = {}
    words = lines.split()
    print(words)
    for token in token_list:
        if token in words:
            count[token] = lines.count(token)
            # print(w)
                 # counting the number of matching tokens
    return count


def unique_keywords(lines):
    keyword_list = ['break', 'case', 'catch', 'continue', 'debugger', 'default', 'delete', 'do', 'else', 'finally',
                   'for', 'function', 'if', 'in', 'instanceof', 'new', 'return', 'switch', 'this', 'throw', 'try',
                   'typeof', 'var', 'void', 'while', 'with']

    count = {}
    words = []
    result = []
    words = lines.split()
    print(words)
    for keywords in keyword_list:
        count[keywords] = lines.count(keywords)
    for key, values in count.items():
        if values == 1:
            result.append(key)
    return result

def line_average():
    s = []
    count = {}
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', 'r').readlines()
    for l in lines:
        for ls in l:
            s += ls
            # print(s)
        count[l] = len(l)
        # print(ls)
    return count

def comment_count(lines):
    comment_list = ['//', '#', '/*', '*/']
    words = []
    count = {}
    words = lines.split()
    print(words)
    for comment in comment_list:
        count[comment] = words.count(comment)
        # print(w)
        # counting the number of matching tokens
    print(count)

def parameter_per_function(lines):
    # comment_list = ['//', '#', '/*', '*/']
    words = []
    count = {}
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', 'r').readlines()
    # print(words)
    for l in lines:
        if 'function' in l:
            element = l.index('function') + 8
            l_new = l[element:]
            l_words = re.sub(r"[^0-9A-Za-z_]", " ", l_new)
            words = l_words.split()
            count[l] = len(words)
    return count


def whitespace_check():
    result = []
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', 'r').readlines()
    print(lines)
    for line in lines:
        if re.match(r"[0-9A-Za-z_]", line):
            result.append('non-whitespace')
            # return True
        if re.match(r'[^0-9A-Za-z_]', line):
            result.append('whitespace')
            # return False
    return result

def start_line():
    c = []
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', 'r').readlines()
    print(lines)
    for line in lines:
        if re.match(r' ', line):
            c.append('whitespace')
        if re.match(r'\t', line):
            c.append('tab')
        if re.match(r'\n', line):
            c.append('new line')
    return c

def empty_line():
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', 'r').readlines()
    count = {}
    for line in lines:
        if re.match(r"\n", line):
            count[line] = lines.count(line)
            # count += 1
    return len(count)

def empty_character():
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', 'r').readlines()
    i = 0
    word = []
    c = []
    while i < len(lines)-1:
        if lines[i].startswith('\n') and lines[i+1].startswith('}'):
            c.append('new line')
        i += 1
    print(len(c))


def avg_calc():
    c = 0
    line = line_average()
    for key, value in line.items():
        c += value
    total_item = len(line.keys())
    mean = c / total_item
    return mean

def sd_calc():
    data = line_average()

    mean, stdDev = avg_calc(), 0.0
    for key, value in data.items():
        stdDev += (float(value) - mean) ** 2
    total_item = len(data.keys())
    stdDev = math.sqrt(stdDev / float(total_item - 1))
    print(stdDev)
    # return stdDev


def main():
    # dir = input("Enter the directory of the file: ")
    len_of_file = 0
    mode = 'r' # specify the a mode
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', mode).read()  # Open file on read mode and reading the entire file
    # getting the length of the file
    print(lines)
    for element in lines:
        len_of_file += len(element)
    # print(len_of_file)
    lines_words = re.sub(r"[^0-9A-Za-z_]", " ", lines) # spacing the elements
    lines_characters = re.sub(r"[0-9A-Za-z_]", " ", lines)
    # print("hi: ", lines_characters)
    # jsToCsv(dir)
    # unigram = word_unigram(lines_words)
    # keyword_count(lines)
    # line_average()
    # unique_keywords(lines_words)
    # token_count(lines_characters)
    # comment_count(lines)
    empty_character()
    # start_line()
    # empty_line()
    # whitespace_check()
    # avg_calc()
    # sd_calc()
    # parameter_per_function(lines)
    # lines.close()  # Close file
    # result = open('result.csv', 'w')
    # for word in unigram:
    #     result.write(word)


if __name__ == '__main__':
    main()
