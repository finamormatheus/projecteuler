"""
Project Euler
Problem 13

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

Number in .txt file
"""

with open('problem013.txt', 'r') as inp:
    k = 0

    for line in inp:
        k += int(line)

print(k)
print(str(k)[0:10])


