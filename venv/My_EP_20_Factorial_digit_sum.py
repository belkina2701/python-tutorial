''' Factorial digit sum - Problem 20
INPUT: Find the sum of the digits in the number 100!

OUTPUT: 648

'''

factorial = 1

for i in range(2,101):
    factorial *= i

summa = 0

for num in str(factorial):
    summa += int(num)

print(summa)