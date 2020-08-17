''' Longest Collatz sequence
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def find_count_of_number(number):
    n = number
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            count += 1
        else:
            n = 3 * n + 1
            count += 1
    return count

number = 13
big_number = 13
big_count = 10

while number < 1000000:
    count_res = find_count_of_number(number)
    if big_count < count_res:
        big_count = count_res
        big_number = number
    number += 1

print(f'{big_number = }, {big_count = }')