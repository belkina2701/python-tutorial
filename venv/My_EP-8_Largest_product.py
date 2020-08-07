'''Largest product in a series
Problem 8

The four adjacent digits in the 1000-digit number that have the greatest product are
9 × 9 × 8 × 9 = 5832.

!!! я искала результат в массиве, а нужно искать множители!!!
исправлено в файле My_EP_8-2_Largest_product

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
'''

digit_number_1000 ='73167176531330624919225119674426574742355349194934\
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450'

# собрать в массив все цифры
def find_big_array(digit_number_1000, num_of_signs):
    array = []
    for i, item in enumerate(digit_number_1000):
        if item == '1':
            num = (digit_number_1000[i:i+num_of_signs])
            array.append(num)
        elif item == '2':
            num = (digit_number_1000[i:i+num_of_signs])
            array.append(num)
        elif item == '3':
            num = (digit_number_1000[i:i+num_of_signs])
            array.append(num)
        elif item == '4':
            num = (digit_number_1000[i:i+num_of_signs])
            array.append(num)
        elif item == '5':
            num = (digit_number_1000[i:i+num_of_signs])
            array.append(num)
        elif item == '6':
            num = (digit_number_1000[i:i+num_of_signs])
            array.append(num)
        elif item == '7':
            num = (digit_number_1000[i:i+num_of_signs])
            array.append(num)
        elif item == '8':
            num = (digit_number_1000[i:i+num_of_signs])
            array.append(num)
        elif item == '9':
            num = (digit_number_1000[i:i+num_of_signs])
            array.append(num)
    return array

# сотрируем массив от большего к меньшему
def sorted_array(array, largest_number):
    array_2 = []
    for i in array:
        i = int(i)
        if i <= largest_number:
            array_2.append(i)
    return array_2
    array_sort = sorted(array_2)
    array_big_num = reversed(array_sort)
    return array_big_num

# удаляем все номера меньше num_of_signs = 13, 12, 11 ... 3
def sorted_len_array(array_big_num, num_of_signs):
    len_array = []
    for i in array_big_num:
        i = str(i)
        if len(i) == num_of_signs:
            len_array.append(i)
    return len_array

# собрать массив из делителей
def find_divisors(num):
    div = 9
    array_div = []
    res_div = int(num)
    while div > 1:
        if res_div % div == 0:
            array_div.append(div)
            res_div = res_div / div
        else:
            div -= 1
    if div == 1:
        if res_div == 1:
            res_array_div = array_div
        else:
            res_array_div = None
    return res_array_div

num_of_signs = 13
largest_number = 9 ** 13 # 2541865828329

while num_of_signs >= 3:
    array = find_big_array(digit_number_1000, num_of_signs) # собрали массив
    # print(array)
    # print(len(array))
    array_big_num = sorted_array(array, largest_number) # отсортировали по уменьшению
    # print(array_big_num)
    # print(len(array_big_num))
    len_array = sorted_len_array(array_big_num,num_of_signs) # отсортировали по длине
    # print(len_array)
    # print(len(len_array))
    for num in len_array:
        divisor_array = find_divisors(num)
        if divisor_array is not None:
            if len(divisor_array) <= 13:
                print(divisor_array)
                print(len(divisor_array))
                print(num)
                break
    num_of_signs -= 1

