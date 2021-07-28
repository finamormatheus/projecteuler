"""
Project Euler
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

import numpy as np

numb = str(np.math.factorial(100))

sum = 0

for i in range(len(numb)):
    sum += int(numb[i])

print(sum)