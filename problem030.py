"""
Project Euler
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def get_digits(number):
    digits = [number%10]

    while number//10 != 0:
        number = number // 10
        digits.append(number%10)

    return digits[::-1]

# 6*9^5 = 354294, this means that the upper bound we can reach with 6 digits is 354294, 7-digits or more will never be possible

numbers_list = []
for number in range(2,354294):
    digits = get_digits(number)

    sum_power_5 = 0
    for num in digits:
        sum_power_5 += num**5

    if sum_power_5 == number:
        numbers_list.append(number)

print(f"""
List of numbers: {numbers_list}
Sum: {sum(numbers_list)}
""")