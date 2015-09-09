"""
Command-line script to invoke and profile linear and binary search

Usage: 'measure dict-file'
Pearls of Computer Science, Week 2
"""

# standard module to access command-line parameter list sys.argv
import sys
# standard module containing clock function
import time

from ordsearch import linear
from ordsearch import binary

# read words from dictionary file
import util

def search(dict, value):
    words = util.lines(dict)

    # ask for the first word
    #value = input("Search for first word? ")
    print("---------- searching for {} ----------".format(value))
    # continue as long as a word was typed
    while value != "":
        # measure time for linear searching
        lstart = time.clock(); lresult = linear(words, value); lend = time.clock()
        # clock values are fractions of seconds;
        # multiply by a million and round to get microseconds
        ltime = round((lend - lstart) * 1000000)

        # measure time for binary searching
        bstart = time.clock(); bresult = binary(words, value); bend = time.clock()
        # clock values are fractions of seconds;
        # multiply by a million and round to get microseconds
        btime = round((bend - bstart) * 1000000)

        # print the outcome
        if (lresult != bresult):
            print("results for linear and binary differ: {} versus {}".format(lresult, bresult))
        elif (lresult < 0):
            print("'{}' does not occur".format(value))
        else:
            print("'{}' occurs at position {}".format(value, lresult))
        # print the measured time
        print("linear search took {} micros to complete".format(ltime))
        print("binary search took {} micros to complete".format(btime))

        # ask for the next word
        value = input("\nSearch for next word? ")
