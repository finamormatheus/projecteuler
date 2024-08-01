"""
Project Euler
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

"""
In a long division process we repeat the process: get the rest, multiply by 10, divide by the denominator

Example: 

- 1/7: 0 rest 1
- 1*10/7: 1 rest 3
- 3*10/7: 4 rest 2
- 2*10/7: 2 rest 6
- 6*10/7: 8 rest 4
- 4*10/7: 5 rest 5
- 5*10/7: 7 rest 1
- 1*10/7: 1 rest 3

The digits are the quotients: 0.142857...

Note that, when the rest repeats it's when the cycle restarts.

Therefore, the solution to our problem is to get 10*rest%d and note when it starts to repeat: indicating the length of our cycle
"""

def is_regular_fraction(denominator):    
    # Check factors of the denominator
    while denominator % 2 == 0:
        denominator //= 2
    while denominator % 5 == 0:
        denominator //= 5
    
    # If the remaining denominator is 1, it's regular
    # Otherwise, it's irregular
    return denominator == 1

def cycle_length(d):
    rests = {}

    position = 0
    value = 1
    while value not in rests:
        rests[value] = position

        value = (value * 10)%d

        position += 1

    return position - rests[value]

cycle_len_dict = {}
for d in range(2, 1000):
    # Skip regular fractions
    if is_regular_fraction(d):
        continue

    cycle_len_dict[d] = cycle_length(d)

max_d, max_cycle_len = max(cycle_len_dict.items(), key=lambda x: x[1])

print(f"Answer: {max_d}")
print(f"Cycle length: {max_cycle_len}")
