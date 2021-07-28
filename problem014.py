"""
Project Euler
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

# Functions
def next_numb(n):
    if n%2 == 0:
        return int(n/2)
    else:
        return int(3*n + 1)

def seq(starting_numb):
    # Only for testing
    chain = [starting_numb]

    while starting_numb != 1:
        n = next_numb(starting_numb)
        chain.append(n)
        starting_numb = n

    return chain

def seq_length(starting_numb):
    if starting_numb in dict:
        return dict[starting_numb]
    else:
        next = next_numb(starting_numb)
        if next in dict:
            length = dict[next]+1
        else:
            length = seq_length(next)+1
        
        dict[starting_numb] = length
        return length 


# Main
dict = {1: 1}

biggest_chain = 0
biggest_chain_starting = 0

for k in range(1,1000000):
    length = seq_length(k)

    if length > biggest_chain:
        biggest_chain = length
        biggest_chain_starting = k

print(biggest_chain_starting)
