''' Large sum
Problem 13
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers
'''

sum = 0

with open('file_number.txt', mode='r') as file_number:
    num = file_number.read()
    x = 0
    y = 50
    while y <= 5100:
        i = num[x:y]
        sum += int(i)
        x = y + 1
        y = y + 51
        print(f'i = {i}')
        print(sum)