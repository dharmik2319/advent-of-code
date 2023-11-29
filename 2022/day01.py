with open('day1.txt','r') as file:
    lines = file.read().split('\n\n')[:-1]

lines = [line.split('\n') for line in lines]

lines = [[int(i) for i in line] for line in lines]

max = sorted([sum(line) for line in lines])[-1]
