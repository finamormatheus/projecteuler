"""
Project Euler
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

# Thinking going down as 1 and going down as 0.
# The problem for 2x2 grid stands for calculating all the possible permutations for: 1100
# Which is calculated by: 4!/(2!)²
# So, we only need to calculate: (20*2)!/(20!)²

import numpy as np

grid_size = 20

print(np.math.factorial(grid_size*2)/(np.math.factorial(grid_size))**2)