"""
Project Euler
Problem 27

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39. However, when n = 40, the solution is divisible by 41, and certainly, when n = 41, the solution is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n, e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check up to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

solution_dict = {}

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        solution = 2 
        while is_prime(solution):
            solution = n**2 + a*n + b
            n += 1

        consecutive_primes = n-1

        solution_dict[consecutive_primes] = (a, b)

max_consecutive_primes = max(solution_dict)
max_a, max_b = solution_dict[max_consecutive_primes]

print(f"""
Number of consecutive primes: {max_consecutive_primes}
a = {max_a}
b = {max_b}
a*b = {max_a*max_b}
""")