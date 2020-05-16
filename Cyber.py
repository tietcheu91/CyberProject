"""
Created on Thurs May 12 3.09 PM

@author: James Tietcheu

"""
import csv
import sys
import os
import glob
from csv import reader

def jsToCsv(dir):
    print("File extension changed from .js to .csv")
    for dirpath, dirs, files in os.walk(dir):
        #print(f"File with .js extension {file_path} changed to", end="")
        for filename in glob(os.path.join(dirpath, "*.js")):
                print(filename)
                try:
                    pre, ext = os.path.splitext(filename)
                    print(f"File with .csv extension  {pre + '.csv'}")
                    dir_path = os.path.join(dir, pre + '.csv')
                    print(dir_path)
                except Exception as e:
                    print(e)

def main():
    dir = input("Enter the directory of the file: ")
    jsToCsv(dir)
    wordUnigram(dir)


def wordUnigram(dir):

    count = {}
    for root, dirs, files in os.walk(dir):
        for file in files:
            print(file)
            if file.endswith(".csv"):
                with open(file, 'r') as csvfile:
                    reader = csv.reader(csvfile)
                    rows = [row for row in reader]
                    print(rows)

                # for w in line:
                #     if w in count:
                #         count[w] += 1
                #     else:
                #         count[w] = 1
                #     for word, times in count.items():
                #         print("%s was found %d times" % (word, times))
                #         os.path.join(path, filename)


if __name__ == '__main__':
    main()
