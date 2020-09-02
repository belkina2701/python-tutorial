''' Digit fifth powers - Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 14 is not a sum it is not included.
The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
import time
start_time = time.time()

res = 0

for num_1 in range (0,10):
    for num_2 in range(0,10):
        for num_3 in range(0, 10):
            for num_4 in range(0, 10):
                for num_5 in range(0, 10):
                    for num_6 in range(0, 10):
                        summa = num_1**5 + num_2**5 + num_3**5 + num_4**5 + num_5**5 + num_6**5
                        number = str(num_1)+str(num_2)+str(num_3)+str(num_4)+str(num_5)+str(num_6)
                        if summa > 1:
                            if int(number) == summa:
                                print(number)
                                res += summa

print(res)

print(str(time.time()-start_time)+" seconds")
