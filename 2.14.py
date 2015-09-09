__author__ = 'Egbert'

from sort import bubble
from sort import merge
from util import words
from ordsearch import binary

#print(bubble([3,253,223,52,6,23,6,2,6,8,3,5,34,8,3,433,76,83465,8,34,36,457,5478,3,45,2]))
#print(bubble(words("hacktest.txt")))
#print(bubble(words("Unabr.dict")))

#print(merge([3,253,223,52,6,23,6,2,6,8,3,5,34,8,3,433,76,83465,8,34,36,457,5478,3,45,2]))
#print(merge(words("hacktest.txt")))
#print(merge(words("Unabr.dict")))

print(binary(merge(words("grail.txt")),"swallow"))