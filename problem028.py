"""
Project Euler
Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
import numpy as np

spiral_len = 1001

num_spirals = int((spiral_len-1)/2) + 1

spiral = np.zeros([spiral_len, spiral_len])

start_row = int((spiral_len-1)/2)
start_col = int((spiral_len-1)/2)

spiral[start_row, start_col] = 1

size_spiral = 0

row = start_row
col = start_col

k = 2
for i in range(1,num_spirals):
    size_spiral += 8
    start_row = row   
    start_col = col 

    min_row = start_row + (2*i - 1)
    max_row = start_row - 1

    min_col = start_col - (2*i - 1)
    max_col = start_col + 1

    col += 1
    spiral[row, col] = k
    k += 1

    while row != min_row:
        row += 1
        spiral[row, col] = k
        k += 1
    while col != min_col:
        col -= 1
        spiral[row, col] = k
        k += 1
    while row != max_row:
        row -= 1
        spiral[row, col] = k
        k += 1
    while col != max_col:
        col += 1
        spiral[row, col] = k
        k += 1

main_diag_sum = np.diag(spiral).sum()
secondary_diag_sum = np.diag(np.fliplr(spiral)).sum()

print(f"""Length of the spiral: {spiral_len}
Sum of diagonals: {int(main_diag_sum + secondary_diag_sum - 1)}""")