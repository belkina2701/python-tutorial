''' Lattice paths
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''

import time
start_time = time.time()

x = 1
y = 1
n = n_2 = 20
array = []
array_next = []

while n > 0:
    summa = x + y
    y = summa
    array.append(summa)
    n -= 1

while n_2-1 > 0:
    x = 1
    for i in array:
        y = i
        summa_2 = x + y
        x = summa_2
        array_next.append(summa_2)
    n_2 -= 1
    array = array_next
    array_next = []

print(summa_2)

print(str(time.time()-start_time)+" seconds")

# Algorithm de libro -  Recursive route-counting function

# def count_routes(m,n):
#     if n == 0 or m == 0:
#         return 1
#     else:
#         return count_routes(m, n-1) + count_routes(m-1, n)
# a = count_routes(20,20)
# print(a)




