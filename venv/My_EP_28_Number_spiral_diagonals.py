''' Number spiral diagonals - Problem 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

cycle = 5 # started od cycle 5
summa = 101
number = 25
difference = 4

while cycle < 1001:
    cycle += 2
    difference += 2
    number += difference # 1
    summa += number
    number += difference # 2
    summa += number
    number += difference # 3
    summa += number
    number += difference # 4
    summa += number

print(summa)