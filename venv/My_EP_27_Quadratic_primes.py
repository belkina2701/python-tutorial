''' Quadratic primes
INPUT:  https://projecteuler.net/problem=27

# Euler discovered the remarkable quadratic formula:
# n ** n + n + 41 = primes numbers

primes = []
for n in range(0,39):
    res = n**2 + n + 41
    primes.append(res)
print(primes)
# [41, 43, 47, 53, 61, 71, 83, 97, 113, 131, 151, 173, 197, 223, 251,
# 281, 313, 347, 383, 421, 461, 503, 547, 593, 641, 691, 743, 797, 853,
# 911, 971, 1033, 1097, 1163, 1231, 1301, 1373, 1447, 1523]

primes_2 = []
for n in range(0,80):
    res = n**2 - 79 * n + 1601
    primes_2.append(res)
print(primes_2)
# [1601, 1523, 1447, 1373, 1301, 1231, 1163, 1097, 1033, 971, 911, 853, 797, 743, 691, 641, 593,
# 547, 503, 461, 421, 383, 347, 313, 281, 251, 223, 197, 173, 151, 131, 113, 97, 83, 71, 61, 53,
# 47, 43, 41, 41, 43, 47, 53, 61, 71, 83, 97, 113, 131, 151, 173, 197, 223, 251, 281, 313, 347,
# 383, 421, 461, 503, 547, 593, 641, 691, 743, 797, 853, 911, 971, 1033, 1097, 1163, 1231, 1301,
# 1373, 1447, 1523, 1601]
print(79*1601) # 126479

# Considering quadratics of the form:
# n ** 2 + a * n  + b where a < 1000 and b <= 1000
# where n is the modulus/absolute value of n
'''

def is_prime_number(number):
    midle_number = number // 2
    sum_number = 1
    for div in range(2, midle_number + 1):
        if number % div == 0:
            sum_number += div
    if sum_number == 1:
        return True
    else:
        return False

# Function for counting consecutive Prime numbers using the formula:
# number = n ** 2 + a * n + b  >>> res = 41, count = 40
# number = n ** 2 - a * n + b  >>> res = 59231, count = 71
# number = n ** 2 - a * n - b  >>> res = 361, count = 38
# number = n ** 2 + a * n - b  >>> res = 108, count = 28

def count_prime_numbers(a, b, n):
    number = n ** 2 - a * n + b
    number = abs(number)
    # print(f'{a = } {b = } = {number} , {n = }')
    is_prime = is_prime_number(number)
    # print(is_prime)
    if is_prime == True:
        n += 1
        n = count_prime_numbers(a,b,n)
    return n


a = 0
b = 0
last_count = 0

while a < 1000:
    n = 0
    count = count_prime_numbers(a,b,n)
    # print(f'{a = }, {b = }, {count = }')
    if count > last_count:
        last_count = count
        res = a * b
        print(f'RES = {count}  {a} * {b}')
    b += 1
    if b > 1001:
        a += 1
        b = 0

print(f'{res = }, {last_count = }')