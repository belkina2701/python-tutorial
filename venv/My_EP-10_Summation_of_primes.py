''' Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
prime_array = [2,3,5,7]
next_numero = 11
big_number = 2000000

def is_prime_numero(next_numero, prime_array):
    prime_numero = next_numero
    for i in prime_array:
        if next_numero % i == 0:
            prime_numero = False
            break
    return prime_numero

# print(is_prime_numero(14, prime_array))

while next_numero < big_number:
    prime_numero = is_prime_numero(next_numero, prime_array)
    if prime_numero is not False:
        prime_array.append(prime_numero)
    next_numero += 2

print(sum(prime_array))

