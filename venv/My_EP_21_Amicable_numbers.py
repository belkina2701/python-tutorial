''' Amicable numbers - Problem 21
INPUT:
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair
and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.

OUTPUT: 31626
'''

n = 10000
res = 0

for a in range(1,n+1):
    array_a = []
    midle_a = a // 2 # max divisor = 1/2 of number
    d_a = 0 # sum of proper divisors of a (numbers less than n which divide evenly into a)

    for div in range(1, midle_a + 1):
        if a % div == 0:
            array_a.append(div)
            d_a += div
    # print(f'{a} - {array_a} - {d_a = }')

    if d_a != 1 and d_a <= n: # if == 1 it is simple number
        b = d_a
        array_b = []
        midle_b = b // 2
        d_b = 0
        for div in range(1, midle_b + 1):
            if b % div == 0:
                array_b.append(div)
                d_b += div
    if a == d_b and b == d_a:
        if a != b:
            print(f'{a} - {array_a} - {d_a = }')
            print(f'{b} - {array_b} - {d_b = }')
            res = d_a + d_b + res

print(res / 2)

