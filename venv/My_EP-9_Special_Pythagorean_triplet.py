''' Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

pythagorean_triple = [(3,4,5), (5,12,13), (8,15,17), (7,24,25)]
sum_pythagorean_triple = []

for triple in pythagorean_triple:
    sum = 0
    for prime_number in triple:
        sum += prime_number
    if 1000 % sum == 0:
        coefficient = 1000 / sum
        print(coefficient)
        print(triple)
        break
resalt = 1

for number in triple:
    resalt = resalt * (number * coefficient)

print(resalt)

