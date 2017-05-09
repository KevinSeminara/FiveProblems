#!/usr/bin/python

print "Hello p1!"

numbers = [1, 2, 3, 5]
total = 0
counter = 0

# for loop
for num in numbers:
    total = num + total
print total

total = 0

# while loop
while counter < len(numbers):
    total = total + numbers[counter]
    counter += 1
print total

total = 0


# recursion
def sum_digits(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[-1] + sum_digits(numbers[:-1])

print sum_digits(numbers)