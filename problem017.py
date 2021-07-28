"""
Project Euler
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

algarisms = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

sum_letters = 0

# From 1 to 19:

for i in range(1, len(algarisms)):
    sum_letters += len(algarisms[i])

for i in range(len(teens)):
    sum_letters += len(teens[i])

# From 20 to 99:

for i in range(20, 100):
    numb = str(i)
    
    ten = int(numb[0])
    alg = int(numb[1])

    if alg != 0:
        numb = tens[ten-2] + algarisms[alg]
    else:
        numb = tens[ten-2]

    sum_letters += len(numb)

# From 100 to 999:

for i in range(100, 1000):
    numb = str(i)

    hundred = int(numb[0])
    ten = int(numb[1])
    alg = int(numb[2])

    if alg == 0 and ten == 0:
        numb = algarisms[hundred] + 'hundred'
    elif ten == 0:
        numb = algarisms[hundred] + 'hundredand' + algarisms[alg]
    elif ten == 1:
        numb = algarisms[hundred] + 'hundredand' + teens[alg]
    elif alg !=0:
        numb = algarisms[hundred] + 'hundredand' + tens[ten-2] + algarisms[alg]
    else:
        numb = algarisms[hundred] + 'hundredand' + tens[ten-2]

    sum_letters += len(numb)

# 1000:

sum_letters += len('onethousand')

print(sum_letters)