''' Maximum path sum I
Problem 18

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
NOTE: As there are only 16384 routes, it is possible to solve this problem
by trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''

# нужно оставлять больший вариант сложения от каждого числа и к нему уже прибавлять нижнее

numbers = []

with open('problem18.txt') as file:
    lines = file.readlines()
    for line in lines:
        list1 = line.strip().split()
        list2 = map(int,list1)
        list3 = list(list2) # ленивое вычисление, надо в лист передать результат
        numbers.append(list3)

# print(numbers)

N = 15
numbers[0][0] = int(numbers[0][0])
for i in range(N):
    if i > 0: # rows 1-14
        for j in range(i + 1): # colomns 0 1, 0 1 2, ... , 0 1 2 ... 14
            if j == 0: # count summ of ferst colomn
                numbers[i][j] += numbers[i - 1][j]
            elif j == i: # count summ of last colomn
                numbers[i][j] += numbers[i - 1][j - 1]
            else:
                # print(f'{numbers[i][j]}  + max ({numbers[i - 1][j - 1]} hasta {numbers[i - 1][j]}')
                numbers[i][j] += max(numbers[i - 1][j - 1], numbers[i - 1][j])
                # print(f'res = {numbers[i][j]}')

print('Path with greatest sum:', max(numbers[N - 1][:]))



