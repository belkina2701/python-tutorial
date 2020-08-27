'''Lexicographic permutations - Problem 24

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

OUTPUT: 2783915460
'''

# import itertools
#
# combinations = itertools.permutations(range(10)) # permutations(range(3)) --> 012 021 102 120 201 210
#
# a = itertools.islice(combinations,999999, None) # 0 = 0123456789, 999999 = 2783915460
#
# print("".join(str(x) for x in next(a)))

from operator import add

def getPermutations(a):
   if len(a)==1:
      yield a
   else:
      for i in range(len(a)):
         this = a[i]
         rest = a[:i] + a[i+1:]
         for p in getPermutations(rest):
            yield [this] + p

index = 0
for k in getPermutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    index += 1
    if index == 1000000:
        print(k)
        break