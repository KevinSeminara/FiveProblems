#!/usr/bin/python

import itertools

print "Hello Problem 4"

input = [420, 34, 19, 71, 341]

perm = list(itertools.permutations(input))
finalperm = []

for each in perm:
    s = map(str, each)
    s = ''.join(s)
    s = int(s)
    finalperm.append(s)

finalperm.sort()

print "Smallest number is: %d" % finalperm[0]
print "Largest number is: %d" % finalperm[-1]


