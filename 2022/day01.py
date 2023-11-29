from aocd import get, get_data
def main(num):
    lines = get_data(day=1,year=2022).split('\n\n')[:-1]
    lines = [line.split('\n') for line in lines]

    lines = [[int(i) for i in line] for line in lines]

    max = sum(sorted([sum(line) for line in lines])[-num:])
    return max
