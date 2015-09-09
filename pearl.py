__author__ = 'Egbert'

from sort import merge_pairs, sortVanGrootNaarKlein
from ordsearch import binary_pairs,linearPairs
from search import linear
from util import words
from dup import remove_dups

def make_table(pairs):
    sortedPairs = merge_pairs(pairs)    #sorteer eerst de binnengekomen data
    pairs = remove_dups_pairs(sortedPairs)  #Verwijder daarna de duplicaten

    res = []    #init de resultaat array
    woordInDezeTextFiles = []   #init de array om de textfiles in te zetten
    fresh = ""

    if len(pairs) != 0:
        fresh = pairs[0][0] #set het te zoeken woord op de eerste van de data
        woordInDezeTextFiles.append(pairs[0][1])    #voeg de textfile name dan ook direct toe
        i = 1   #En zet i op 1 want je hebt de eerste al gehad

        while i < len(pairs):
            if pairs[i][0] == fresh:
                woordInDezeTextFiles.append(pairs[i][1]) #als het woord om te zoeken hetzelfde is, voeg de textfile name dan toe aan de array
            else:
                res.append([fresh,woordInDezeTextFiles]) #Er komt een nieuw woord => zet de te zoeken woord en de textfile names in de resultaat array
                woordInDezeTextFiles = []   #Reset de textfiles namen array

                fresh = pairs[i][0] #Set het nieuwe te zoeken woord
                woordInDezeTextFiles.append(pairs[i][1])    #En voeg de naam van de textfile toe aan de array
            i += 1

        res.append([fresh,woordInDezeTextFiles]) #Alles is nu geweest, voeg het laatste woord + textfiles nog toe
    return res

def make_counted_table(data):
    pairs = merge_pairs(data) #Sorteer eerst de binnengekomen data

    res = []    #init the resultaat array
    zelfdeWoordAndereBestand = []   #init array om de count in te zetten
    fresh = ""

    if len(pairs) != 0:
        fresh = pairs[0][0] #zet het eerste woord waar we naar gaan kijken
        currentTextFile = pairs[0][1]; #zet het textfile naam waar het eerste woord in voor komt
        countForHowManyInTextFile = 1;  #zet de count op 1 omdat we het eerste woord zelf hebben neergezet

        i = 1   #set i op 1 omdat we de eerste woord handmatig hebben gedaan

        while i < len(pairs):   #ga door tot het eind
            if pairs[i][0] == fresh:
                if pairs[i][1] == currentTextFile:
                    countForHowManyInTextFile += 1 #Als het woord het zelfde is, en je zit nog in hetzelfde bestand, doe de counter +1
                else:
                    zelfdeWoordAndereBestand.append([currentTextFile,countForHowManyInTextFile]) #Als we niet meer in hetzelfde textbestand zitten zetten we de counter in de array, om later te sorteren
                    currentTextFile = pairs[i][1]   #set de huidige textfile naam
                    countForHowManyInTextFile = 1   #Doe de counter op 1, omdat we hem handmatig hebben ingesteld

            else:
                if len(zelfdeWoordAndereBestand) == 0:
                    #woord is 1 keer voorgekomen in 1 tekstbestand
                    zelfdeWoordAndereBestand.append([currentTextFile,countForHowManyInTextFile])

                zelfdeWoordAndereBestand = sortVanGrootNaarKlein(zelfdeWoordAndereBestand) #er komt een nieuw woord aan bod, dus sorteer de count-array van het laatste woord

                res.append([fresh,zelfdeWoordAndereBestand]) #Voeg deze lijst toe aan de resultaat array
                zelfdeWoordAndereBestand = []   #reset de array voor de counters

                fresh = pairs[i][0] #Set het nieuwe zoekwoord
                currentTextFile = pairs[0][1];  #En het textbestand waar we nu in zoeken
                countForHowManyInTextFile = 1;  #En zet de counter op 1 omdat we hem zelf al hebben gecount

            i += 1

        #Omdat alle woorden nu zijn geweest zitten we aan onze maximale lengte, maar het laatste woord moet nog wel aan de array toegevoegt worden:
        zelfdeWoordAndereBestand = sortVanGrootNaarKlein(zelfdeWoordAndereBestand)
        res.append([fresh,zelfdeWoordAndereBestand])
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
                if len(zelfdeWoordAndereBestand) == 0:
                    #woord is 1 keer voorgekomen in 1 tekstbestand
                    gestorteerdeLijst = merge_pairs(woordenPerFile)
                    indexOfTextFile = linearPairs(gestorteerdeLijst, currentTextFile)

                    if indexOfTextFile != -1:
                        totalWordCount = woordenPerFile[indexOfTextFile][1]
                    else:
                        totalWordCount = len(words(currentTextFile))
                        woordenPerFile.append([currentTextFile, totalWordCount])
                    freq = countForHowManyInTextFile / totalWordCount
                    zelfdeWoordAndereBestand.append([currentTextFile, freq])


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