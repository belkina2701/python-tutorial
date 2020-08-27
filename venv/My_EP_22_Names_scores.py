''' Names scores
Problem 22

INPUT:
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

OUTPUT: 871198282
'''

names_2 = []

with open('p022_names.txt') as file:
    names = file.read()
    names_1 = names.split(',')
    for i in names_1:
        y = i.strip('"')
        names_2.append(y)

names_2.sort()
# print(names_2)

alphabet = dict(A=1,B=2,C=3,D=4,E=5,F=6,G=7,H=8,I=9,
               J=10,K=11,L=12,M=13,N=14,O=15,P=16,Q=17,R=18,S=19,
               T=20,U=21,V=22,W=23,X=24,Y=25,Z=26)
n = 0
resalt = 0

for name in names_2:
    n += 1
    name_sum = 0
    for letra in name:
        for v, k in alphabet.items():
            if letra == v:
                name_sum += k
            res_name = name_sum * n
    # print(f'name = {name} / {res_name} = {name_sum} * {n}')
    resalt += res_name

print(resalt)