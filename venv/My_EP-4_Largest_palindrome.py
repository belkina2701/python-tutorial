''' Largest palindrome product
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

num_1 = 1000
num_2 = 1000
palindome = []

while num_1 >= 100:
    while num_1 >= 100:
        resalt = num_1 * num_2
        resalt_str = str(resalt)
        num_1 -= 1
        if resalt_str == resalt_str[::-1]:
            palindome.append(resalt)
    num_2 -= 1
    num_1 = num_2

print(palindome)
print(max(palindome))