''' Power digit sum
Problem 16

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?
'''

number = pow(2, 1000)
number_str = str(number)
sum = 0

for i in number_str:
    sum += int(i)

print(sum)