''' Sum square difference

The sum of the squares of the first ten natural numbers is 385
The square of the sum of the first ten natural numbers is 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640
Find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum.
'''

# brute force implementation

# sum_of_sqr = 0
# sum = 0
#
# for i in range (1,101):
#     sum_of_sqr += i**2
#     sum += i
#
# resalt = sum**2 - sum_of_sqr
# print(resalt)


# solving the problem using the formula

limit = 100

sum = limit * (limit + 1) / 2
print (sum)

sum_sq = (2* limit + 1) * (limit + 1) * limit / 6 #
print(sum_sq)
print (sum ** 2 - sum_sq)
