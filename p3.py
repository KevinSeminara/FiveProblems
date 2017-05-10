#!/usr/bin/python

print "Hello p3"

fib = [0, 1]
counter = 0

while counter < 100:
    fib.append(fib[-1] + fib[-2])
    counter += 1

print fib