import re

one = list('VCWLRMFQ')
two = list('LQD')
three = list('BNCWGRSP')
four = list('GQBHDCL')
five = list('SZFLGV')
six = list('PNGD')
seven = list('WCFVPZD')
eight = list('SMDPC')
nine = list('CPMVTWNZ')

lsts = [one, two, three, four, five, six, seven, eight, nine]

maps = {
        '1':one,
        '2':two,
        '3':three,
        '4':four,
        '5':five,
        '6':six,
        '7':seven,
        '8':eight,
        '9':nine,
        }


for i in lsts:
    i.reverse()

def move(a, b):
    b.insert(len(b),a.pop(-1))

with open('day5.txt','r') as file:
    lines = file.read().splitlines()

lines = [list(filter(None, re.split('move | from | to ',i))) for i in lines]
lines = [[int(i) for i in line] for line in lines]

# for i in lines:
#     for j in range(i[0]):
#         move(maps[str(i[1])],maps[str(i[2])])
# 
# for i in lsts:
#     print(i[-1])

def moreMove(num,a,b):
    b.extend(a[len(a)-num:])
    del a[len(a)-num:]

for i in lines:
    moreMove(i[0],maps[str(i[1])],maps[str(i[2])])

for i in lsts:
    print(i[-1],end='')
