__author__ = 'Egbert'

from dup import remove_dups
from util import words


print("hacktest.txt bevat {} woorden".format(len(remove_dups(words("hacktest.txt")))))
print("Grail.txt bevat {} woorden".format(len(remove_dups(words("grail.txt")))))