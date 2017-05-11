sentence = "Here is a test sentence"

letter = raw_input('letter to count> ')
letterdict = {}

for each in sentence:
    if each in letterdict:
        letterdict[each] += 1
    else:
        letterdict[each] = 1

print letterdict.get(letter)

print "Most repeated character was: %s - %d" % (max(letterdict, key=letterdict.get), letterdict.get(max(letterdict, key=letterdict.get)))



