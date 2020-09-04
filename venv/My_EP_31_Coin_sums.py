'''Coin sums - Problem 31
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

import time
start_time = time.time()

target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [1] + [0] * target # [1, 0, ... 0, 0] len 201

for coin in coins:
    for i in range(coin, 201):
        print(f'ways = {ways[i]} , {i = }, {coin = } , {ways[i-coin]}')
        ways[i] += ways[i-coin]
        print(f'{ways[i]} = ')

print(ways[target])

print(str(time.time()-start_time)+" seconds") # 0.0005257129669189453 seconds

# start_time = time.time()
#
# def fill(value, _max=200):
#     n = 0
#     for coin in [1,2,5,10,20,50,100,200]:
#         if coin > _max:
#             continue
#         if value - coin == 0:
#             return n + 1
#         if value - coin > 0:
#             n += fill(value - coin, coin)
#     return n
#
#
# print(fill(200))
# print(str(time.time()-start_time)+" seconds") # 1.771756649017334 seconds