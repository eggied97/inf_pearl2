__author__ = 'Egbert'

import ordsearch

print(ordsearch.linear([1,2,3,4,5,6,7,8,9,10], 4))
print(ordsearch.linear([1,2,3,5,6,7,8,9,10], 11)) #zit de 4 niet in
print(ordsearch.linear([3,1,7,4,6,1,4,6,7], 4)) #niet geordent
#print(ordsearch.linear([1,2,3,"vier",5,6,7,8],9))

print("------------ BINARY SEARCH --------------")

print(ordsearch.binary([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 4))

