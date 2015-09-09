__author__ = 'Egbert'

from sort import merge_pairs, sortVanGrootNaarKlein
from ordsearch import binary_pairs
from search import linear
from util import words
from dup import remove_dups

def make_table(pairs):
    sortedPairs = merge_pairs(pairs)
    withoutDuplicates = remove_dups_pairs(sortedPairs)

    pairs = withoutDuplicates

    res = []
    zelfdeWoordAndereBestand = []
    fresh = ""

    if len(pairs) != 0:
        fresh = pairs[0][0]
        zelfdeWoordAndereBestand.append(pairs[0][1])
        i = 1

        while len(pairs) > i:
            if pairs[i][0] == fresh:
                zelfdeWoordAndereBestand.append(pairs[i][1])
            else:
                res.append([fresh,zelfdeWoordAndereBestand])
                zelfdeWoordAndereBestand = []

                fresh = pairs[i][0]
                zelfdeWoordAndereBestand.append(pairs[i][1])
            i += 1
        res.append(fresh)
    return res

def make_counted_table(data):
    sortedPairs = merge_pairs(data)

    pairs = sortedPairs

    res = []
    zelfdeWoordAndereBestand = []
    fresh = ""

    if len(pairs) != 0:
        fresh = pairs[0][0]
        i = 1

        currentTextFile = pairs[0][1];
        countForHowManyInTextFile = 1;

        while len(pairs) > i:
            if pairs[i][0] == fresh:
                if pairs[i][1] == currentTextFile:
                    countForHowManyInTextFile += 1
                else:
                    zelfdeWoordAndereBestand.append([currentTextFile,countForHowManyInTextFile])
                    currentTextFile = pairs[i][1]
                    countForHowManyInTextFile = 1

            else:
                #sorteer zelfdeWoordAnderBestand op de i=1
                zelfdeWoordAndereBestand = sortVanGrootNaarKlein(zelfdeWoordAndereBestand)

                res.append([fresh,zelfdeWoordAndereBestand])
                zelfdeWoordAndereBestand = []

                fresh = pairs[i][0]
                currentTextFile = pairs[0][1];
                countForHowManyInTextFile = 1;

            i += 1
        res.append(fresh)
    return res

def make_density_table(data):
    woordenPerFile = [] # [["Brian.txt",17562],["huppel.txt",127547]]

    sortedPairs = merge_pairs(data)

    pairs = sortedPairs

    res = []
    zelfdeWoordAndereBestand = []
    fresh = ""

    if len(pairs) != 0:
        fresh = pairs[0][0]
        i = 1

        currentTextFile = pairs[0][1];
        countForHowManyInTextFile = 1;

        while len(pairs) > i:
            if pairs[i][0] == fresh:
                if pairs[i][1] == currentTextFile:
                    countForHowManyInTextFile += 1
                else:
                    #check if we already have the wordCount in our Array
                    indexOfTextFile = binary_pairs(merge_pairs(woordenPerFile), pairs[i][1])

                    if indexOfTextFile != -1:
                        totalWordCount = woordenPerFile[indexOfTextFile][1]
                    else:
                        totalWordCount = len(words(pairs[i][1]))
                        woordenPerFile.append([pairs[i][1], totalWordCount])


                    freq = countForHowManyInTextFile / totalWordCount

                    zelfdeWoordAndereBestand.append([currentTextFile, freq])
                    currentTextFile = pairs[i][1]
                    countForHowManyInTextFile = 1

            else:
                #sorteer zelfdeWoordAnderBestand op de i=1
                zelfdeWoordAndereBestand = sortVanGrootNaarKlein(zelfdeWoordAndereBestand)

                res.append([fresh,zelfdeWoordAndereBestand])

                zelfdeWoordAndereBestand = []
                fresh = pairs[i][0]
                currentTextFile = pairs[0][1];
                countForHowManyInTextFile = 1;

            i += 1
        res.append(fresh)


    return res


def remove_dups_pairs(data):
    res = []

    if len(data) != 0:
        fresh = data[0]
        i = 1

        while len(data) > i:
            if data[i] != fresh:
                res.append(fresh)
                fresh = data[i]
            i += 1
        res.append(fresh)
    return res