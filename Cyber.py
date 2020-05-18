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
    len_of_file = len(words)
    print("the length of the file is: ", len_of_file)
    print(words)
    for w in words:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1
    print(len(count.keys()))
    # for word, times in count.items():
    #     print("%s was found %d times" % (word, times))


def keyword_count(lines):
    keywordList = ['break', 'case', 'catch', 'continue', 'debugger', 'default', 'delete', 'do', 'else', 'finally',
                   'for', 'function', 'if', 'in', 'instanceof', 'new', 'return', 'switch', 'this', 'throw', 'try',
                   'typeof', 'var', 'void', 'while', 'with']
    count = {}
    words = []
    c = 0
    words = lines.split()
    len_of_file = len(words)
    print("the length of the file is: ", len_of_file)
    # print(words)
    for w in words:
        if w in keywordList:
            # print(w)
            c += 1      # counting the number of occurrences of keywords
    print(c)
    print(c/len_of_file)

def token_count(lines):
    token_list = ['!', '!=', '!==', '%', '%=', '&', '&&', '&=', '(', ')', '*', '*=', '+', '++', '+=', ',', '-', '--',
                  '-=', '.', '..', '...', '/', '/=', ':', '::', ';', '<', '<<', '<<=', '<=', '=', '==', '===', '>',
                  '>=', '>>', '>>=', '>>>', '>>>=', '?', '[', ']', '^', '^=', '{', '|', '|=', '||', '}', '~']
    words = []
    c = 0
    words = lines.split()
    len_of_file = len(words)
    print("the length of the file is: ", len_of_file)
    print(words)
    for w in words:
        if w in token_list:
            # print(w)
            c += 1      # counting the number of matching tokens
    print(c)
    print(c/len_of_file)


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
            if key_word == word:
                result.append(key_word)
    unique_words = set(result)
    print(len(unique_words))



def main():
    # dir = input("Enter the directory of the file: ")
    mode = 'r' # specify the a mode
    f = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', mode)  # Open file on read mode
    lines = f.read() # reading the entire file
    lines = re.sub(r"[^a-zA-Z0-9(){}!=%&*+,-./:<>?|;~]+", " ", lines) # spacing the elements
    # jsToCsv(dir)
    # word_unigram(lines)
    # keyword_count(lines)
    unique_keywords(lines)
    # token_count(lines)
    f.close()  # Close file

if __name__ == '__main__':
    main()
