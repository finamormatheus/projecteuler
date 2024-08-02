"""
Project Euler
Problem 31

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can £2 be made using any number of coins?
"""

# Dynamic programming:
def count_coin_combinations(target, coins):
    # Initialize an array to store the number of ways to make each amount
    ways = [0] * (target + 1)
    ways[0] = 1  # There's one way to make 0: use no coins

    # For each coin, update the ways array
    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

# Define the coin denominations
coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200  # 200p = £2

result = count_coin_combinations(target, coins)
print(f"Different ways we can make £2 with coins: {result}")

# Recursion:
def count_coin_combinations(target, coins, index=0):
    # Base cases
    if target == 0:
        return 1
    if target < 0 or index >= len(coins):
        return 0

    # Recursive cases
    # 1. Include the current coin
    include = count_coin_combinations(target - coins[index], coins, index)
    
    # 2. Exclude the current coin
    exclude = count_coin_combinations(target, coins, index + 1)

    # Return the sum of combinations
    return include + exclude

# Define the coin denominations
coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200  # 200p = £2

result = count_coin_combinations(target, coins)
print(f"Different ways we can make £2 with coins: {result}")