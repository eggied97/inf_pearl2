__author__ = 'Egbert'

from sort import merge_pairs, sortVanGrootNaarKlein
from ordsearch import binary_pairs,linearPairs
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

        while i < len(pairs):
            if pairs[i][0] == fresh:    #Als woord is gelijk aan het te vergelijkenwoord
                if pairs[i][1] == currentTextFile:  #als die uit het zelfde bestand komt counter 1 omhoog
                    countForHowManyInTextFile += 1
                else:
                    #check if we already have the wordCount in our Array

                    gestorteerdeLijst = merge_pairs(woordenPerFile) #sorteer eerst de lijst van woorden met het totaal aantal woorden
                    indexOfTextFile = linearPairs(gestorteerdeLijst, currentTextFile)   #zoek dan de index van het huidige textbestand

                    if indexOfTextFile != -1:
                        totalWordCount = woordenPerFile[indexOfTextFile][1] #als deze niet -1 is kunnen we hem gewoon opvragen
                    else:
                        totalWordCount = len(words(currentTextFile))    #als hij -1 is, kijk wat het totaal aantal woorden is
                        woordenPerFile.append([currentTextFile, totalWordCount])    #en zet deze in de array


                    freq = countForHowManyInTextFile / totalWordCount   #bereken de frequentie door de het getelde aantal woorden delen door het totaal aantal woorden

                    zelfdeWoordAndereBestand.append([currentTextFile, freq]) #En voeg deze vervolgens toe aan de array
                    currentTextFile = pairs[i][1]   #set de nieuwe huidige textfile, waar we nu in aan het zoeken zijn
                    countForHowManyInTextFile = 1   #En er is dus al 1 geteld, dus de counter begint op 1

            else:
                #Er is nu een nieuw woord gedetecteerd
                #Dus moeten we eerst de array van de tekstbestanden met de frequentie sorteren van groot naar klein
                zelfdeWoordAndereBestand = sortVanGrootNaarKlein(zelfdeWoordAndereBestand)


                res.append([fresh,zelfdeWoordAndereBestand])    #Vervolgens voegen wij het woord + de gesorteerde lijst met frequenties toe aan het resultaat

                zelfdeWoordAndereBestand = []   #We resetten deze array voor nieuwe frequenties
                fresh = pairs[i][0]             #Setten het nieuwe woord om naar te zoeken
                currentTextFile = pairs[i][1];  #Setten het nieuwe textbestand waarin we zoeken
                countForHowManyInTextFile = 1;  #Omdat hij nu al is gezien begint de counter op 1

            i += 1

        #einde van de rit, sorteer en voeg het laatste woord nog toe
        zelfdeWoordAndereBestand = sortVanGrootNaarKlein(zelfdeWoordAndereBestand)
        res.append([fresh,zelfdeWoordAndereBestand])

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