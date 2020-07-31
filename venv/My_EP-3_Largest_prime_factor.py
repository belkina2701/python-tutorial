''' Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

import math

array = []
numero = int(input())  # numero = 600851475143

def find_prime(numero):
    i = 2
    while i <= int(math.sqrt(numero)):
        if numero % i == 0:
            return i, numero / i
        i = i + 1
    return int(numero), 1

while (numero != 1):
    prime_numero, numero = find_prime(numero)
    array.append(prime_numero)
print(array)
print(max(array))