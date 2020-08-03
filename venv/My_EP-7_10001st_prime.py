''' 10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

def find_prime_num (next_number, prime_number):
    for i in prime_number:
        if next_number % i == 0:
            return False
        else:
            res = next_number
    return res

# print(find_prime_num(101,[2,3,5,7,11,13]))

prime_number = [2,3,5,7,11,13]
n = 6
next_number = 15

while n <= 10000:
    a = find_prime_num(next_number,prime_number)
    if a == False:
        next_number += 2
    else:
        prime_number.append(a)
        n += 1

print(prime_number[-1])
print(n)

