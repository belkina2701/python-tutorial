import time

start_time = time.time()

prime_array  = []

for i in range(1,100):
    midle_i = i // 2
    sum_i = 0
    array = []
    for div in range(1, midle_i + 1):
        if i % div == 0:
            array.append(div)
            sum_i += div
    if sum_i == 1:
        prime_array.append(i)

print(prime_array)

print(str(time.time()-start_time)+" seconds")

# var 2

start_time = time.time()

pr_array  = [2]
array = []

for i in range(3,100):
    array.append(i)
    for i in array:
        pr_array.append(i)
        for div in pr_array:
            if i // div == 0:
                array.remove(i)

print(prime_array)

print(str(time.time()-start_time)+" seconds")