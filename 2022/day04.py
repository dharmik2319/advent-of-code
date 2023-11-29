from aocd import get_data
numOfOverlap = 0

lines = get_data(day=4,year=2022).splitlines()
# with open('day4.txt','r') as file:
#     lines = file.read().splitlines()

lines = [el.split(',') for el in lines]
lines = [[tuple(i.split('-')) for i in el] for el in lines]
lines = [[[int(i) for i in el] for el in line] for line in lines]
lines = [[tuple(i) for i in el] for el in lines]

for line in lines:
    if set(range(line[0][0],line[0][1]+1)).issubset(range(line[1][0],line[1][1]+1)) or set(range(line[1][0],line[1][1]+1)).issubset(range(line[0][0],line[0][1]+1)):
        numOfOverlap+=1
        pass
    else:
        pass

part2overlap = 0

for line in lines:
    if len(set(range(line[0][0],line[0][1]+1)).intersection(set(range(line[1][0],line[1][1]+1)))) > 0:
        part2overlap+=1
        pass
    else:
        pass
