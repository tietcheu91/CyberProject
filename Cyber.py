"""
Created on Thurs May 12 3.09 PM

@author: James Tietcheu

"""

import sys
import os
import csv, pathlib
class WebsiteCheck:

    #def __init__(s):
    def accessFile(row):
        user_input = input("Enter the path of your file: ")

        for path in pathlib.Path(user_input).glob("*.js"):
            with path.open() as jsfile, path.with_suffix(".csv").open(mode="w") as csvfile:
                reader = csv.reader(jsfile, delimiter='}')
                writer = csv.writer(csvfile)

                for row in reader:
                    writer.writerow(row)
                    #print(row)
        return row
        '''assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
        f = open(user_input,'r+')
        print("Your file was found!")
        # stuff you do with the file goes here
        f.close()'''

    def wordUnigram(row):
        count = {}
        for w in row.read().split(" "):
            if w in count:
                count[w] += 1
            else:
                count[w] = 1
        for word, times in count.items():
            print ("%s was found %d times" % (word, times))

if __name__ == '__main__':

    my_website = WebsiteCheck()
    my_website.accessFile()
    my_website.wordUnigram()