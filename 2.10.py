__author__ = 'Egbert'

from ordsearch import binary
from ordsearch import linear
from util import lines
import searchmeasure


print(binary(lines("Unabr.dict"),"eagle"))
print(binary(lines("Unabr.dict"),"zygose"))

searchmeasure.search("Unabr.dict","eagle")