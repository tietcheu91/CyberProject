"""
Created on Thurs May 12 3.09 PM

@author: James Tietcheu

"""
import re
import csv
import sys
import os
import glob
from csv import reader

def wordUnigram():

    count = {}
    words = []
    mode ='r'
    f = open('/Users/jamestietcheu/Downloads/tutoring/Hw7/player.js', mode)  # Open file on read mode
    lines = f.read()
    lines = re.sub(r"[^a-zA-Z0-9]+"," ", lines)  # Create a list containing all lines
    words = lines.split()
    print(words)
    for w in words:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1
    print(len(count.keys()))
    # for word, times in count.items():
    #     print("%s was found %d times" % (word, times))
    f.close()  # Close file
    

def main():
    # dir = input("Enter the directory of the file: ")
    # jsToCsv(dir)
    wordUnigram()

if __name__ == '__main__':
    main()
