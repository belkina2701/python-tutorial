''' Largest product in a grid
Problem 11
In the 20×20 grid below
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?
'''

import numpy as np
import pandas as pd

# Танцы с бубном что бы собрать массив 20*20
a = '08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08' \
    ' 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00' \
    ' 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65' \
    ' 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91' \
    ' 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80' \
    ' 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50' \
    ' 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70' \
    ' 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21' \
    ' 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72' \
    ' 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95' \
    ' 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92' \
    ' 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57' \
    ' 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58' \
    ' 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40' \
    ' 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66' \
    ' 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69' \
    ' 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36' \
    ' 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16' \
    ' 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54' \
    ' 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'
b = a.split(' ')
c = []
for i in b:
    c.append(int(i))
array_1 = np.array(c)

#
res = 0
array = array_1.reshape((20, 20))

# 1 этап смотрим на больший результат по горизонтали
row = 0

while row <= 19:
    column = 0
    while column <= 16:
        mult = array[row,column] * array[row,column+1] * array[row,column+2] * array[row,column+3]
        if mult > res:
            res = mult
        column += 1
    row += 1

print(f'1 этап - По горизонтали {res}')

# 2 этап смотрим на больший результат по вертикали
column = 0

while column <= 19:
    row = 0
    while row <= 16:
        mult = array[row,column] * array[row+1,column] * array[row+2,column] * array[row+3,column]
        if mult > res:
            res = mult
        row += 1
    column += 1

print(f'2 этап - По вертикали {res}')

# 3 этап смотрим на больший результат по диаганали вправо верх
column = 0
row = 0
n = 0

while n <= 16:
    row = 0
    column = n
    while column <= 16:
        mult = array[row, column] * array[row+1, column+1] * array[row+2, column+2] * array[row+3, column+3]
        if mult > res:
            res = mult
        row += 1
        column += 1
    n += 1

print(f'3 этап - по диаганали вправо верх {res}')

# 4 этап смотрим на больший результат по диаганали вправо низ
column = 0
row = 1
n = 1

while n <= 16:
    column = 0
    row = n
    while row <= 16:
        mult = array[row, column] * array[row+1, column+1] * array[row+2, column+2] * array[row+3, column+3]
        if mult > res:
            res = mult
        row += 1
        column += 1
    n += 1

print(f'4 этап - диаганали вправо низ {res}')

# 5 этап смотрим на больший результат по диаганали влево и вниз (верхняя часть)
column = 19
row = 0
n = 19

while n >= 3:
    row = 0
    column = n
    while column >= 3:
        mult = array[row, column] * array[row+1, column-1] * array[row+2, column-2] * array[row+3, column-3]
        if mult > res:
            res = mult
        row += 1
        column -= 1
    n -= 1

print(f'5 этап - по диаганали вЛево вниз (верхняя часть) {res}')

# 6 этап смотрим на больший результат по диаганали влево и вниз (нижняя часть)
column = 19
row = 1
n = 1

while n <= 16:
    column = 19
    row = n
    while row <= 16:
        mult = array[row, column] * array[row+1, column-1] * array[row+2, column-2] * array[row+3, column-3]
        if mult > res:
            res = mult
        row += 1
        column -= 1
    n += 1

print(f'6 этап - по диаганали вЛево вниз (нижняя часть) {res}')

