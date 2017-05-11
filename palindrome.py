word = raw_input("input word> ")

word = word.lower()

if word == word[::-1]:
    print "True"
else:
    print "False"


