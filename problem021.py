"""
Project Euler
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import numpy as np

def proper_divisors(n):
    div = [1]
    for i in range(2, int(np.sqrt(n))+1):
        if n%i == 0:
            div.append(i)
            if i*i != n:
                div.append(int(n/i))
        
    return div

amicables = []
dictionary = {}

for a in range(2,10000):
    b = sum(proper_divisors(a))
    a2 = sum(proper_divisors(b))

    if a2 == a and a != b:
        amicables.append(a)
        amicables.append(b)

amicables = set(amicables)

print(sum(amicables))