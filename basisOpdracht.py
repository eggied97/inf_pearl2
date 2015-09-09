__author__ = 'Egbert'

from util import all_word_pairs
from sort import merge_pairs
from pearl import remove_dups_pairs, make_counted_table, make_density_table

#print(all_word_pairs())

#eerst sorteer

#print(sortedPairs)
#nu alle dublicaten weg flikkeren

#print(make_counted_table(all_word_pairs())) #eerste bonuspunt
print(make_density_table(all_word_pairs())) #tweede bonuspujnt

#make_density_table(all_word_pairs())
