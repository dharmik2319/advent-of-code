from aocd import get, get_data

data = get_data(day=7,year=2022).splitlines()

dirs = {}

def addPath(path):
    if path not in dirs.keys():
        dirs[path] = 0

for line in data:
    if  not (line.startswith('$ cd ..') or line.startswith('$cd /')):


