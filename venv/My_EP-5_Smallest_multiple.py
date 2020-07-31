''' Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

num = 2520
i = 1

while i <= 20:
    i += 1
    if num % i != 0:
        num += 1
        i = 1

    if i == 20:
        break
print(num)





