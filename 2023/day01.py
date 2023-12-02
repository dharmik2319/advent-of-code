from aocd import get_data
lines = get_data(day=1, year=2023).splitlines()
lines = [''.join(ch for ch in line if ch.isdigit()) for line in lines]
lines = [int(line[0] + line[-1]) for line in lines]
max = sum(lines)
