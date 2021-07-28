"""
Project Euler
Problem 22

Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import urllib.request

url = "https://projecteuler.net/project/resources/p022_names.txt"

file = urllib.request.urlopen(url)

for line in file:
    line = line.decode("utf-8")
    names = line.split("\",\"")

names[0] = names[0][1:]
names[len(names)-1] = names[len(names)-1][:-1]

names = sorted(names)

total = 0
for i in range(len(names)):
    sum_char = 0
    for j in range(len(names[i])):
        sum_char += ord(names[i][j]) - 64

    total += sum_char*(i+1)

print(total)
