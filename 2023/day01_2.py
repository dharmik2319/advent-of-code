from aocd import get_data

lines = get_data(day=1, year=2023).splitlines()

map_dict = {'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        }

for i, line in enumerate(lines):
    for num in map_dict:
        if num in line:
            lines[i] = lines[i].replace(num,f'{num}{map_dict[num]}{num}')
            continue
        continue
    continue
lines = [''.join(ch for ch in line if ch.isdigit()) for line in lines]
lines = [int(line[0] + line[-1]) for line in lines]
# print(lines)
# 
max = sum(lines)


