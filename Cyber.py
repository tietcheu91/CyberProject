"""
Created on Thurs May 12 3.09 PM

@author: James Tietcheu

"""
import keyword
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
    print(count)
    # for word, times in count.items():
    #     print("%s was found %d times" % (word, times))


def keyword_count(lines):
    keywordList = ['break', 'case', 'catch', 'continue', 'debugger', 'default', 'delete', 'do', 'else', 'finally',
                   'for', 'function', 'if', 'in', 'instanceof', 'new', 'return', 'switch', 'this', 'throw', 'try',
                   'typeof', 'var', 'void', 'while', 'with']
    count = {}
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', 'r').read()
    for keywords in keywordList:
        count[keywords] = lines.count(keywords)
    print(count)
    # count = {}
    # words = []
    # c = 0
    # words = lines.split()
    # len_of_file = len(words)
    # print("the length of the file is: ", len_of_file)
    # # print(words)
    # for w in words:
    #     if w in keywordList:
    #         # print(w)
    #         c += 1      # counting the number of occurrences of keywords
    # print(c)
    # print(c/len_of_file)

def token_count(lines):
    token_list = ['!', '!=', '!==', '%', '%=', '&', '&&', '&=', '(', ')', '*', '*=', '+', '++', '+=', ',', '-', '--',
                  '-=', '.', '..', '...', '/', '/=', ':', '::', ';', '<', '<<', '<<=', '<=', '=', '==', '===', '>',
                  '>=', '>>', '>>=', '>>>', '>>>=', '?', '[', ']', '^', '^=', '{', '|', '|=', '||', '}', '~']
    words = []
    count = {}
    words = lines.split()
    print(words)
    for token in token_list:
        count[token] = words.count(token)
            # print(w)
                 # counting the number of matching tokens
    print(count)


def unique_keywords(lines):
    keyword_list = ['break', 'case', 'catch', 'continue', 'debugger', 'default', 'delete', 'do', 'else', 'finally',
                   'for', 'function', 'if', 'in', 'instanceof', 'new', 'return', 'switch', 'this', 'throw', 'try',
                   'typeof', 'var', 'void', 'while', 'with']

    count = {}
    words = []
    result = []
    words = lines.split()
    len_of_file = len(words)
    print("the length of the file is: ", len_of_file)
    print(words)
    for word in words:
        for key_word in keyword_list:
            if key_word in word:
                result.append(key_word)
    unique_words = set(result)
    print(unique_words)
    print(len(unique_words))

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
    print("line:", count)
    print(len(lines))

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

def whitespace_check():
    result = []
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', 'r').readlines()
    print(lines)
    for line in lines:
        if re.match(r"[0-9A-Za-z_]", line):
            result.append('non-whitespace')
            return True
        if re.match(r'[^0-9A-Za-z_]', line):
            result.append('whitespace')
            return False

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
    print(c)

def empty_line():
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', 'r').readlines()
    print(lines)
    count = 0
    for line in lines:
        if re.match(r"\n", line):
            count += 1
    print(count)

def main():
    # dir = input("Enter the directory of the file: ")
    len_of_file = 0
    mode = 'r' # specify the a mode
    lines = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', mode).read()  # Open file on read mode and reading the entire file
    # getting the length of the file
    for element in lines:
        len_of_file += len(element)
    print(len_of_file)
    lines = re.sub(r"[^a-zA-Z0-9-(!=#%$&{<(?}*;:/>|)]+", " ", lines) # spacing the elements
    # jsToCsv(dir)
    # word_unigram(lines)
    # keyword_count(lines)
    # line_average()
    # unique_keywords(lines)
    # token_count(lines)
    # comment_count(lines)
    start_line()
    # empty_line()
    # whitespace_check()
    # lines.close()  # Close file

if __name__ == '__main__':
    main()
